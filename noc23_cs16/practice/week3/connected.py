#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:45:05 2023

@author: ram

Connected components
"""

# Find out how many connected components are there in the below graph.

graph={
       1:[2,5],
       2:[1],
       5:[1,9,10],
       9:[5,10],
       10:[5,9],
       6:[],
       3:[4,7,8],
       4:[3],
       7:[3],
       8:[3]
      }


stack=[]
visited=[]

path=[]
connected=[]

for k,v in graph.items():
    stack.append(k)


def dfs(G,v):
    visited.append(v)
    path.append(v)
    for neighbour in G[v]:
        if neighbour not in visited:
            dfs(G,neighbour)

while stack:
    path=[]
    v=stack.pop(0)
    if v not in visited:
        dfs(graph,v)
        connected.append(path)

