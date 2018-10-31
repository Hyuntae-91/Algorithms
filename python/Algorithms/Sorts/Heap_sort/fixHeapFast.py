#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .promote import promote
from .bubbleUpHeap import bubbleUpHeap

def fixHeapFast(_list, key, vacant, h, size):
    if h <= 0:
        _list[vacant] = key
    else:
        hStop = int(h/2)
        vacStop = promote(_list, hStop, vacant, h, size)

        if vacStop is -1:
            _list[vacant] = key
            return

        vacParent = int(vacStop/2) - 1
        if _list[vacParent] <= key:
            _list[vacStop] = _list[vacParent]
            bubbleUpHeap(_list, vacant, h, size)
        else:
            fixHeapFast(_list, key, vacStop, hStop, size)
