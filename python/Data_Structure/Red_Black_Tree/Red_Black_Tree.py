#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function

RED = 0
BLACK = 1

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = self.left_child = self.right_child = None
        self.color = RED

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


class Red_Black_Tree:
    def __init__(self):
        self.root = None
        self.count = 0
    
    def insert(self, data):
        if self.is_empty():
            self.root = Node(data)
            self.root.set_color = BLACK
            self.count += 1
            return True
        else:
            if(self._internal_insert(self.root, data)):
                fixInsertRBtree(self.root, data)
                self.root.set_color = BLACK
            return 

    def _internal_insert(self, root, data):
        if root.data is data:
            print("Same data already exist!")
            return False
        elif root.data > data:
            if root.left_child is not None:
                return self._internal_insert(root.left_child, data)
            else:
                self.count += 1
                root.left_child = Node(data)
                root.left_child.parent = root
                return True
        else:
            if root.right_child is not None:
                return self._internal_insert(root.right_child, data)
            else:
                self.count += 1
                root.right_child = Node(data)
                root.right_child.parent = root
                return True

    def delete(self, data):
        if self.root is None:
            print("The Tree is empty!")
            return False
        return self._internal_delete(self.root, data)


    def fixInsertRBtree(self, root, data):
        if root.data > data:
            self.fixInsertRBtree(root.left_child, data)
        elif root.data < data:
            self.fixInsertRBtree(root.right_child, data)
        else:
            cnode = root
            parent = root.parent
            grandparent = parent.parent
            while (root is not self.root) and (root.get_color is RED) and (root.parent.get_color is RED):

                a=10





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
