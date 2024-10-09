from common import Builder

Builder('yaml-cpp', [
    '-DYAML_CPP_BUILD_CONTRIB=OFF',
    '-DYAML_CPP_BUILD_TESTS=OFF',
    '-DYAML_CPP_BUILD_TOOLS=OFF'
], dep=True).exec()
