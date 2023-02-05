#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:59:36 2023

@author: ram

Array slicing creates a new array in memory
"""

arr=[1,3,4,2]
arr2=arr

def printarr(arr):
    print("id of array",id(arr)," array:",arr)

arr2[0]=10

arr3=arr[1:]

printarr(arr)    
printarr(arr2)    
printarr(arr3)
