#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Data_Structure.Binary_Search_Tree import *

bst1 = Binary_Search_Tree.Binary_Search_Tree()

bst1.insert(10)
bst1.insert(5)
bst1.insert(3)
bst1.insert(1)
bst1.insert(7)
bst1.insert(6)
bst1.insert(15)
bst1.insert(11)
bst1.insert(20)
bst1.insert(21)

print("======================")
bst1.preorder()
bst1.inorder()
bst1.postorder()
print("")
print("======================")


bst1.delete(5)
bst1.delete(15)
print("Deleted data 5 and 15")
print("======================")

print("")
print("======================")
bst1.preorder()
bst1.inorder()
bst1.postorder()
print("======================")
print("")

bst1.insert(15)
bst1.insert(10)
print("Try to insert 10 and 15. (10 is duplicated)")
bst1.delete(10)
print("deleted data 10")
print("")
print("======================")
bst1.preorder()
bst1.inorder()
bst1.postorder()
print("======================")
