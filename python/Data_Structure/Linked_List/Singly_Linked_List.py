#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None

class Singly_Linked_List:
    head = None
    tail = None
    count = 0
    def init(self):
        self.head = None
        self.tail = None
    def list_add(self, data):
        newNode = Node(data) # Create New Node to add
        if self.head == None: # if head Node is empty
            self.head = newNode # Set head pointer to New Node
            self.tail = newNode 
        else:
            self.tail = newNode # Set tail pointer to New Node
        self.count += 1 # Increase size by 1
    def list_remove(self, data):
        pointer = self.head # set pointer as head
        if pointer == None:
            print("List is Empty") # if list is empty, print this message, and return
            return
        while pointer.next is not None: # Follow next pointer until end of list
            if pointer.next.data == data: # if next Node's data is same with data which want to delete
                pointer.next = pointer.next.next # point current Node's next pointer to next next Node
                print("Remove successfully")
                return 
            pointer = pointer.next # Keep search next datas
        if pointer.next == None: # It means, there are no data which want to delete
            print("There are No data")
            return 
    def list_size(self):
        print(self.count)
        return 
    def is_empty(self):
        return Head is None # Return True or False

