#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 07:40:16 2023

@author: ram
"""
dag = {
        1:[2],
        2:[3,4],
        3:[4],
        4:[]
        
}


indegree={}
stack=[]

for u in dag.keys():
    indegree[u]=0


for u in dag.keys():
    for v in dag[u]:
        indegree[v] += 1

for u in indegree.keys():
    if indegree[u] == 0:
        stack.append(u)

visited={}

def visit(G,v):
    visited[v]=True
    print(v, end="->")
    for neighbour in G[v]:
        if neighbour not in visited:
            visit(G,neighbour)

visit(dag,1)

# Topological sort
print("\nTopological sort!")
while stack:
    u=stack.pop(0)
    print(u,end="->")
    for v in dag[u]:
        indegree[v] -= 1
        if indegree[v]==0:
            stack.append(v)
        
    