import nuke

__author__ = 'Makis Stergiou'
__course__ = 'BUas FVFX Y1'

if not nuke.env['studio']:

	nuke.pluginAddPath('Python')

	from tools import paths

	menubar = nuke.menu("Nuke")

	tools = menubar.addMenu(name='Tools', index=6)

	tools.addCommand('Convert Paths to Relative', 'paths.relative_paths()')
