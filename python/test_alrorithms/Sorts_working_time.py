#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import random

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Algorithms.Sorts import *

li = []
SIZE = 10000                    # create SIZE of random integer list for checking working time
rand_num = random.randint(0, SIZE)

for i in range(SIZE):              
    while rand_num in li:
        rand_num = random.randint(0, SIZE)

    li.append(rand_num)



start_time = time.time()
print("")
print("== Bubble Sorts ==")
Bubble_sort.Bubble_sort(li)
print("--- %.7s Seconds ---" % (time.time() - start_time))


print("")
print("")
start_time = time.time()
print("== Selection Sorts ==")
Selection_sort.Selection_sort(li)
print("--- %.7s Seconds ---" % (time.time() - start_time))


print("")
print("")
start_time = time.time()
print("== Insertion Sorts ==")
Insertion_sort.Insertion_sort(li)
print("--- %.7s Seconds ---" % (time.time() - start_time))


print("")
print("")
start_time = time.time()
print("== Quick Sorts ==")
Quick_sort.Quick_sort(li)
print("--- %.7s Seconds ---" % (time.time() - start_time))


print("")
print("")
start_time = time.time()
print("== Merge Sorts ==")
Merge_sort.Merge_sort(li)
print("--- %.7s Seconds ---" % (time.time() - start_time))
