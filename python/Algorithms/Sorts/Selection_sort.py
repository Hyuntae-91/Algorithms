#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Selection_sort(unsorted_list):
    list_length = len(unsorted_list)
    new_list = unsorted_list

    for i in range(list_length - 1):
        min = i
        for j in range(i+1, list_length):
            if new_list[min] > new_list[j]:
                min = j
        if min is not i:
            new_list[min], new_list[i] = new_list[i], new_list[min]

    return new_list
