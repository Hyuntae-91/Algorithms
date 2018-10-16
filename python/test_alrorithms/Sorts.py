#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Algorithms.Sorts import *

li = [2, 0, 10, 22, 11, 23, 5, 9, 14, 19]
print("")
print("== Bubble Sorts ==")
print(Bubble_sort.Bubble_sort(li))
print("==================")
print("")
print("")


print("== Selection Sorts ==")
print(Selection_sort.Selection_sort(li))
print("==================")
print("")
print("")
print("== Insertion Sorts ==")
print(Insertion_sort.Insertion_sort(li))
print("==================")
