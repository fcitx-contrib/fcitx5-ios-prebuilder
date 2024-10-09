from common import Builder, patch

project = 'leveldb'

patch(project)

Builder(project, [
    '-DLEVELDB_BUILD_BENCHMARKS=OFF',
    '-DLEVELDB_BUILD_TESTS=OFF'
], dep=True).exec()
