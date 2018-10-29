#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Construct_heap import Construct_heap
from .fixHeapFast import fixHeapFast
import math

def Acceleated_Heap_sort(_list):
    list_size = len(_list) - 1
    Construct_heap(_list, 0, list_size)

    for i in range(list_size, 0, -1):
        curMax = _list[0]
        key = _list[i]
        fixHeapFast(_list, key, 0, int(math.log(i, 2)), i)
        _list[i] = curMax

    return _list
