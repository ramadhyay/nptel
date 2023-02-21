#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 23:02:18 2023

@author: ram
"""
# finding cycles in a graph using BFS


graph={
       1:[2,3],
       2:[1],
       3:[4,5],
       4:[3,5],
       5:[4,3]
      }