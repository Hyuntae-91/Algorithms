#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Algorithms.Sorts import *
from Algorithms.Sorts.Heap_sort import *

li = [2, 0, 10, 22, 11, 23, 5, 9, 14, 19]

copied_li = li[:]
print("")
print("== Bubble Sorts ==")
print(Bubble_sort.Bubble_sort(copied_li))
print("==================")



copied_li = li[:]
print("")
print("")
print("== Selection Sorts ==")
print(Selection_sort.Selection_sort(copied_li))
print("==================")


copied_li = li[:]
print("")
print("")
print("== Insertion Sorts ==")
print(Insertion_sort.Insertion_sort(copied_li))
print("==================")


copied_li = li[:]
print("")
print("")
print("== Quick Sorts ==")
print(Quick_sort.Quick_sort(copied_li))
print("==================")


copied_li = li[:]
print("")
print("")
print("== Merge Sorts ==")
print(Merge_sort.Merge_sort(copied_li))
print("==================")


copied_li = li[:]
print("")
print("")
print("== Heap Sorts ==")
print(Heap_sort.Heap_sort(copied_li))
print("==================")


copied_li = li[:]
print("")
print("")
print("== Acceleated Heap Sorts ==")
print(Acceleated_Heap_sort.Acceleated_Heap_sort(copied_li))
print("==================")
