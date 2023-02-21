#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 10:16:01 2023

@author: ram
"""

# l=130
# w=340
# n=5

# coordinates=[
#                 [10,50],
#                 [130,130],
#                 [70,170],
#                 [0,180],
#                 [60,260]
#             ]

# r is the radius of a soldier view
# Distance between soliders should be less than or equal to 2r(=d) if they overlab
r=100
d=2*r

# Input l,w and n. Here l has no bearing on the outcome and w is the key. 
# May we can add some input validations around it.
inputs=input()
lwn=[eval(i) for i in inputs.split()]

l=lwn[0]
w=lwn[1]
n=lwn[2]

# Soldier co-ordinates
coordinates=[]
for i in range(0,n):
    inputs=input()
    xy=[eval(i) for i in inputs.split()]
    coordinates.append([xy[0],xy[1]])

# Initialize the graph.
graph={}
start=[]
end=[]

# distance function
def distance(p1,p2):
    return round((( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 ) **0.5),2)


# Adding s & t which are in the range of view of soldiers
for i in range(0,n):
    if coordinates[i][1]+r>=w:
        coordinates.append([coordinates[i][0],w])
        start.append(len(coordinates)-1)

    if coordinates[i][1]-r<=0:
        coordinates.append([coordinates[i][0],0])    
        end.append(len(coordinates)-1)
    
# New number of co-ordinates
n=len(coordinates)    

# Create a graph. Calculate the distance between each of the co-ordinates and
# build a grapsh when there is overlap. Distance is less than 200
for i in range(0,n):
    if i not in graph:
        graph[i]=[]
    for j in range(i+1, n):
        s=distance(coordinates[i],coordinates[j])
        if s <= d:
            if j not in graph:
                graph[j]=[]
            
            if j not in graph[i]:
                graph[i].append(j)
            
            if i not in graph[j]:
                graph[j].append(i)


# Visited array
visited=[]
escape=[]

def visit(G,v):
    visited.append(v)
    if v in end:
        escape.append(v)
        return
    for u in G[v]:
        if u not in visited:
            visit(G,u)


# For each start perform DFS
for v in start:
    visited=[]
    visit(graph,v)
    if escape:
        break;

if escape or not(end):
    print(1)
else:
    print(0)    
