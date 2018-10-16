#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Insertion_sort(_list):
    list_length = len(_list)

    i = 1
    while i < list_length:
        j = i
        while j > 0 and _list[j-1] > _list[j]:
            _list[j-1], _list[j] = _list[j], _list[j-1]
            j -= 1
        i += 1

    return _list
