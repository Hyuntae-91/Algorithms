#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    next = None
    def __init__(self, data):
        self.data = data

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top 
        self.top = newNode # Set NewNode as a top
        self.count += 1

    def pop(self):
        if self.is_empty():
            print("Stack is Empty!")
            return -1
        poped_data = self.top.data # save data on top at poped_data
        self.top = self.top.next # change top node
        self.count -= 1
        return poped_data

    def peek(self):
        if self.is_empty():
            print("Stack is Empty!")
            return -1
        return self.top.data

    def StackSize(self):
        return self.count

    def is_empty(self):
        return self.top is None

