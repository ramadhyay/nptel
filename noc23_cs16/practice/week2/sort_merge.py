#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 21:28:27 2023

@author: ram
"""

arr=[1,3,5,10,2,2,0,1,2,3]

# A more natural and intiutive way to look at array and also saves space while merge sort
# on second thought this wont work in C because basically what we call an array here is infact a 
# list!!!. If you, ideally you need to use "array" object in python to handle this
def merge(arr1,arr2):
    arr=[]
    
    while (arr1 != [] or arr2 != []):
        if arr1==[] and arr2 != []:
            arr.append(arr2.pop(0))
        
        if arr2==[] and arr1 != []:
            arr.append(arr1.pop(0))


        if arr1 != [] and arr2 != []:
            if arr1[0] <= arr2[0]:
                arr.append(arr1.pop(0))
            else:
                arr.append(arr2.pop(0))    


    return arr

# Using indices... painful... but translates to c language. 
# If some is evaluating then this is the the way
def merge2(arr1,arr2):
    arr=[]
    
    i=0
    j=0
    
    while ( i < len(arr1) or j < len(arr2) ):
        print("1: i",i,"j",j)

        if (j==len(arr2)) or (i < len(arr1) and arr1[i] <= arr2[j]):
            arr.append(arr1[i])
            i += 1
        
        print("2: i",i,"j",j)

        if (i==len(arr1)) or (j < len(arr2) and arr1[i] > arr2[j]):
            arr.append(arr2[j])
            j += 1
        
        print("3: i",i,"j",j)
        print("\n")
        
    return arr


# Perform merge sort...!
def merge_sort(arr):
    
    # Base condition t(1) = 1
    if len(arr)==1:
        return arr
    
    # Recurrence
    mid=len(arr)//2
    
    leftarr=merge_sort(arr[0:mid])
    rightarr=merge_sort(arr[mid:])
    
    return merge(leftarr,rightarr)


print(arr)
arr=merge_sort(arr)
print(arr)