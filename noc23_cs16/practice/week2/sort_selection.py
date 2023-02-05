#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 14:36:01 2023

@author: ram
"""

arr=[1,3,2,1,2,3]

def swap(arr, i,j):
    arr[i],arr[j]=arr[j],arr[i]

def selection_sort_iterative():
    maxpos=len(arr)
    iteration=0
    
    for startpos in range(0, maxpos):
        minpos=startpos
        iteration += 1
        for i in range(startpos,maxpos):
            if arr[i] < arr[minpos]:
                minpos=i

        swap(arr,minpos,startpos)
        
        print("at the end of the iteration",iteration," min value",arr[startpos])

def selection_sort_recursive(arr, startpos, maxpos):
    if maxpos - startpos <= 1:
        return
    minpos=startpos
    for i in range(startpos,maxpos):
        if arr[i] < arr[minpos]:
            minpos=i
            
    swap(arr, minpos,startpos)
    
    selection_sort_recursive(arr,startpos+1,maxpos)
    
# This function doesn't work since splicing an arry creates a new object in memory
def selection_sort_recursive2(arr):
    print("start:",arr)
    startpos=0
    maxpos=len(arr)
    if maxpos <= 1:
        print("return x",arr)
        return;
    minpos=startpos
    for i in range(startpos,maxpos):
        if arr[i] < arr[minpos]:
            minpos=i

    swap(arr, minpos,startpos)
    
    print("after swap: ",arr)
    
    selection_sort_recursive2(arr[1:])

    print("return ",arr)


selection_sort_recursive(arr,0,len(arr))
#selection_sort_recursive2(arr)

print("after sort",arr)