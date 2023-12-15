import nuke
import os
from pathlib import PureWindowsPath

def relative_paths():
    """Converts absolute paths to relative and sets the project directory"""

    script_directory = nuke.script_directory()

    if script_directory:
        nuke.root()['project_directory'].setValue('[python {nuke.script_directory()}]')

        # Read and Writes are sufficient for now
        nodes = nuke.allNodes('Read')
        nodes += nuke.allNodes('Write')

        for node in nodes:
            path = nuke.filename(node)
            # If instead node['file'].value() is used:
            # path = os.path.normpath(os.path.join(script_directory, path))

            relative = os.path.relpath(path, script_directory)
            # Convert it if windows
            if os.name == 'nt':
                relative = PureWindowsPath(relative).as_posix()

            node['file'].setValue(relative)

        nuke.message('Finished converting paths to relative.\nIf there are no errors, SAVE the script.')
        # Maybe we save the script for them?
        # nuke.ask('Finished converting paths to relative.\nDo you want to overwrite it?')
    else:
        nuke.alert('The script is not saved yet :(\nSave it and then try again.')

