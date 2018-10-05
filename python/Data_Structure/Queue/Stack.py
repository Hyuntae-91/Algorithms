#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        self.count += 1
    def pop(self):
        if self.top is None:
            print("Stack is Empty!")
            return -1
        poped_data = self.top.data
        self.top = self.top.next
        self.count -= 1
        return poped_data
    def peek(self, data):
        if self.top is None:
            print("Stack is Empty!")
            return -1
        return self.top.data
    def StackSize(self):
        return self.count
    def is_empty(self):
        return self.top is None

