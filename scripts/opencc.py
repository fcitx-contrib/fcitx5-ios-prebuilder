from common import Builder, cache, ensure, patch

project = 'opencc'

prebuilt = 'opencc-arm64.tar.bz2'
url = f'https://github.com/fcitx-contrib/fcitx5-macos-prebuilder/releases/download/latest/{prebuilt}'

cache(url)
directory = 'build/opencc/usr'
ensure('mkdir', ['-p', directory])
ensure('tar', [
    'xjvf',
    f'cache/{prebuilt}',
    '-C',
    directory,
    'share'
])

patch(project)

Builder(project, [
    '-DUSE_SYSTEM_MARISA=ON',
    '-DENABLE_DARTS=OFF'
], dep=True).exec()
