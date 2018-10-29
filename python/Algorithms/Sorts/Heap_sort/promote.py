#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def promote(_list, hStop, vacant, h):
    if h <= hStop:
        vacStop = vacant
    elif _list[2 * vacant + 1] <= _list[2 * vacant + 2]:
        _list[vacant] = _list[2 * vacant + 2]
        vacStop = promote(_list, hStop, 2 * vacant + 2, h - 1)
    else:
        _list[vacant] = _list[2 * vacant + 1]
        vacStop = promote(_list, hStop, 2 * vacant + 1, h - 1)
    return vacStop

