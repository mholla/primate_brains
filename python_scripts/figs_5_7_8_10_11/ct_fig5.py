#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:06:34 2022

@author: nagehan
"""

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = np.linspace(0,3,10)
y = x
plt.plot(x, y, '--', color='lightgray', zorder=1)

plt.ylim(0.5,3)
plt.xlim(0.5,3)


# Senegal Galago
sen_mine_mean = [0.91] # n=1
#y1 = 1.19 # n=1
y2 = 0.81 # n=1

#n1 = 1
n2 = 1

#y = (y1*n1 + y2*n2)/(n1+n2)


plt.errorbar([0.91], [0.81], fmt='s',
             color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0) 

# Night Monkey
nm_mine_mean = 1.37 # n=1
y1 = 1.3 # n=1
#y2 = 1.5 # n=3
#y3 = 1.67 # n=1

n1 = 1
#n2 = 3
#n3 = 1

s1 = 0
#s2 = 0.039
#s3 = 0

#y = (y1*n1 + y2*n2 + y3*n3)/(n1+n2+n3)
#s = np.sqrt((n1*s1*s1 + n2*s2*s2 + n3*s3*s3 + n1*(y1-y)**2 + n2*(y2-y)**2 + n3*(y3-y)**2)/(n1+n2+n3))

plt.errorbar([1.37], [1.3], fmt='s',
             color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0)

# White Faced Saki
wfs_mine_mean = [1.47]
wfs_br_mean = [1.44]

plt.errorbar([1.47], [1.44], fmt='s',
             color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0)

# Tufted capuchin
tc_mine_mean = [1.53]
#y1 = 1.47
y2 = 1.77
y3 = 2.067

#n1 = 1
n2 = 2
n3 = 1

#s1 = 0
s2 = 0.15
s3 = 0

y = (y2*n2 + y3*n3)/(n2+n3)
s = np.sqrt((n2*s2*s2 + n3*s3*s3 + n2*(y2-y)**2 + n3*(y3-y)**2)/(n2+n3))


plt.errorbar([1.53], y, yerr = s, fmt='o',
             color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0)

# Macaques
mac_ants = np.array([2.05, 1.97, 1.97, 2.05, 1.98, 2.02, 2.05, 2.02, 2.04, 2.05, 2.04, 2.04, 2.05, 2.03,
                     2.05, 2.04, 2.05, 2.03, 2.03, 2.05, 2.04, 2.04, 2.05, 2.05])

mac_mine = np.array([1.94, 1.95, 1.88, 2.00, 1.85, 1.87, 1.87, 2.05, 1.98, 1.97, 1.82, 1.87, 1.78, 1.72,
                     1.76, 1.74, 1.85, 1.56, 1.72, 1.91, 1.82, 1.86, 1.77, 1.91, 1.85, 1.64, 1.85, 1.85])

mac_mine_mean = 1.85
mac_mine_std = 0.11

#y1 = 2.03 # ANTs volumetric data mean
y2 = 2.37 # Koo 2012
y3 = 1.99 # Lepage 2021
y4 = 1.73 # Donahue, 2018
y5 = 1.74 # Bourgeous, 1994
y6 = 2.2 #Hofman 1985
y7 = 1.714 #Houzel 2015
#y8 = 1.413
#y9 = 1.835
#y10 = 1.572


#n1 = 28
n2 = 18
n3 = 31
n4 = 19
n5 = 25
n6 = 1
n7 = 1
#n8 = 1
#n9 = 1
#n10 = 1

#s1 = 0.025 # ANTs volumetric data std
s2 = 0.19
s3 = 0.43
s4 = 0.1
s5 = 0.34
s6 = 0.0
s7 = 0.0
#s8 = 0.0
#s9 = 0.0
#s10 = 0.0

# y = (y1*n1+y2*n2+y3*n3+y4*n4+y5*n5+y6*n6+y7*n7+y8*n8+y9*n9+y10*n10)/(n1+n2+n3+n4+n5+n6+n7+n8+n9+n10)

# s = np.sqrt((n1*s1*s1+n2*s2*s2+n3*s3*s3+n4*s4*s4+n5*s5*s5+n6*s6*s6+n7*s7*s7+n8*s8*s8+n9*s9*s9+n10*s10*s10 + 
#              n1*(y1-y)**2 + n2*(y2-y)**2 + n3*(y3-y)**2 + n4*(y4-y)**2 + n5*(y5-y)**2 + 
#              n6*(y6-y)**2 + n7*(y7-y)**2 + n8*(y8-y)**2 + n9*(y9-y)**2 + n10*(y10-y)**2)/(n1+n2+n3+n4+n5+n6+n7+n8+n9+n10))

y = (y2*n2+y3*n3+y4*n4+y5*n5+y6*n6+y7*n7)/(n2+n3+n4+n5+n6+n7)

s = np.sqrt((n2*s2*s2+n3*s3*s3+n4*s4*s4+n5*s5*s5+n6*s6*s6+n7*s7*s7 + 
              + n2*(y2-y)**2 + n3*(y3-y)**2 + n4*(y4-y)**2 + n5*(y5-y)**2 + 
             n6*(y6-y)**2 + n7*(y7-y)**2 )/(n2+n3+n4+n5+n6+n7))

plt.errorbar([1.9], y, xerr = mac_mine_std, yerr = s, fmt='o',
             color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0)

# Colobus
co_mine_mean = [1.37]
co_br_mean = [1.36]

plt.errorbar([1.37], 1.36, fmt='s',
             color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0)

# Wooly Monkey
wm_mine_mean = [1.54]
wm_br_mean = [1.50]

wm_mean = [1.54, 1.50]
wm_std = [0, 0]

plt.errorbar([1.54], 1.50, fmt='s',
             color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0)

# Gray Cheeked Mangabey
gcm_mine_mean = [1.89]
gcm_br_mean = [1.78]

gcm_mean = [1.78, 1.89]
gcm_std = [0, 0]

plt.errorbar([1.89], 1.78, fmt='s',
             color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0)

# Chimpanzees
chi_cat = np.array([2.21, 2.15, 2.22, 2.11, 1.96, 2.19, 2.09, 2.10, 2.20, 2.10, 2.37, 2.17, 2.03, 2.14, 2.21, 2.43,
                      2.22, 2.07, 2.18, 2.14, 2.19, 2.13, 2.05, 1.93, 2.04, 2.09, 2.20, 2.12, 2.22, 2.00, 2.13, 2.12,
                      2.24, 2.04, 2.24, 2.11, 2.31, 2.21, 1.95, 2.13, 2.28, 2.03, 2.07, 2.35, 2.30, 2.35, 1.94, 2.47,
                      2.58, 2.14, 2.25, 2.43])


chi_mine = np.array([1.98, 1.93, 1.95, 1.96, 1.78, 2.01, 1.98, 1.94, 2.03, 1.96, 2.11, 1.94, 1.91, 1.93, 2.05, 2.13,
                       2.03, 1.93, 1.98, 1.99, 1.96, 1.92, 1.86, 1.80, 1.91, 1.89, 2.05, 1.92, 1.97, 1.84, 1.95, 1.83,
                       2.01, 1.86, 2.01, 2.00, 2.10, 2.01, 1.85, 1.96, 2.07, 1.92, 1.93, 2.10, 2.04, 2.03, 1.83, 2.21,
                       2.19, 2.00, 2.01, 2.05])


chi_mine_mean = [1.97]
#y1 = 2.17 # CAT report results mean
y2 = 1.71 # Autrey, 2014
#y3 = 1.984
y4 = 2.6 # Donahue, 2018
#y5 = 2.2
#y6 = 2.4
#y7 = 1.57
#y8 = 1.41
y9 = 1.4 #Xiang, 2020

#n1 = 54
n2 = 219
#n3 = 34
n4 = 29
# n5 = 3
# n6 = 71
# n7 = 0.044
# n8 = 74
n9 = 77

chi_mine_std = [0.09]
#s1 = 0.14 # CAT report results mean
s2 = 0.05
# s3 = 0.42
s4 = 0.1
# s5 = 0.0
# s6 = 0.0425
# s7 = 67
# s8 = 0.0185
s9 = 0.0125

# y = (y1*n1+y2*n2+y3*n3+y4*n4+y5*n5+y6*n6+y7*n7+y8*n8+y9*n9)/(n1+n2+n3+n4+n5+n6+n7+n8+n9)
# s = np.sqrt((n1*s1*s1+n2*s2*s2+n3*s3*s3+n4*s4*s4+n5*s5*s5+n6*s6*s6+n7*s7*s7+n8*s8*s8+n9*s9*s9 + 
#              n1*(y1-y)**2 + n2*(y2-y)**2 + n3*(y3-y)**2 + n4*(y4-y)**2 + n5*(y5-y)**2 + 
#              n6*(y6-y)**2 + n7*(y7-y)**2 + n8*(y8-y)**2 + n9*(y9-y)**2)/(n1+n2+n3+n4+n5+n6+n7+n8+n9))

y = (y2*n2+y4*n4+y9*n9)/(n2+n4+n9)

s = np.sqrt((n2*s2*s2+n4*s4*s4+n9*s9*s9 + 
              n2*(y2-y)**2 + n4*(y4-y)**2 + n9*(y9-y)**2)/(n2+n4+n9))


plt.errorbar([1.97], y, xerr = 0.09, yerr = s, fmt='o',
             color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0)

# Bonobo
bo_mine_mean = [2.31]
y1 = 2.458
n1 = 34
s1 = 0.69

plt.errorbar([2.31], 2.458, yerr = 0.69, fmt='^',
             color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0)

# Gorilla
go_mine_mean = [2.61]
y1 = 2.5
n1 = 1
s1 = 0.0

plt.errorbar([2.61], 2.5, fmt='^',
             color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0)

# Human
hum_mine_mean = [2.72]
y1 = 2.81
y2 = 2.938
y3 = 2.7
y4 = 2.3
#y5 = 2.8
y5 = 2.5
y6 = 2.6

n1 = 1
n2 = 1
n3 = 60
n4 = 91
#n5 = 3
n5 = 30
n6 = 26+18

s1 = 0.0
s2 = 0.0
s3 = 0.1
s4 = 0.09
#s5 = 0.0
s5 = 0.7
s6 = 0

y = (y1*n1+y2*n2+y3*n3+y4*n4+y5*n5+y6*n6)/(n1+n2+n3+n4+n5+n6)
s = np.sqrt((n1*s1*s1+n2*s2*s2+n3*s3*s3+n4*s4*s4+n5*s5*s5+n6*s6*s6 + 
              n1*(y1-y)**2 + n2*(y2-y)**2 + n3*(y3-y)**2 + n4*(y4-y)**2 + n5*(y5-y)**2 + n6*(y6-y)**2)/(n1+n2+n3+n4+n5+n6))

# y = (y1*n1+y2*n2+y3*n3+y4*n4)/(n1+n2+n3+n4)

# s = np.sqrt((n1*s1*s1 + n2*s2*s2 + n3*s3*s3 + n4*s4*s4 + 
#              n1*(y1-y)**2 + n2*(y2-y)**2 + n3*(y3-y)**2 + n4*(y4-y)**2)/(n1+n2+n3+n4))

plt.errorbar([2.72], y, xerr = 0.17, yerr = s, fmt='o',
              color = 'black', ecolor = 'black', markersize=4, elinewidth = 0.5, capsize=0)



# #Regression Plot
# import scipy
# import scipy.stats

# mine_t = np.array([0.91, 1.37, 1.47, 1.53, 1.84, 1.37, 1.54, 1.89, 1.97, 2.31, 2.61, 2.72])
# others_t = np.array([1, 1.49, 1.44, 1.77, 1.97, 1.36, 1.50, 1.78, 1.82, 2.45, 2.5, 2.47])

# slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(mine_t, others_t)

# m,b = np.polyfit(mine_t, others_t, 1)
# x = np.linspace(0,3,10)
# plt.plot(x, m*x + b, '--', color = 'lightgray')

#plt.legend()

plt.savefig('thickness_grouped.jpg', dpi=500, bbox_inches='tight')













