"""test class for testing bptnode class"""

from ..src.bptnode import bptNode
from ..src.bptsubnode import bptsubNode

def test_node():
    #creating a node of order 6, hence 7 subnodes and 7 possible childs/poinnters
    node = bptNode(order = 6)
    # key for last subnode would be "Magic"
    assert node.node[6].key == "Magic"
    #asserting order of node
    assert node.order == 6
    #length check
    assert node.node.__len__() == (7)
    # freshly created node has keys as None except last subnode
    for x in range(node.order-1):
        assert node.node[x].key is None

def test_subnode():
    x = bptsubNode(data = "data", key = 123)
    assert x.data == "data"
    assert x.key == 123
    y = bptsubNode()
    assert y.data is None
    assert y.key is None