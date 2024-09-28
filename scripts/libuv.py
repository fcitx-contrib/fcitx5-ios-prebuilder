from common import Builder, patch

project = 'libuv'

patch(project)

Builder(project, [
    '-DLIBUV_BUILD_SHARED=OFF',
    '-DLIBUV_BUILD_TESTS=OFF'
]).exec()
