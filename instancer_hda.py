import hou

def execute():
    num_assets = hou.pwd().parm("assets").eval()

    ## get 'root' path
    main_root_path = hou.pwd().parent().path()

    ## main subnet
    subnet = hou.node(main_root_path).createNode("subnet", "instancer")
    root_path = subnet.path()

    ## move target to subnet
    target_obj_merge = hou.node(root_path).createNode("object_merge")
    target_obj_merge.parm("xformtype").set(1)
    target_obj_merge.parm("objpath1").set(hou.pwd().parm("target").eval())

    ## merge node
    merge_node = hou.node(root_path).createNode("merge")

    ## target node operations
    scatter_node = target_obj_merge.createOutputNode("scatter")
    scatter_node.parm("relaxpoints").set(0)

    ## Attribute randomise
    attr_rand_name = scatter_node.createOutputNode("attribrandomize")
    attr_rand_name.parm("name").set("name")
    attr_rand_name.parm("distribution").set("discrete")
    attr_rand_name.parm("valuetype").set(1)
    attr_rand_name.parm("values").set(num_assets)

    for i in range(num_assets):
        prim_name = hou.pwd().parm("asset{}".format(i + 1)).eval().split("/")[-1]
        node = hou.node(root_path).createNode("object_merge", prim_name)
        node.parm("xformtype").set(1)
        node.parm("objpath1").set(hou.pwd().parm("asset{}".format(i + 1)).eval())
        pack_node = node.createOutputNode("pack")
        name_node = pack_node.createOutputNode("name")
        name_node.parm("name1").set(node.name())
        merge_node.setNextInput(name_node)
        attr_rand_name.parm("strvalue{}".format(i)).set(node.name())
        node.moveToGoodPosition()

    merge_node.moveToGoodPosition()

    ## copy to points
    copy_node = hou.node(root_path).createNode("copytopoints::2.0")
    copy_node.parm("useidattrib").set(1)
    copy_node.parm("idattrib").set("name")
    copy_node.setInput(0, merge_node)
    copy_node.setInput(1, attr_rand_name)
    copy_node.moveToGoodPosition()


##########################################################################

""" BACK-UP v1 - BEFORE REFACTOR
nodes = [] ## empty atrray
num_assets = hou.pwd().parm("assets").eval() ## all nodes in assets array
#print(num_assets)

for i in range(num_assets):
    nodes.append(hou.node(hou.pwd().parm("asset{}".format(i+1)).eval()))

## create 'pack' and 'name' nodes for each node in the 'nodes' array
name_nodes = []
for node in nodes:
    pack_node = node.createOutputNode("pack")
    name_node = pack_node.createOutputNode("name")
    name_node.parm("name1").set(node.name())
    name_nodes.append(name_node)

## get 'root' path
root_path = hou.pwd().parent().path()

## create 'merge' node and connect all 'name_nodes' to it
merge_node = hou.node(root_path).createNode("merge")
for name_node in name_nodes:
    merge_node.setNextInput(name_node)
merge_node.moveToGoodPosition()

## Target
target_node = hou.node(hou.pwd().parm("target").eval())
scatter_node = target_node.createOutputNode("scatter")
scatter_node.parm("relaxpoints").set(0)

## Attribute randomise
attr_rand_name = scatter_node.createOutputNode("attribrandomize")
attr_rand_name.parm("name").set("name")
attr_rand_name.parm("distribution").set("discrete")
attr_rand_name.parm("valuetype").set(1)
attr_rand_name.parm("values").set(num_assets)

for x, node in enumerate(nodes):
    attr_rand_name.parm("strvalue{}".format(x)).set(node.name())

## copy to points
copy_node = hou.node(root_path).createNode("copytopoints::2.0")
copy_node.parm("useidattrib").set(1)
copy_node.parm("idattrib").set("name")
copy_node.setInput(0, merge_node)
copy_node.setInput(1, attr_rand_name)
copy_node.moveToGoodPosition()

"""

################################################################


""" BACK-UP v2 - refactor
num_assets = hou.pwd().parm("assets").eval()

## get 'root' path
root_path = hou.pwd().parent().path()

## merge node
merge_node = hou.node(root_path).createNode("merge")

## target node operations
target_node = hou.node(hou.pwd().parm("target").eval())
scatter_node = target_node.createOutputNode("scatter")
scatter_node.parm("relaxpoints").set(0)

## Attribute randomise
attr_rand_name = scatter_node.createOutputNode("attribrandomize")
attr_rand_name.parm("name").set("name")
attr_rand_name.parm("distribution").set("discrete")
attr_rand_name.parm("valuetype").set(1)
attr_rand_name.parm("values").set(num_assets)

for i in range(num_assets):
    node = hou.node(hou.pwd().parm("asset{}".format(i+1)).eval())
    pack_node = node.createOutputNode("pack")
    name_node = pack_node.createOutputNode("name")
    name_node.parm("name1").set(node.name())
    merge_node.setNextInput(name_node)
    attr_rand_name.parm("strvalue{}".format(i)).set(node.name())

merge_node.moveToGoodPosition()

## copy to points
copy_node = hou.node(root_path).createNode("copytopoints::2.0")
copy_node.parm("useidattrib").set(1)
copy_node.parm("idattrib").set("name")
copy_node.setInput(0, merge_node)
copy_node.setInput(1, attr_rand_name)
copy_node.moveToGoodPosition()

"""

###################################################################

""" BACK-UP v3 - create subnetwork container
num_assets = hou.pwd().parm("assets").eval()

## get 'root' path
main_root_path = hou.pwd().parent().path()

## main subnet
subnet = hou.node(main_root_path).createNode("subnet","instancer")
root_path = subnet.path()

## move target to subnet
target_obj_merge = hou.node(root_path).createNode("object_merge")
target_obj_merge.parm("xformtype").set(1)
target_obj_merge.parm("objpath1").set(hou.pwd().parm("target").eval())

## merge node
merge_node = hou.node(root_path).createNode("merge")

## target node operations
scatter_node = target_obj_merge.createOutputNode("scatter")
scatter_node.parm("relaxpoints").set(0)

## Attribute randomise
attr_rand_name = scatter_node.createOutputNode("attribrandomize")
attr_rand_name.parm("name").set("name")
attr_rand_name.parm("distribution").set("discrete")
attr_rand_name.parm("valuetype").set(1)
attr_rand_name.parm("values").set(num_assets)

for i in range(num_assets):
    prim_name = hou.pwd().parm("asset{}".format(i+1)).eval().split("/")[-1]
    node = hou.node(root_path).createNode("object_merge", prim_name)
    node.parm("xformtype").set(1)
    node.parm("objpath1").set(hou.pwd().parm("asset{}".format(i+1)).eval())
    pack_node = node.createOutputNode("pack")
    name_node = pack_node.createOutputNode("name")
    name_node.parm("name1").set(node.name())
    merge_node.setNextInput(name_node)
    attr_rand_name.parm("strvalue{}".format(i)).set(node.name())
    node.moveToGoodPosition()

merge_node.moveToGoodPosition()

## copy to points
copy_node = hou.node(root_path).createNode("copytopoints::2.0")
copy_node.parm("useidattrib").set(1)
copy_node.parm("idattrib").set("name")
copy_node.setInput(0, merge_node)
copy_node.setInput(1, attr_rand_name)
copy_node.moveToGoodPosition()
"""

