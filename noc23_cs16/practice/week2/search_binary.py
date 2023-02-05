#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 11:06:23 2023

@author: ram

Unsorted array. This is amazing..!
"""

arr=[1,3,2]

arr.sort() 

print(arr)

def search(k, arr):
    if len(arr) == 0:
        return False
    
    print('Iter...')
    print(arr)
    
    mid=len(arr)//2
    
    print("mid:",mid,"value:",arr[mid]," k:",k)

    if arr[mid]==k:
        return True
    elif mid==0:
        return False
    elif k < arr[mid] :
        return search(k,arr[0:mid])
    else:
        return search(k,arr[mid:])    


#k=input("Enter value: ")
k=1

if search(int(k),arr):
    print("Value exists!")
else:
    print("Does not exists")    