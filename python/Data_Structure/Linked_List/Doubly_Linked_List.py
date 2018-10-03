#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Doubly_Linked_List:
    def __init__(self):
        self.head = Node(None) # dummy node
        self.tail = Node(None) # dummy node
        self.head.next = self.tail
        self.count = 0
    def list_add(self, data):
        newNode = Node(data) # Create New Node to add
        pointer = self.head
        while pointer.next is not self.tail:
            pointer = pointer.next
        pointer.next = newNode # Set tail's next node to New Node
        newNode.prev = pointer # Set newNode's previous node to end data of the list
        newNode.next = self.tail
        self.tail.prev = newNode
        self.count += 1 # Increase size by 1
    def list_remove(self, data):
        pointer = self.head # set pointer as head
        if self.head.next == self.tail:
            print("List is Empty") # if list is empty, print this message, and return
            return
        while pointer.next is not self.tail: # Follow next pointer until end of list
            if pointer.next.data == data: # if next Node's data is same with data which want to delete
                temp = pointer.next
                pointer.next = temp.next # point current Node's next pointer to next next Node
                temp.next.prev = pointer # set temp's previous node to pointer
                print("Remove", data, " successfully")
                self.count -= 1
                return 
            pointer = pointer.next # Keep search next datas
        if pointer.next == self.tail: # It means, there are no data which want to delete
            print("There are No matched data")
            return 
    def list_print(self):
        pointer = self.head
        print("List data : ", end='')
        while pointer.next is not self.tail:
            pointer = pointer.next
            print(pointer.data, end=' ')
        print("")
    def list_size(self):
        print("Total List Size : ", self.count)
        return 
    def is_empty(self):
        return self.head.next is self.tail # Return True or False

