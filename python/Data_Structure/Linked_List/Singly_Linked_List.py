#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def init(self):
        self.head = None
        self.tail = None
        self.count = 0 
    def list_add(self, data):
        newNode = Node(self, data) # Create New Node to add
        if head == None: # if head Node is empty
            self.head = newNode # Set head pointer to New Node
            self.tail = newNode 
        else:
            self.tail = newNode # Set tail pointer to New Node
        self.count += 1 # Increase size by 1
    def list_remove(self, data):
        pointer = self.head # set pointer as head
        if pointer == None:
            return "List is Empty"# if list is empty, return
        while pointer.next is not None: # Follow next pointer until end of list
            if pointer.next.data == data: # if next Node's data is same with data which want to delete
                pointer.next = pointer.next.next # point current Node's next pointer to next next Node
                return "Remove successfully"
            pointer = pointer.next # Keep search next datas
        if pointer.next == None: # It means, there are no data which want to delete
            return "There are No data"
    def list_size(self):
        return self.count
    def is_empty(self):
        return Head is None # Return True or False
