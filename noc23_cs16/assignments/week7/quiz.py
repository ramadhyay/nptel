#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 23:28:35 2023

@author: ram
"""

match_timings=[[7,45],[15,31],[35,47],[46,61],[48,60],[57,58],[59,63],[64,70],[71,80],[75,90],[81,83],[91,100]]

Next=[]
Watch=[]
for i in range(0,len(match_timings)):
    Watch.append(None)
    Next.append(0)
    for j in range(i, len(match_timings)):
        if (match_timings[j][0] >= match_timings[i][1]):
            Next[i]=j
            break

Watch[len(match_timings)-1]=1    
for i in range(len(match_timings)-2, -1, -1):
    Watch[i]=max(1+Watch[Next[i]], Watch[i+1])