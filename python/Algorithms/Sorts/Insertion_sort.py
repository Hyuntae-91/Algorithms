#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Insertion_sort(_list):
    list_length = len(_list)

    i = 1
    while i < list_length:
        key = _list[i]
        j = i - 1
        while j >= 0 and _list[j] > key:
            _list[j+1] = _list[j]
            j -= 1
        _list[j+1] = key
        i += 1

    return _list
