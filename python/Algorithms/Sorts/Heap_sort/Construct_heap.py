#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .fixHeap import fixHeap

def Construct_heap(_list, root, size):
    if root*2 + 1 <= size:
        Construct_heap(_list, 2*root + 1, size) # left
        Construct_heap(_list, 2*root + 2, size) # right
        key = _list[root]
        fixHeap(_list, root, key, size)
