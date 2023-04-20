#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 22:00:44 2023

@author: ram
"""
graph={
       1:[2,3,4],
       2:[1,3],
       3:[2,1],
       4:[5,8],
       5:[4,6,7],
       6:[5,7,9,8],
       7:[5,6],
       8:[4,6,9],
       9:[6,10],
       10:[]
      }


queue=[]
visited=[]
level={}

queue.append(1) #Starting node
visited.append(1)
level[1]=0
parent={}

while queue:
    node=queue.pop(0)
    for neighbour in graph[node]:
        if  neighbour not in visited: # and neighbour not in queue: # => 2 logn
            visited.append(neighbour)
            queue.append(neighbour)
            # Parent, gives the path
            parent[neighbour]=node
            # Level
            level[neighbour]=level[node]+1
    

    