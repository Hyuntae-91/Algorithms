#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Bubble_sort(_list):
    list_length = len(_list)

    for i in range(list_length - 1):
        for j in range(1, list_length):
            if _list[j-1] > _list[j]:
                _list[j - 1], _list[j] = _list[j], _list[j - 1]

    return _list
