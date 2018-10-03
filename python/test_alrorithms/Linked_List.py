#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Data_Structure.Linked_List import *

print("** Singly Linked List **")
list1 = Singly_Linked_List.Singly_Linked_List()
for i in range(1, 11):
    list1.list_add(i)

print("-- Added 10 data at the list --")
list1.list_size()
list1.list_remove(5)
list1.list_size()
list1.list_print()

print("\n** Doubly Linked List **")
list2 = Doubly_Linked_List.Doubly_Linked_List()
print("-- Added 20 data at the list --")
for i in range(1, 21):
    list2.list_add(i)

list2.list_size()
list2.list_remove(15)
list2.list_size()
list2.list_print()
