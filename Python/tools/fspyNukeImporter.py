"""Imports a camera from a fSpy exported json file.

   Wrapped version of Mitchell Kehn's fspyNukeImporter.py
   https://gist.github.com/MitchellKehn/e7ccdfad932886c7e9e4c072a08006c8
""" 

import json
import nuke

def import_camera():

    def Matrix4toList(M):
        mVals = []
        for i in range(len(M)):
            mVals.append(M[i])
        return mVals

    # ---  load file  ---
    fp = nuke.getFilename("Select fSpy data file", "*.json")

    if not fp:
        return

    with open(fp) as datafile:
        data = json.load(datafile)

    # ---  create camera, set knobs
    camera = nuke.createNode("Camera")

    # camera transform
    M = nuke.math.Matrix4()  # camera pose
    matrixVals = data["cameraTransform"]["rows"]
    for row, values in enumerate(matrixVals):
        rowStart = row * 4
        M[rowStart + 0] = values[0]
        M[rowStart + 1] = values[1]
        M[rowStart + 2] = values[2]
        M[rowStart + 3] = values[3]

    camera["useMatrix"].setValue(True)
    camera["matrix"].setValue(Matrix4toList(M))


    # projection parameters
    aspectRatio = float(data["imageWidth"]) / float(data["imageHeight"])
    camera["vaperture"].setExpression("haperture / {aspect}".format(aspect=aspectRatio))
    camera["focal"].setExpression("haperture / (2 * tan({hFOV} / 2))".format(hFOV=data["horizontalFieldOfView"]))

    principal = data["principalPoint"]
    camera["win_translate"].setValue([principal["x"], principal["y"]])
