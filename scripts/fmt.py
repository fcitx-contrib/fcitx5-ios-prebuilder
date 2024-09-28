from common import Builder

Builder('fmt', [
    '-DFMT_TEST=OFF',
    '-DFMT_DOC=OFF'
]).exec()
