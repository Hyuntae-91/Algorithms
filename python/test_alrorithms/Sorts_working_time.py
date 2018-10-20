#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import random

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Algorithms.Sorts import *

li = []
LIST_SIZE = 10000           
NUM_SCOPE = 100000          
rand_num = random.randint(0, NUM_SCOPE)

for i in range(LIST_SIZE):              
    while rand_num in li:
        rand_num = random.randint(0, NUM_SCOPE)

    li.append(rand_num)


copied_li = li[:]
start_time = time.time()
print("")
print("== Bubble Sorts ==")
Bubble_sort.Bubble_sort(copied_li)
print("--- %.7s Seconds ---" % (time.time() - start_time))


copied_li = li[:]
print("")
print("")
start_time = time.time()
print("== Selection Sorts ==")
Selection_sort.Selection_sort(copied_li)
print("--- %.7s Seconds ---" % (time.time() - start_time))


copied_li = li[:]
print("")
print("")
start_time = time.time()
print("== Insertion Sorts ==")
Insertion_sort.Insertion_sort(copied_li)
print("--- %.7s Seconds ---" % (time.time() - start_time))


copied_li = li[:]
print("")
print("")
start_time = time.time()
print("== Quick Sorts ==")
Quick_sort.Quick_sort(copied_li)
print("--- %.7s Seconds ---" % (time.time() - start_time))


copied_li = li[:]
print("")
print("")
start_time = time.time()
print("== Merge Sorts ==")
Merge_sort.Merge_sort(copied_li)
print("--- %.7s Seconds ---" % (time.time() - start_time))
