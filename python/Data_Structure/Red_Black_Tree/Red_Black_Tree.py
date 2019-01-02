#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from enum import Enum

class COLOR(Enum):
    RED = 0
    BLACK = 1

class Node:
    color = 0
    parent = None
    left_child = None
    right_child = None
    def __init__(self, data):
        self.data = data

class Red_Black_Tree:
    def __init__(self):
        self.root = None
        self.count = 0
    
    def insert(self, data):
        if self.is_empty():
            self.root = Node(data)
            self.count += 1
            return True
        else:
            return self._internal_insert(self.root, data)

    def delete(self, data):
        if self.root is None:
            print("The Tree is empty!")
            return False
        return self._internal_delete(self.root, data)

    def RBTSize(self):
        print("Total BST Size : ", self.count)
        return 

    def is_empty(self):
        return self.root is None

    
    def preorder(self):
        print("- Preorder Traversal")
        self._internal_preorder(self.root)
        print("")

    def _internal_preorder(self, root):
        print(root.data, end=" ")
        if root.left_child is not None:
            self._internal_preorder(root.left_child)
        if root.right_child is not None:
            self._internal_preorder(root.right_child)

    def postorder(self):
        print("- Postorder Traversal")
        self._internal_postorder(self.root)
        print("")

    def _internal_postorder(self, root):
        if root.left_child is not None:
            self._internal_postorder(root.left_child)
        if root.right_child is not None:
            self._internal_postorder(root.right_child)
        print(root.data, end=" ")

    def inorder(self):
        print("- Inorder Traversal")
        self._internal_inorder(self.root)
        print("")

    def _internal_inorder(self, root):
        if root.left_child is not None:
            self._internal_inorder(root.left_child)
        print(root.data, end=" ")
        if root.right_child is not None:
            self._internal_inorder(root.right_child)
