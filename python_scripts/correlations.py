#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 22:36:46 2022

Plotting all the correlations

@author: nagehan
"""

import scipy
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

s = np.array([0.59, 1.44, 1.74, 2.40, 2.32, 2.41, 2.77, 2.55, 4.17, 4.04, 3.83, 6.92]) #average of all local depths
t = np.array([0.91, 1.37, 1.47, 1.53, 1.84, 1.37, 1.54, 1.89, 1.97, 2.31, 2.61, 2.72]) #average of all cortical thickness
gi = np.array([1.03, 1.35, 1.53, 1.69, 1.85, 1.81, 1.83, 1.77, 2.11, 2.33, 2.21, 2.53]) #gyrification index
vol = np.array([4, 15, 28, 92, 74, 88, 77, 90, 321, 325, 432, 1200]) #volume
sa = np.array([14, 53, 98, 210, 225, 228, 253, 261, 718, 750, 761, 2115]) #total surface area
sa_alpha = sa/gi #exposed surface area

#cortical thickness ratio, convex_to_concave
cc = np.array([1.05, 1.19, 1.18, 1.23, 1.33, 1.18, 1.19, 1.19, 1.19, 1.35, 1.39, 1.3])

cc1 = np.array([1.05, 1.19, 1.18])
cc2 = np.array([1.23, 1.33, 1.18, 1.19, 1.19])
cc3 = np.array([1.19, 1.35, 1.39])
cc4 = np.array([1.3])

s1 = np.array([0.59, 1.44, 1.74])
s2 = np.array([2.40, 2.32, 2.41, 2.77, 2.55])
s3 = np.array([4.17, 4.04, 3.83])
s4 = np.array([6.92])

sa1 = np.array([14, 53, 98])
sa2 = np.array([210, 225, 228, 253, 261])
sa3 = np.array([718, 750, 761])
sa4 = np.array([2115])

sa_alpha1 = np.array([14, 39, 64])
sa_alpha2 = np.array([124, 122, 126, 138, 147])
sa_alpha3 = np.array([340, 322, 344])
sa_alpha4 = np.array([836])

vol1 = np.array([4, 15, 28])
vol2 = np.array([92, 74, 88, 77, 90])
vol3 = np.array([321, 325, 432])
vol4 = np.array([1200])

t1 = np.array([0.91, 1.37, 1.47])
t2 = np.array([1.53, 1.84, 1.37, 1.54, 1.89])
t3 = np.array([1.97, 2.31, 2.61])
t4 = np.array([2.72])

gi1 = np.array([1.03, 1.35, 1.53])
gi2 = np.array([1.69, 1.85, 1.81, 1.83, 1.77])
gi3 = np.array([2.11, 2.33, 2.21])
gi4 = np.array([2.53])

# Plotting total brain volume and total surface area for each species

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(np.log(sa), np.log(vol))

m,b = np.polyfit(np.log(sa), np.log(vol), 1)

plt.plot(sa, np.exp(m * np.log(sa) + b), '--', color = 'gray')

plt.plot(sa, np.exp(1.5*np.log(sa) + 1.5*b), '--', color = 'gray', alpha=0.3)

plt.plot(sa1, vol1, 'o', color='#fde725', markersize=5, label='small') 
plt.plot(sa2, vol2, 'o', color='#35b779', markersize=5, label='medium') 
plt.plot(sa3, vol3, 'o', color='#31688e', markersize=5, label='large') 
plt.plot(sa4, vol4, 'o', color='#440154', markersize=5, label='xlarge') 
plt.legend()
plt.xscale('log') 
plt.yscale('log') 
plt.ylim(0, 10000)
plt.savefig('sa_vol.jpg', dpi=500, bbox_inches='tight')

# Plotting gyrification index and surface area for each species
import scipy
import scipy.stats

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(np.log(sa), gi)

m,b = np.polyfit(np.log(sa), gi, 1)

plt.plot(sa, m * np.log(sa) + b, '--', color = 'gray')

plt.plot(sa1, gi1, 'o', color='#fde725', markersize=5, label='small') 
plt.plot(sa2, gi2, 'o', color='#35b779', markersize=5, label='medium') 
plt.plot(sa3, gi3, 'o', color='#31688e', markersize=5, label='large') 
plt.plot(sa4, gi4, 'o', color='#440154', markersize=5, label='xlarge') 
plt.legend()
plt.xscale('log') 
plt.savefig('sa_gi.jpg', dpi=500, bbox_inches='tight')

# Plotting alpha_surface_area and pial_surface area for each species

import scipy
import scipy.stats

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(np.log(sa), np.log(sa_alpha))

m,b = np.polyfit(np.log(sa), np.log(sa_alpha), 1)

plt.plot(sa, np.exp(m * np.log(sa) + b), '--', color = 'gray')

x = np.linspace(0,1000,10)
y = x
plt.plot(x, y, '--', color='lightgray', zorder=1)

plt.plot(sa1, sa_alpha1, 'o', color='#fde725', markersize=5, label='small') 
plt.plot(sa2, sa_alpha2, 'o', color='#35b779', markersize=5, label='medium') 
plt.plot(sa3, sa_alpha3, 'o', color='#31688e', markersize=5, label='large') 
plt.plot(sa4, sa_alpha4, 'o', color='#440154', markersize=5, label='xlarge') 
plt.legend()
plt.xscale('log') 
plt.yscale('log') 
plt.savefig('sa_sa_alpha.jpg', dpi=500, bbox_inches='tight')

# Plotting sulcal depth and surface area for each species
import scipy
import scipy.stats

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(np.log(sa), np.log(s))

m,b = np.polyfit(np.log(sa), np.log(s), 1)

plt.plot(sa, np.exp(m * np.log(sa) + b), '--', color = 'gray')

plt.plot(sa, np.exp(0.5*np.log(sa) + 1.05*b), '--', color = 'gray', alpha=0.3)

plt.plot(sa1, s1, 'o', color='#fde725', markersize=5, label='small') 
plt.plot(sa2, s2, 'o', color='#35b779', markersize=5, label='medium') 
plt.plot(sa3, s3, 'o', color='#31688e', markersize=5, label='large') 
plt.plot(sa4, s4, 'o', color='#440154', markersize=5, label='xlarge') 
plt.xscale('log') 
plt.yscale('log') 
plt.ylim(0, 10)
plt.legend()
plt.savefig('area_depth.jpg', dpi=500, bbox_inches='tight')

# Plotting mean cortical thickness and mean surface area for each species
import scipy
import scipy.stats

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(np.log(sa), np.log(t))

m, b = np.polyfit(np.log(sa), np.log(t), 1)

plt.plot(sa, np.exp(m * np.log(sa) + b), '--', color = 'gray')

plt.plot(sa, np.exp(0.5*np.log(sa) + 2.15*b), '--', color = 'gray', alpha=0.3)

plt.plot(sa1, t1, 'o', color='#fde725', markersize=5, label='small') 
plt.plot(sa2, t2, 'o', color='#35b779', markersize=5, label='medium') 
plt.plot(sa3, t3, 'o', color='#31688e', markersize=5, label='large') 
plt.plot(sa4, t4, 'o', color='#440154', markersize=5, label='xlarge') 
plt.legend()
plt.xscale('log') 
plt.yscale('log') 
plt.ylim(0,3)
plt.savefig('area_thickness.jpg', dpi=500, bbox_inches='tight')

# plotting cortical thickness ratios to surface area for all species/groups
#convex-concave

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(np.log(sa), np.log(cc))

m,b = np.polyfit(np.log(sa), np.log(cc), 1)

plt.plot(sa, m * np.log(sa) + b, '--', color = 'gray')

plt.plot(sa1, cc1, 'o', color='#fde725', markersize=5, label='small') 
plt.plot(sa2, cc2, 'o', color='#35b779', markersize=5, label='medium') 
plt.plot(sa3, cc3, 'o', color='#31688e', markersize=5, label='large') 
plt.plot(sa4, cc4, 'o', color='#440154', markersize=5, label='xlarge') 
plt.legend()
plt.xscale('log')
plt.ylim(1,1.5)
plt.savefig('thickness_depth.jpg', dpi=500, bbox_inches='tight')

# plotting cortical thickness ratio (convex to concave) to cortical thickness for all species/groups

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(t, cc)

m,b = np.polyfit(t, cc, 1)
x = np.linspace(0.7,3,3)
plt.plot(x, m*x + b, '--', color = 'gray')
plt.plot(t1, cc1, 'o', color='#fde725', markersize=5, label='small') 
plt.plot(t2, cc2, 'o', color='#35b779', markersize=5, label='medium') 
plt.plot(t3, cc3, 'o', color='#31688e', markersize=5, label='large') 
plt.plot(t4, cc4, 'o', color='#440154', markersize=5, label='xlarge') 
plt.legend()
plt.ylim(1,1.5)
plt.xlim(0.8,3)
plt.xticks([1,1.5,2,2.5,3])
plt.savefig('thickness_ratio.jpg', dpi=500, bbox_inches='tight')

# Plotting gyrification index and cortical thickness ratio for each species
import scipy
import scipy.stats

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(gi, cc)

m,b = np.polyfit(gi, cc, 1)
x = np.linspace(0.5,3,3)
plt.plot(x, m*x + b, '--', color = 'gray')
plt.plot(gi1, cc1, 'o', color='#fde725', markersize=5, label='small') 
plt.plot(gi2, cc2, 'o', color='#35b779', markersize=5, label='medium') 
plt.plot(gi3, cc3, 'o', color='#31688e', markersize=5, label='large') 
plt.plot(gi4, cc4, 'o', color='#440154', markersize=5, label='xlarge') 
plt.legend()
plt.ylim(1,1.5)
plt.savefig('gi_cc.jpg', dpi=500, bbox_inches='tight')
