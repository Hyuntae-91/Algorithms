#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def Bubble_sort(unsorted_list):
    list_length = len(unsorted_list)
    new_list = unsorted_list

    for i in range(list_length - 1):
        for j in range(1, list_length):
            if new_list[j-1] > new_list[j]:
                new_list[j - 1], new_list[j] = new_list[j], new_list[j - 1]

    return new_list
