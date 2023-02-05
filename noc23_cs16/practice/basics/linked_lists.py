#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 09:43:46 2023

@author: ram
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

last_node=None
linked_list=None

def addNode(node):
    global last_node
    global linked_list
    if (linked_list==None):
        linked_list=node
        last_node=linked_list
    else:
        last_node.next=node
        last_node=node
    

addNode(Node('node 0(root)'))
addNode(Node('node 1'))
addNode(Node('node 2'))

curr_node=linked_list

while (curr_node != None):
    print(curr_node.data)
    curr_node=curr_node.next