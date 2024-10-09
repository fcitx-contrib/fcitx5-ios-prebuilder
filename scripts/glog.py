from common import Builder

Builder('glog', [
    '-DWITH_GFLAGS=OFF',
    '-DWITH_UNWIND=OFF',
    '-DBUILD_EXAMPLES=OFF',
    '-DBUILD_TESTING=OFF'
], dep=True).exec()
