#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 02:33:42 2023

@author: ram
"""

singers=[]
ranges=[]

n=input()
n=int(n)
if n <= 0:
    print("Enter a value greater than 0")



for i in range(0,n):
    s=input()
    limits=[eval(i) for i in s.split()]
    ranges=[(limits[1]-limits[0])]
    ranges.append(i)
    singers.append(ranges)


def partition(arr,lower,upper):
    #pivot index is always 0
    p_idx = lower+1
    for i in range(lower+1,upper):
        if arr[i][0] <= arr[lower][0]:
            arr[p_idx],arr[i]=arr[i],arr[p_idx]
            p_idx += 1
    arr[p_idx-1],arr[lower]=arr[lower],arr[p_idx-1]
    return p_idx

# Partition strategy: both pointers moving in same direction
def quick_sort(arr,lower,upper):
    if upper-lower <= 1:
        return arr
    
    p_idx=partition(arr,lower,upper)
    quick_sort(arr,lower,p_idx)
    quick_sort(arr,p_idx,upper)

# print(singers)
# n=5
# singers=[[23-3,0],[20-4,1],[16-11,2],[19-5,3],[25-1,4]]


arr_out=[None]*n

# def insertion_sort(arr):
#     for i in range(0, len(arr)):
#         for j in range(i,0,-1):
#             if arr[j][0] < arr[j-1][0]:
#                 arr[j-1],arr[j]=arr[j],arr[j-1]

quick_sort(singers,0,len(singers)) 

for i in range(0,len(singers)):
    arr_out[singers[i][1]] = i

for i in range(0,len(arr_out)):
    print(arr_out[i]*2, end=" ")