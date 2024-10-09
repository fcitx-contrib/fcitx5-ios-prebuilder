from common import Builder

Builder('librime', [
    '-DBUILD_TEST=OFF'
]).exec()
