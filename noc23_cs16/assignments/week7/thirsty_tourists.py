#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 18:43:27 2023

@author: ram
"""
inputs=input()
hnc=[eval(i) for i in inputs.split()]

h=hnc[0]    # Total # of hours
n=hnc[1]    # No. of shops
c=hnc[2]    # Carrying capacity in litres

dist=[]     # Distance of a shop i from starting point
cost=[]     # Price per litre at shop i

for i in range(0,n):
    inputs=input()
    input_arr=[eval(i) for i in inputs.split()]
    dist.append(input_arr[0])
    cost.append(input_arr[1])


# Testing
# h=400
# n=4
# c=200
# dist=[0,100,150,300]
# cost=[1000,1300,1200,1100]

maxcost=0
for i in range(0,n):
    maxcost = max(maxcost,cost[i])

maxcost=h*maxcost

# mincost=[]
# for i in range(0,n+1):
#     mincost.append([])
#     for j in range(0,c+1):
#         mincost[i].append(maxcost+1)

mincost=[ [maxcost for j in range(0,c+1)] for i in range(0,n+1) ]



for j in range(0,c+1):
    mincost[0][j]=j*cost[0]
    
for i in range(1,n):
    for j in range(0,c+1):
        if(j + dist[i] - dist[i - 1] <= c):
            mincost[i][j] = min(mincost[i - 1][j + (dist[i] - dist[i - 1])], mincost[i - 1][dist[i] - dist[i - 1]] + j * cost[i])
        else:
            mincost[i][j] = min(mincost[i][j], mincost[i - 1][dist[i] - dist[i - 1]] + j * cost[i])

        if j > 0:
            mincost[i][j] = min(mincost[i][j], mincost[i][j - 1] + cost[i])

print(mincost[n - 1][h - dist[n - 1]])