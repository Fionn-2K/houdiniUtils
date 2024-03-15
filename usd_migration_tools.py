import os
import hou

class USDMigrationUtils:
    def __init__(self):
        pass

    def test(self):
        print("Hello from USD tools")

    def createMainTemplate(self, dir_path: str):
        print("Execute template structure...")

        # get the first FBX file in the "dir_path" param.
        fbx_file = [file for file in os.listdir(dir_path) if file.endswith(".fbx")][0]
        print(fbx_file)

        # sopcreate lop node
        root_path = "/stage"
        sopcreate_lop = hou.node(root_path).createNode("sopcreate", "asset01")
        sopcreate_lop.parm("enable_partitionattribs").set(0)

        # file sop node
        file_sop = hou.node(sopcreate_lop.path() + "/sopnet/create").createNode("file")
        file_sop.parm("file").set(dir_path + "/" + fbx_file)

        # begin loop
        for_each_begin = file_sop.createOutputNode("block_begin", "foreach_begin1")
        #for_each_begin.parm("method").set(1)
        for_each_begin.parm("blockpath").set("../foreach_end1")
        for_each_begin.parm("createmetablock").pressButton()
        meta_node = hou.node(for_each_begin.parent().path() + "/foreach_begin1_metadata1")
        #meta_node.parm("method").set(2)
        meta_node.parm("blockpath").set("../foreach_end1")

        # attribute wrangle node
        attr_wrangle = for_each_begin.createOutputNode("attribwrangle")
        attr_wrangle.setInput(1, meta_node)
        attr_wrangle.parm("class").set(1)
        attr_wrangle.parm("snippet").set('string assets[] = {"leaves","trunk","twigs","leaves_small"};\n\ns@path = "/" + assets[detail(1,"iteration")];')

        # end loop
        for_each_end = attr_wrangle.createOutputNode("block_end", "foreach_end1")
        for_each_end.parm("itermethod").set(1)
        for_each_end.parm("method").set(1)
        for_each_end.parm("class").set(0)
        for_each_end.parm("useattrib").set(1)
        for_each_end.parm("attrib").set("shop_materialpath")
        for_each_end.parm("blockpath").set("../foreach_begin1")
        for_each_end.parm("templatepath").set("../foreach_begin1")

        # attribute delete node
        attrib_delete = for_each_end.createOutputNode("attribdelete")
        attrib_delete.parm("ptdel").set("fbx_rotation fbx_scale fbx_translation")
        attrib_delete.parm("primdel").set("shop_materialpath MaxHandle name")

        # output node
        output_sop = attrib_delete.createOutputNode("output")



