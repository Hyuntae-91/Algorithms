#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Linked_List import *

list1 = Singly_Linked_List.Singly_Linked_List()
for i in range(1, 11):
    list1.list_add(i)

list1.list_size()
list1.list_remove(5)
list1.list_size()
list1.list_print()

list2 = Doubly_Linked_List.Doubly_Linked_List()
for i in range(1, 20):
    list2.list_add(i)

list2.list_size()
list2.list_remove(15)
list2.list_size()
list2.list_print()
