#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 09:24:33 2023

@author: ram
"""

import numpy as np
from matplotlib import pyplot as plt

x=[2,3,5,2,-1,-2]
y=[4,-1,6,0,0,2]
label=[1,-1,-1,1,1,1]

plt.scatter(x,y,c=label)


value = 1/(1+np.exp(-0.1))

print(value)