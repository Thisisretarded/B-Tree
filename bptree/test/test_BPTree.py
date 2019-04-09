"""This is test module for BPTree module/s"""

from ..src.bptree import bptree

s = bptree(order = 3)

def test_insert():
    """test insertion of subnodes in BPtree"""
    s.insert(key = 10)
    assert s.root.node[0].key == 10
    s.insert(key = 15)
    assert s.root.node[1].key == 15
    s.insert(key = 12)
    assert s.root.node[1].key == 12
    assert s.root.node[2].key == 15
    s.insert(key = 17)
    assert s.root.node[3].key == 17


def test_root():
    """test class for checking root node"""
    assert s.root.node[3].key == "Magic"