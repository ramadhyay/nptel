#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:44:52 2023

@author: ram
"""

import matplotlib.pyplot as plt
import numpy as np
coordinates=[[200, 0], [250, 200], [100, 150], [400, 150], [200, 0], [250, 300]]

data=np.array(coordinates)

plt.scatter(data[:, 0], data[:, 1], cmap='hot')