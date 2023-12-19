import nuke

if not nuke.env['studio']:

	nuke.pluginAddPath('Python')

	from tools import paths
	from tools import fspyNukeImporter as fspy

	menubar = nuke.menu("Nuke")

	tools = menubar.addMenu(name='Tools', index=6)

	tools.addCommand('Convert Paths to Relative', 'paths.relative_paths()')
	tools.addCommand('Import fSpy Camera', 'fspy.import_camera()')
