#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Merge(left_list, right_list):
    merged_list = list()

    i = 0
    j = 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] <= right_list[j]:
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1

    while i < len(left_list):
        merged_list.append(left_list[i])
        i += 1
    
    while j < len(right_list):
        merged_list.append(right_list[j])
        j += 1

    return merged_list

def Merge_sort(_list):
    if len(_list) <= 1:
        return _list

    mid = int(len(_list)//2)
    left_list = _list[:mid]
    right_list = _list[mid:]
    left_list = Merge_sort(left_list)
    right_list = Merge_sort(right_list)
    return Merge(left_list, right_list)
