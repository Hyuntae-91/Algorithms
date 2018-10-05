#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Data_Structure.Stack import *

st1 = Stack.Stack()
for i in range(1, 11):
    st1.push(i)
print("Stack Size : ", st1.StackSize())
print("pop : ", st1.pop())
print("Stack Size : ", st1.StackSize())

print("Is Empty? ", st1.is_empty())

print("pop : ", st1.pop())
print("Stack Peek : ", st1.peek())
print("pop : ", st1.pop())
print("pop : ", st1.pop())

print("Stack Size : ", st1.StackSize())
