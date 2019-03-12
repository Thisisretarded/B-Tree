""" class module for creating B+tree of order 3 by using bptNode from bptnode.py module"""

class bptree:
    """ class to initiate a B+ Tree and performing operations like insert delete and search"""
    def __init__(self, k1 = None):
        self.root = None

    def insert