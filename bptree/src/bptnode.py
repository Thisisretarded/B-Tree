"""
Date: March 12 2019
creator: RT2

Class file for Node of a BPlusTree of order 3(2Keys and 3Pointers)

following will be the structure os a node

            #####################################################
            ##    ##             ##     ##               ##    ##
            ##    ##             ##     ##               ##    ##
            ## P1 ##     K1      ## P2  ##       K2      ## p3 ##
            ##    ##             ##     ##               ##    ##
            ##  1 ##      2      ##  3  ##        4      ##  5 ##
            ##    ##             ##     ##               ##    ##
            #####################################################
"""

from .bptsubnode import bptsubNode

class bptNode(list):
    """Node class for B+Tree of order 3"""
    def __init__(self, order = 4, isleaf = True):
       self.order = order
       self.isleaf = isleaf
       self.node = [bptsubNode() for _ in range(self.order+1)]
       self.node[-1].key = "Magic"

    @classmethod
    def find(self, key, node):
        """searches for the index where key needs to be inserted"""
        for x in range(len(node) -1):
            if node[x].key < key and node[x].key is not None:
                continue
            else:
                return x

    def insert(self, key, data):
        if self.isleaf:
            if not self.node[-2].key:    # Node is not full #keyy comparison
                subnode = bptsubNode(data = data, key = key)
                index = bptNode.find(key, self.node)
                if not self.node[-2].key:  ##Node is not full check
                    self.node.insert(index, subnode)
                else:
                    print("splitting needs to be done here")


#    def len(self):
#       return self.__len__() - 13
