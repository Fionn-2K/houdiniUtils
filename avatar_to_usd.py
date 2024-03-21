import hou
import os


class RPMAvatarToUsd:
    def __init__(self, dir_path: str):
        self.dir_path = dir_path
        self.obj_path = "/obj"
        self.prim_path_prefix = "ReadyPlayerMe_avatar_"
        self.sop_prefix = "SOP_"
        self.asset_name = ""

    ## Import GLB file and create glTF Hierarchy node
    def importReadyPlayerMeAvatar(self):
        # Get first GLB file in dir_path
        glb_file = [file for file in os.listdir(self.dir_path) if file.endswith(".glb")][0]
        self.asset_name = glb_file[:-4]

        # Setup glTF hierarchy. This will import the GLB which contains model & materials
        hierarchy_node = hou.node(self.obj_path).createNode("gltf_hierarchy", self.asset_name)
        hierarchy_node.parm("filename").set(self.dir_path + "/" + self.asset_name + ".glb")
        hierarchy_node.parm("flattenhierarchy").set(1)
        hierarchy_node.parm("importcustomattributes").set(0)
        hierarchy_node.parm("buildscene").pressButton()

        # self.createTemplate()

    def createTemplate(self):
        pass


    def execute(self):
        # self.importReadyPlayerMeAvatar() # use await?
        self.createTemplate()

