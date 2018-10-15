#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function

class Node:
    left_child = None
    right_child = None
    def __init__(self, data):
        self.data = data

class Binary_Search_Tree:
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

    def _internal_delete(self, cnode, data):
        if cnode.data is data:
            if (cnode.left_child is None) and (cnode.right_child is None): # Leaf Node
                cnode = None
                print("Data ", data, " is successfully deleted")
                return True
            elif (cnode.left_child is not None) and (cnode.right_child is not None): # if has two children
                self._replace_node(cnode, cnode.right_child, data)
            elif (cnode.left_child is not None) and (cnode.right_child is None): # if has a left child
                self._replace_node(cnode, cnode.left_child, data)
            else:                                                                   # if has a right child
                self._replace_node(cnode, right_child, data)
        elif cnode.data > data:
            self._internal_delete(cnode.left_child, data)
        else:
            self._internal_delete(cnode.right_child, data)


    def _replace_node(self, cnode, lmost, data):                            # I think this function need refactoring
        lmost_p = cnode
        while lmost.left_child is not None:
            lmost_p = lmost
            lmost = lmost.left_child

        if cnode.right_child is lmost:
            lmost.left_child = cnode.left_child
            temp_node = self.root
            while True:
                if temp_node.left_child is cnode:
                    flag = 0
                    break
                elif temp_node.right_child is cnode:
                    flag = 1
                    break
                
                if temp_node.data > data:
                    temp_node = temp_node.left_child
                else:
                    temp_node = temp_node.right_child

            if flag is 0:
                temp_node.left_child = lmost
            else:
                temp_node.right_child = lmost
        else:
            cnode.data = lmost.data
            if lmost.right_child is None:
                lmost_p.left_child = None
            else:
                lmost_p.left_child = lmost.right_child


    def BSTSize(self):
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
