from common import Builder, patch

project = 'libintl'

patch(project)

Builder(project).exec()
