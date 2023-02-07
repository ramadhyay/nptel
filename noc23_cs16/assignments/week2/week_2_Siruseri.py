#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 02:33:42 2023

@author: ram
"""
n=input()
n=int(n)

singers=[]
ranges=[]
if n <= 0:
    print("Enter a value greater than 0")
    
for i in range(0,n):
    s=input()
    limits=[eval(i) for i in s.split()]
    ranges=[(limits[1]-limits[0])]
    ranges.append(i)
    singers.append(ranges)

# print(singers)
# n=5
# singers=[[23-3,0],[20-4,1],[16-11,2],[19-5,3],[25-1,4]]
singers_copy = singers.copy()
def insertion_sort(arr):
    for i in range(0, len(arr)):
        for j in range(i,0,-1):
            if arr[j][0] < arr[j-1][0]:
                arr[j-1],arr[j]=arr[j],arr[j-1]
            else:
                break

insertion_sort(singers)

# print(singers)

for i in range(0,n):
    for j in range(0,n):
        if i == singers[j][1]:
            print(j*2, end=" ")
print("\n")            

