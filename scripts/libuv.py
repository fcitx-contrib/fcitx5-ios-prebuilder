from common import Builder

Builder('libuv', [
    '-DLIBUV_BUILD_SHARED=OFF',
    '-DLIBUV_BUILD_TESTS=OFF'
]).exec()
