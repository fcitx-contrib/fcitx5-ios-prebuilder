import os
import platform

INSTALL_PREFIX = '/usr'
IOS_VERSION = 15

POSTFIX = '-' + platform.machine() if os.environ['IOS_PLATFORM'] == 'SIMULATOR' else ''

def ensure(program: str, args: list[str]):
    command = " ".join([program, *args])
    print(command)
    if os.system(command) != 0:
        raise Exception("Command failed")


def patch(project: str, src: str | None = None, dst: str | None = None):
    if src and dst:
        ensure('cp', [
            f'patches/{src}',
            f'{project}/{dst}'
        ])
    else:
        ensure('git', [
            'apply',
            f'--directory={project}',
            f'patches/{project}.patch'
        ])


def cache(url: str):
    file = url[url.rindex('/') + 1:]
    path = f'cache/{file}'
    if os.path.isfile(path):
        print(f'Using cached {file}')
        return
    ensure('wget', [
        '-P',
        'cache',
        url
    ])


class Builder:
    def __init__(self, name: str, options: list[str] | None=None, src='.', build='build', dep=False):
        self.name = name
        self.root = os.getcwd()
        self.destdir = f'{self.root}/build/{self.name}'
        self.options = options or []
        self.src = src
        self.build_ = build
        self.dep = dep

    def configure(self):
        os.environ['PKG_CONFIG_PATH'] = f'{self.root}/build/sysroot/usr/lib/pkgconfig'
        os.chdir(f'{self.root}/{self.name}')
        ensure('cmake', [
            '-B', self.build_, '-G', 'Xcode',
            '-S', self.src,
            f'-DCMAKE_TOOLCHAIN_FILE={self.root}/ios.cmake',
            f'-DIOS_PLATFORM={os.environ["IOS_PLATFORM"]}',
            '-DBUILD_SHARED_LIBS=OFF',
            f'-DCMAKE_INSTALL_PREFIX={INSTALL_PREFIX}',
            f'-DCMAKE_FIND_ROOT_PATH={self.root}/build/sysroot/usr',
            f'-DCMAKE_OSX_DEPLOYMENT_TARGET={IOS_VERSION}',
            *self.options
        ])

    def build(self):
        ensure('cmake', ['--build', self.build_, '--config', 'Release'])

    def install(self):
        os.environ['DESTDIR'] = self.destdir
        ensure('cmake', ['--install', self.build_])

    def package(self):
        os.chdir(f'{self.destdir}{INSTALL_PREFIX}')
        ensure('tar', ['cjvf', f'{self.destdir}{POSTFIX}.tar.bz2', '*'])

    def extract(self):
        directory = 'build/sysroot/usr'
        os.chdir(self.root)
        ensure('mkdir', ['-p', directory])
        ensure('tar', ['xjvf', f'{self.destdir}{POSTFIX}.tar.bz2', '-C', directory])

    def exec(self):
        self.configure()
        self.build()
        self.install()
        self.package()
        if self.dep:
            self.extract()
