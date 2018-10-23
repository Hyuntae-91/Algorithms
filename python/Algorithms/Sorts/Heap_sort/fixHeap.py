#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fixHeap(_list, root, key, size):
    if 2*root + 1 >= size: # if root node is leaf node
        _list[root] = key
    else:
        LargerSubHeap = 2*root + 1
        if (size > 2*root + 2) and (_list[2*root+1] < _list[2*root+2]): 
            LargerSubHeap = 2*root + 2 # if exist right subtree and if that is larger than left subtree
                                       # Change LagerSubHeap to right subtree

        if key >= _list[LargerSubHeap]:
            _list[root] = key
        else:
            _list[root] = _list[LargerSubHeap]
            fixHeap(_list, LargerSubHeap, key, size)

