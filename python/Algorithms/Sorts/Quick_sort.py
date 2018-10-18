#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Quick_sort(_list):
    if len(_list) <= 1:
        return _list

    mid = Partition(_list)
    left = _list[:mid]
    right = _list[mid:]
    left = Quick_sort(left)
    right = Quick_sort(right)
    return left + right

def Partition(_list):
    pivot = _list[int((len(_list)) / 2)]
    left = 0 
    right = len(_list) - 1

    while left < right:
        while (_list[left] < pivot) and (left < right):
            left += 1
        while (_list[right] >= pivot) and (left < right):
            right -= 1

        if left < right:
            _list[left], _list[right] = _list[right], _list[left]

    pivot, _list[right] = _list[right], pivot

    return left
