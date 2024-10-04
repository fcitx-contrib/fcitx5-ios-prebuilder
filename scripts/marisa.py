from common import Builder

Builder('marisa', [
    '-DBUILD_TOOLS=OFF'
],dep=True).exec()
