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
            return _internal_insert(self.root, data)

    def _internal_insert(self, root, data):
        if root.data == data:
            print("Same data already exist!")
            return False
        elif root.data > data:
            if root.left_child is not None:
                return self._internal_insert(root.left_child, data)
            else:
                self.count += 1
                root.left_child = Node(data)
                return True
        else:
            if root.right_child is not None:
                return self._internal_insert(root.right_child, data)
            else:
                self.count += 1
                root.right_child = Node(data)
                return True


    def delete(self, data):
        if self.root is None:
            print("The Tree is empty!")
            return False
        return self._internal_delete(self.root, data)

    def _internal_delete(self, root, data):
        if root is None:
            print("There are no data what you want to delete!")
            return False

        if root.data > data:
            self._internal_delete(root.left_child, data)
        elif root.data < data:
            self._internal_delete(root.right.child, data)
        else:
            if root.data is data:
                if (root.left_child is None) and (root.right_child is None): # Leaf Node
                    root = None
                    print("Data ", data, " is successfully deleted")
                    return True
                elif (root.left_child is not None) and (root.right_child is not None): # if has two children
                    self._replace_Node(root, self._LeftMostNode(root.right_child))
                elif (root.left_child is not None) and (root.right_child is None): # if has a left child
                    self._replace_Node(root, root.left_child)
                else:
                    self._replace_Node(root, root.right_child)
                return True
            elif root.data > data:
                return self._internal_delete(root.left, data)
            else:
                return self._internal_delete(root.right, data)

            return False

                
    def _LeftMostNode(self, root):
        while root.left_child is not None:
            root = root.left_child
        return root

    def _replace_Node(self, replace, new):
        if (replace is None) or (new is None):
            return False

        if (replace.left_child is not None) and (replace.right_child is not None):
            new.left_child = replace.left_child
            if replace.right_child is not new:
                new.right_child = replace.right_child
        replace = new


    def BSTSize(self):
        return self.count

    def is_empty(self):
        return self.root is None


