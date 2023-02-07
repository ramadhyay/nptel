#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 19:26:22 2023

@author: ram
"""

arr=[1,1,1,1,10,2,3,1,5,6,1,1,1]
print(arr)

def swap(arr, i,j):
    arr[i],arr[j]=arr[j],arr[i]

def insertion_sort_iter(arr):
    for i in range(0, len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                break

# Insertion sort recursive
# Insert value at 'pos' into array arr which is sotred 'before' poisition pos
def insert(arr,pos):
    for j in range(pos,0,-1):
        if arr[j] < arr[j-1]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
        

def insertion_sort_recur(arr,pos):
    if pos==len(arr):
        return

    insert(arr,pos)    
    insertion_sort_recur(arr,pos+1)

#insertion_sort_iter(arr)
insertion_sort_recur(arr,0)

print(arr)