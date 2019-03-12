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

Class bptNode:
    """Node class for B+Tree of order 3"""

    def __init__(self, order = 2, **kwargs, isleaf = True):
        z = dict()

        self.isleaf = isleaf
        for x in range(order):


    def insert(self, key):
