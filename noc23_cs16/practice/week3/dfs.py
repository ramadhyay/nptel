#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 23:28:18 2023

@author: ram
"""
graph={
        1:[2,3,4],
        2:[1,3],
        3:[1,2],
        4:[1,5,8],
        5:[4,6,7],
        6:[5,7,9,8],
        7:[5,6],
        8:[4,6,9],
        9:[6,10],
        10:[]
      }

# graph={
#         1:[2,3],
#         2:[4,1],
#         3:[4,1],
#         4:[1,3]
#         }

stack=[]
visited=[]
level={}
parent={}

dfs_counter={}
counter=0

def dfs(G,v):
    visited.append(v)

    global counter 
    dfs_counter[v]=[]
    dfs_counter[v].append(counter)
    counter = counter+1
    
    for neighbour in G[v]:
        if neighbour not in visited:
            parent[neighbour]=v
            dfs(G,neighbour)
    dfs_counter[v].append(counter)
    counter += 1
        
    
    
dfs(graph,4)    

visited=[]
stack.append(1)
visited.append(1)
popstack=False

def dfs_iter():
    while stack:
        node=stack.pop()
        if node not in visited:
            visited.append(node)
            for neighbour in graph[node]:
                    stack.append(neighbour)
    
dfs_iter()