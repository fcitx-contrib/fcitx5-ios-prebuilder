import os
from common import Builder, POSTFIX, cache, ensure

version = '1.86.0'

boost_dir = f'boost-{version}'
boost_tar = f'{boost_dir}-cmake.tar.xz'
url = f'https://github.com/boostorg/boost/releases/download/{boost_dir}/{boost_tar}'
cache(url)

if not os.path.isdir(boost_dir):
    ensure('tar', [
        'xJf',
        f'cache/{boost_tar}',
        '-C',
        '.'
    ])

cwd = os.getcwd()

Builder(boost_dir, [
    '-DBOOST_INCLUDE_LIBRARIES="algorithm;bimap;container;crc;interprocess;iostreams;multi_index;ptr_container;scope_exit;signals2;uuid"',
    '-DBOOST_IOSTREAMS_ENABLE_BZIP2=Off',
    '-DBOOST_IOSTREAMS_ENABLE_ZLIB=Off',
    '-DBOOST_IOSTREAMS_ENABLE_LZMA=Off',
    '-DBOOST_IOSTREAMS_ENABLE_ZSTD=Off'
], dep=True).exec()

os.chdir(f'{cwd}/build')
ensure('mv', [
    f'{boost_dir}{POSTFIX}.tar.bz2',
    f'boost{POSTFIX}.tar.bz2'
])
