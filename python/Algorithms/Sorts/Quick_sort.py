#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Quick_sort(_list, start, end):
    if start < end:
        p = Partition(_list, start, end)
        Quick_sort(_list, start, p - 1)
        Quick_sort(_list, p + 1, end)
    return _list

def Partition(_list, start, end):
    pivot = _list[int((start + end) / 2)]
    left = start 
    right = end

    while left < right:
        while (_list[left] < pivot) and (left < right):
            left += 1
        while (_list[right] >= pivot) and (left < right):
            right -= 1

        if left < right:
            _list[left], _list[right] = _list[right], _list[left]

    pivot, _list[right] = _list[right], pivot

    return left
