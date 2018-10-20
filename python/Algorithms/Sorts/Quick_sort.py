#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def qs_swap(_list, l, r):
    _list[l], _list[r] = _list[r], _list[l]

def Quick_sort(_list):
    if len(_list) <= 1:
        return _list

    p = Partition(_list)
    left = _list[:p]
    right = _list[p:]
    return Quick_sort(left) + Quick_sort(right)

def Partition(_list):
    pivot = int((len(_list)) / 2)
    left = 0 
    right = len(_list) - 1
    qs_swap(_list, pivot, right)
    pivot = right

    while left < right:
        while (_list[left] < _list[pivot]) and (left < right):
            left += 1
        while (_list[right] >= _list[pivot]) and (left < right):
            right -= 1

        if left < right:
            qs_swap(_list, left, right)
            left += 1
            right -= 1


    if _list[pivot] < _list[right]:
        qs_swap(_list, pivot, right)

    return left 
