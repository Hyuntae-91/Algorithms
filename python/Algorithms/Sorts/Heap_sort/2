#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .promote import promote
from .bubbleUpHeap import bubbleUpHeap

def fixHeapFast(_list, key, vacant, h, size):
    if h < 0:
        _list[vacat] = key
    else:
        hStop = int(h/2)
        vacStop = promote(_list, hStop, vacant, h)
        vacParent = int(vacStop/2)
        if _list[vacParent] <= key:
            _list[vacStop] = _list[vacParent]
            bubbleUpHeap(_list, vacant, h, size)
        else:
            fixHeapFast(_list, key, vacant, h, size)
