#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:47:20 2023

@author: ram
"""

class PriorityQueue:
    def __init__(self):
        self.value=None
        self.next=None
        self.root=None
    
    def add(self,value):
        if self.value==None:
            self.value=value
            return
        
        new=PriorityQueue()
        new.add(value)

        curr=self
        prev=None
        while curr:
            if value < curr.value:
                new.next=curr
                if prev:
                    prev.next=new
                return
            prev=curr
            curr=curr.next
        prev.next=new
        
        self.root=self
        self.value=self.root.value
        self.next=self.root.next

    def print(self):
        node=self
        while node:
            print(node.value, end=" ")
            node=node.next
        print("\r")

    def queue(self):
        node=self
        queue_list=[]
        while node:
            queue_list.append(node.value)
            node=node.next
        return queue_list

    def peek(self):
        value = self.value

        self.root=self.next
        self.value=self.root.value
        self.next=self.root.next

        return value

queue=PriorityQueue()    
queue.add(10)
queue.add(20)
queue.add(15)
queue.add(20)
queue.add(30)
