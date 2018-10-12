#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function

class Node:
    left_child = None
    right_child = None
    def __init__(self, data):
        self.data = data

class Binary_search_tree:
    def __init__(self):
        self.root = None
        self.count = 0
    
    def insert(self, data):
        if self.is_empty():
            self.root = Node(data)
            self.count += 1
            return true
        else:
            return internal_insert(self.root, data)

    def internal_insert(self, root, data):
        if root.data == data:
            print("Same data already exist!")
            return False
        elif root.data > data:
            if root.left_child is not None:
                return self.internal_insert(root.left_child, data)
            else:
                self.count += 1
                root.left_child = Node(data)
                return True
        else:
            if root.right_child is not None:
                return self.internal_insert(root.right_child, data)
            else:
                self.count += 1
                root.right_child = Node(data)
                return True


    def delete(self, data):
        if self.root is None:
            print("The Tree is empty!")
            return False
        return self.internal_delete(self.root, data)

    def internal_delete(self, root, data):
        if root is None:
            print("There are no data what you want to delete!")
            return False

        if root.data > data:
            internal_delete(root.left_child, data)
        elif root.data < data:
            internal_delete(root.right.child, data)
        else:
            if (root.left_child is None) and (root.right_child is None):
                pass
       

    def FindMinNode(self, root):
        pass

    def BSTSize(self):
        return self.count

    def is_empty(self):
        return self.root is None


