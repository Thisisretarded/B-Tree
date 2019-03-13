""" class module for creating B+tree of order 3 by using bptNode from bptnode.py module"""

from bptnode import bptnode
class bptree:
    """ class to initiate a B+ Tree and performing operations like insert delete and search"""
    def __init__(self):
        self.root = None

    def insert(self, data = None, key = None):
        """insert function for bptree"""
        
