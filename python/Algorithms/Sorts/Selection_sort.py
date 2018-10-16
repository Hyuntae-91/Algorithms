#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Selection_sort(_list):
    list_length = len(_list)

    for i in range(list_length - 1):
        min = i
        for j in range(i+1, list_length):
            if _list[min] > _list[j]:
                min = j
        if min is not i:
            _list[min], _list[i] = _list[i], _list[min]

    return _list
