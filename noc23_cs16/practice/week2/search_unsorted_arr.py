#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 11:06:23 2023

@author: ram

Unsorted array. This is amazing..!
"""

arr=[1,10,2,20,33,44]

print(arr)

def search(k, arr):
    print("k:", k)
    
    for val in arr:
        print(val)
        if (val==k):
            return True
    return False

k=input("Enter value: ")

if search(int(k),arr):
    print("Value exists!")
else:
    print("Does not exists")    