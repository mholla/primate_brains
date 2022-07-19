#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 09:24:34 2022

@author: nagehan
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.stats

gi = np.array([1.03, 1.69, 1.85, 1.83, 1.77, 2.11, 2.33, 2.21, 2.53])
gi_zilles = np.array([1.17, 1.60, 1.75, 1.97, 1.87, 2.31, 2.17, 2.17, 2.56])

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(gi, gi_zilles)

m,b = np.polyfit(gi, gi_zilles, 1)

fig = plt.figure()

# x = np.linspace(0,10,3)
# plt.plot(x, m * x + b, '--', color = 'gray')

x = np.linspace(0,3,10)
y = x
plt.plot(x, y, '--', color='lightgray', zorder=1)
plt.plot(gi, gi_zilles, 'o', color='black', markersize=5) 
plt.xlim(1,3)
plt.ylim(1,3)

plt.savefig('gi.jpg', dpi=500, bbox_inches='tight')