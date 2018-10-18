#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Quick_sort(_list, first, last):
    if first < last:
        p = Partition(_list, first, last)
        Quick_sort(_list, first, p - 1)
        Quick_sort(_list, p + 1, last)
    return _list

def Partition(_list, first, last):
    pivot = _list[int((first + last) / 2)]
    left = first 
    right = last

    while left < right:
        while (_list[left] < pivot) and (left < right):
            left += 1
        while (_list[right] >= pivot) and (left < right):
            right -= 1

        if left < right:
            _list[left], _list[right] = _list[right], _list[left]

    pivot, _list[right] = _list[right], pivot

    return left
