#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bubbleUpHeap(_list, root, key, vacant):
    if vacant is root:
        _list[vacant] = key
    else:
        parent = int(vacant / 2) - 1
        if key <= _list[parent]:
            _list[vacant] = key
        else:
            _list[vacant] = _list[parent]
            bubbleUpHeap(_list, root, key, parent)
