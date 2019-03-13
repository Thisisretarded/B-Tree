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

from bptsubnode import bptsubnode

Class bptNode(list):
    """Node class for B+Tree of order 3"""

    def __init__(self, data, key, order = 4, isleaf = True):
       self.node = [ bptsubnode(data, key), None ]
       self.order = order
       self.isleaf = isleaf


    def insert(self, key):
        pass

    def len(self):
        return self.__len__() - 1