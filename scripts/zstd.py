from common import Builder

Builder('zstd', [
    '-DZSTD_LEGACY_SUPPORT=OFF',
    '-DZSTD_BUILD_PROGRAMS=OFF',
    '-DZSTD_BUILD_TESTS=OFF',
    '-DZSTD_BUILD_SHARED=OFF'
], src='build/cmake', build='build-zstd').exec()
