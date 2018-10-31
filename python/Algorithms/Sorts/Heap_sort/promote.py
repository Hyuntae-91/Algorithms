#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def promote(_list, hStop, vacant, h, size):
    if h <= hStop:
        vacStop = vacant
    elif vacant * 2 + 1 >= size:
        vacStop = -1
    else:
        if _list[2 * vacant + 1] <= _list[2 * vacant + 2]:
            _list[vacant] = _list[2 * vacant + 2]
            vacStop = promote(_list, hStop, 2 * vacant + 2, h - 1, size)
        else:
            _list[vacant] = _list[2 * vacant + 1]
            vacStop = promote(_list, hStop, 2 * vacant + 1, h - 1, size)
    return vacStop

