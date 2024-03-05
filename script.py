import hou
import sys

# script.py is as the specified Houdini project with shell file (batch_process.sh)

hip_file = sys.argv[1]
input_file = sys.argv[2]

hou.hipFile.load(hip_file)

file_node = hou.node("/obj/geo1/file1") # file node in Houdini project
file_node.parm("file").set(input_file)

name_node = hou.node("/obj/geo1/set_name") # attribute wrangler node in Houdini project
name_node.parm("name").set(input_file)

export_node = hou.node("/obj/geo1/set_name")
export_node.parm("file").set(input_file + "remeshed.bgeo.sc")
export_node.parm("execute").pressButton()