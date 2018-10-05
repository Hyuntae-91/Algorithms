#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Data_Structure.Queue import *

Q = Queue.Queue()
for i in range(1, 11):
    Q.enqueue(i)
print("Queue Size : ", Q.Qsize())
print("Dequeue : ", Q.dequeue())
print("Queue Size : ", Q.Qsize())

print("Is Empty? ", Q.is_empty())

print("Dequeue : ", Q.dequeue())
print("Queue peek : ", Q.Qpeek())
print("Dequeue : ", Q.dequeue())
print("Dequeue : ", Q.dequeue())

print("Queue Size : ", Q.Qsize())


