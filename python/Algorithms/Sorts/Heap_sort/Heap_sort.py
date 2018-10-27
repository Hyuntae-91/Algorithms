#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .fixHeap import fixHeap
from .Construct_heap import Construct_heap

def Heap_sort(_list):
    list_size = len(_list) - 1
    Construct_heap(_list, 0, list_size)

    for i in range(list_size, 0, -1):
        curMax = _list[0]
        key = _list[i]
        fixHeap(_list, 0, key, i)
        _list[i] = curMax

    return _list
