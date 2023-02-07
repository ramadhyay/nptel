#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 23:23:08 2023

@author: ram
"""
arr=[5, 2, 3, 4, 7, 9, 1,-1,-22]


def partition_basic(arr,lower,upper):
    #pivot index is always 0
    p_idx = lower+1
    for i in range(lower+1,upper):
        if arr[i] <= arr[lower]:
            arr[p_idx],arr[i]=arr[i],arr[p_idx]
            p_idx += 1
    arr[p_idx-1],arr[lower]=arr[lower],arr[p_idx-1]
    print(p_idx)
    return p_idx

def partition_hoare(arr,lower,upper):
    #pivot index is always 0

    pivot=lower
    p_idx = lower+1
    p_u_idx = upper-1
    for i in range(lower+1,upper):
        if arr[p_idx] <= arr[pivot]:
            p_idx += 1
        elif arr[p_u_idx] > arr[pivot]:
            p_u_idx -= 1
        else:
            arr[p_idx],arr[p_u_idx]=arr[p_u_idx],arr[p_idx]
            p_u_idx -= 1

    arr[pivot],arr[p_u_idx] = arr[p_u_idx],arr[pivot]

    return p_idx
    #print(arr,p_idx, p_u_idx)

# Partition strategy: both pointers moving in same direction
def quick_sort(arr,lower,upper):
    if upper-lower <= 1:
        return arr
    
    p_idx=partition_basic(arr,lower,upper)
    quick_sort(arr,lower,p_idx)
    quick_sort(arr,p_idx,upper)


def quick_sort_hoare(arr,lower,upper):
    if upper-lower <= 1:
        return arr
    
    p_idx=partition_basic(arr,lower,upper)
    quick_sort(arr,lower,p_idx)
    quick_sort(arr,p_idx,upper)

quick_sort_hoare(arr,0,len(arr)) 

#quick_sort(arr,0,len(arr)) 




print(arr)