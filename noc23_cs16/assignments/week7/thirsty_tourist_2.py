#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 15:09:43 2023

@author: ram
"""


# Testing
H=400
N=4
C=200
dist=[0,100,150,300]
cost=[1000,1300,1200,1100]


# H, N, C = map(int, input().split())

# shops = [(0, 0)]  # starting point
# for _ in range(N):
#     dist, cost = map(int, input().split())
#     shops.append((dist, cost))

shops=[[0.0]]

for i in range(len(dist)):
    shops.append([dist[i],cost[i]])

# initialize mincost array
mincost = [[float('inf')] * (C+1) for _ in range(N+1)]
mincost[N][0] = 0  # base case

# dynamic programming
for i in range(N-1, -1, -1):
    for j in range(C+1):
        # case 1: buy water at current shop
        k = j
        cost = 0
        while k <= C and shops[i+1][0] - shops[i][0] > k - j:
            cost += shops[i+1][1] * (k-j+1)
            k += 1
        if k <= C:
            cost += mincost[i+1][k]
        mincost[i][j] = min(mincost[i][j], cost)

        # case 2: don't buy water at current shop
        if j < C:
            mincost[i][j] = min(mincost[i][j], mincost[i+1][j+1])

print(mincost[1][C])