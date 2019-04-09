""" class module for creating B+tree of order 3 by using bptNode from bptnode.py module"""

from .bptnode import  bptNode

class bptree:
    """ class to initiate a B+ Tree and performing operations like insert delete and search"""
    def __init__(self, order):
        self.root = bptNode(order = order)

    def insert(self, data = None, key = None):
        """insert function for bptree"""
        # find the node where key:data value needs to be inserted
        node, parent = self._find(key)
        node.insert(key, data)



    def _find(self, key):
        """find the leaf node where key:value needs to be inserted and returns it"""
        parent = None
        child = self.root
        while not child.isleaf:
            parent = child
            child = child.node[self._findindex(child, key)].data
        return child, parent


    def _findindex(child, key):
        """Find the leaf node where subnode needs to be inserted"""
        child.find(key, child.node )
        return index