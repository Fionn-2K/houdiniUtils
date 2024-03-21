import hou
import os


class RPMAvatarToUsd:
    def __init__(self, dir_path: str):
        self.dir_path = dir_path
        self.obj_path = "/obj"
        self.stage_path = "/stage"
        self.prim_path_prefix = "ReadyPlayerMe_avatar_"
        self.sop_prefix = "SOP_"
        self.asset_name = ""
        self.asset_full_path = ""

    ## Import GLB file and create glTF Hierarchy node
    def importReadyPlayerMeAvatar(self):
        # Get first GLB file in dir_path
        glb_file = [file for file in os.listdir(self.dir_path) if file.endswith(".glb")][0]
        self.asset_name = glb_file[:-4]
        self.asset_full_path = self.dir_path + "/" + self.asset_name + ".glb"

        # Setup glTF hierarchy. This will import the GLB which contains model & materials
        hierarchy_node = hou.node(self.obj_path).createNode("gltf_hierarchy", self.asset_name)
        hierarchy_node.parm("filename").set(self.asset_full_path)
        hierarchy_node.parm("flattenhierarchy").set(1)
        hierarchy_node.parm("importcustomattributes").set(0)
        hierarchy_node.parm("buildscene").pressButton()

        # self.createTemplate()

    ## Create ReadyPlayerMe avatar to USD template. Export USD at the end.
    def createTemplate(self):
        ## SOP create
        sop_create = self.createSop()

        # primitive
        prim_node = hou.node(self.stage_path).createNode("primitive")
        prim_node.parm("primpath").set(self.prim_path_prefix + self.asset_name)
        prim_node.parm("primkind").set("component")

        # graft stages
        graft_stage = prim_node.createOutputNode("graftstages")
        graft_stage.setNextInput(sop_create)
        graft_stage.parm("primkind").set("subcomponent")

        ##TODO material library & usd export

    ## Create SOP Create node
    def createSop(self):
        sop_create = hou.node(self.stage_path).createNode("sopcreate", self.sop_prefix + self.asset_name)
        sop_create.parm("enable_partitionattribs").set(0)

        # glTF file
        gltf_file = hou.node(sop_create.path() + "/sopnet/create").createNode("gltf")
        gltf_file.parm("filename").set(self.asset_full_path)
        gltf_file.parm("usecustomattribs").set(0)
        gltf_file.parm("materialassigns").set(1)

        # attribute wrangler
        attrib_wrangle = gltf_file.createOutputNode("attribwrangle")
        attrib_wrangle.parm("class").set(1)
        attrib_wrangle.parm("snippet").set(
            'string assets = split(s@shop_materialpath, "/")[-1];\n\ns@path = "/" + assets;')

        # attirbute delete
        attrib_delete = attrib_wrangle.createOutputNode("attribdelete")
        attrib_delete.parm("primdel").set("name shop_materialpath")

        # output
        output_node = attrib_delete.createOutputNode("output")

        return sop_create


    def execute(self):
        # self.importReadyPlayerMeAvatar() # use await?
        self.createTemplate()

