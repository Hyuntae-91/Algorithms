#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self):
        self.data = -1
        self.next = None

class Queue:
    def __init__(self):
        self.front = node(None) # Dummy node
        self.rear = None 
        self.front.next = self.rear # connect front to rear 
        self.count = 0
    
    def enqueue(self, data):
        newNode = Node(data) # create New Node
        pointer = self.front
        while pointer.next is not self.rear: # find rear location to put in the data
            pointer = pointer.next
        newNode.next = self.rear
        pointer.next = newNode
        self.count += 1

    def dequque(self, data):
        if self.front.next is self.rear: # check the queue is empty
            print("Queue is Empty!")
            return -1
        pointer = self.front.next
        dequeued_data = pointer.data
        pointer = pointer.next
        self.count -= 1
        return dequeued_data

    def Qpeek(self):
        if self.front.next is self.rear:
            print("Queue is Empty!")
            return -1
        return self.front.next.data

    def Qsize(self):
        return self.count

    def is_empty(self):
        return self.front.next is self.rear

