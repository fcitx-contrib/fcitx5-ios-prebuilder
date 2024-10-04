from common import Builder

Builder('json-c', [
    '-DDISABLE_WERROR=YES', # https://github.com/json-c/json-c/issues/808
    '-DBUILD_TESTING=OFF',
    '-DBUILD_APPS=OFF',
    '-DDISABLE_EXTRA_LIBS=ON'
]).exec()
