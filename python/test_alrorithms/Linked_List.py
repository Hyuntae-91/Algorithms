#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from Data_Structure.Linked_List import *

print("** Singly Linked List **")
list1 = Singly_Linked_List.Singly_Linked_List()
for i in range(1, 11):
    list1.append(i)

print("-- Added 10 data at the list --")
list1.ListSize()
list1.remove(5)
list1.ListSize()
list1.lprint()

print("\n** Doubly Linked List **")
list2 = Doubly_Linked_List.Doubly_Linked_List()
print("-- Added 20 data at the list --")
for i in range(1, 21):
    list2.append(i)

list2.ListSize()
list2.remove(15)
list2.ListSize()
list2.lprint()
