#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:39:15 2023

@author: ram
"""

import numpy as np

maxcost=10
# mincost = np.array([],dtype="int32")
h=400
n=7
c=6

mincost=[]
for i in range(0,n+1):
    mincost.append([])
    for j in range(0,c+1):
        mincost[i].append(maxcost+1)

mincost2=[ [maxcost for j in range(0,c+1)] for i in range(0,n+1) ]
