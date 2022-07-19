#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:45:34 2022

@author: nagehan
"""

import matplotlib.pyplot as plt
import numpy as np

# Sulcal depth with respect to shape

# Surface area small - senegal galago, night monkey, white faced saki

s1 = [[1.23,2.32,2.73],
        [0.93,1.74,1.98],
        [0.61,1.21,1.38]]

error1 = [[0.0,0.0,0.0],
          [0.0,0.0,0.0],
          [0.0,0.0,0.0]]

# Surface area medium - tufted capuchin, rhesus macaque, colobus, wooly monkey, graycheeked mangabey

s2 = [[3.51,4.41,3.61,4.01,3.93],
        [2.56,3.02,2.64,2.88,2.77],
        [1.77,1.52,1.79,2.07,1.79]]

error2 = [[0.0,0.57,0.0,0.0,0.0],
          [0.0,0.42,0.0,0.0,0.0],
          [0.0,0.23,0.0,0.0,0.0]]

# Surface area large - chimpanzee, bonobo, gorilla

s3 = [[6.61,6.38,6.12],
        [4.36,4.36,4.13],
        [3.13,2.60,2.51]]

error3 = [[0.26,0.0,0.0],
          [0.25,0.0,0.0],
          [0.23,0.0,0.0]]

# surface area XL - human

s4 = [[9.37],
        [7.08],
        [5.21]]

error4 = [[0.37],
          [0.36],
          [0.34]]

X = np.arange(3)
Y = np.array([4,5,6,7,8])
Z = np.array([10,11,12])
Q = np.array([14])

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])  #FDE725 #54278f

ax.bar(X - 0.25, s1[0], color = '#FDE725', width = 0.25, yerr = error1[0], bottom=0)
ax.bar(X + 0.00, s1[1], color = '#1F9E89', width = 0.25, yerr = error1[1], bottom=0)
ax.bar(X + 0.25, s1[2], color = '#54278f', width = 0.25, yerr = error1[2], bottom=0)

ax.bar(Y - 0.25, s2[0], color = '#FDE725', width = 0.25, yerr = error2[0], bottom=0)
ax.bar(Y + 0.00, s2[1], color = '#1F9E89', width = 0.25, yerr = error2[1], bottom=0)
ax.bar(Y + 0.25, s2[2], color = '#54278f', width = 0.25, yerr = error2[2], bottom=0)

ax.bar(Z - 0.25, s3[0], color = '#FDE725', width = 0.25, yerr = error3[0], bottom=0)
ax.bar(Z + 0.00, s3[1], color = '#1F9E89', width = 0.25, yerr = error3[1], bottom=0)
ax.bar(Z + 0.25, s3[2], color = '#54278f', width = 0.25, yerr = error3[2], bottom=0)

ax.bar(Q - 0.25, s4[0], color = '#FDE725', width = 0.25, yerr = error4[0], bottom=0)
ax.bar(Q + 0.00, s4[1], color = '#1F9E89', width = 0.25, yerr = error4[1], bottom=0)
ax.bar(Q + 0.25, s4[2], color = '#54278f', width = 0.25, yerr = error4[2], bottom=0)

ax.legend(labels=['concave', 'saddle', 'convex'], loc='upper left', fontsize=10)
ax.set(ylim=(0.0, 10))

# x_labels = ('Senegal Galago', 'Night Monkey', 'White-faced Saki')
# plt.xticks(X, x_labels,rotation=90)

# x_labels = ('Tufted Capuchin', 
#             'Rhesus Macaque', 'Black-and-white Colobus', 'Wooly Monkey', 'Grey-cheeked Mangabey')
# plt.xticks(Y, x_labels,rotation=90)

# x_labels = ('Chimpanzee', 'Bonobo', 'Gorilla')
# plt.xticks(Z, x_labels,rotation=90)

# x_labels = ('Human')
# plt.xticks(Q, x_labels,rotation=90)

T = np.array([0,1,2,4,5,6,7,8,10,11,12,14])
x_labels = ('Senegal Galago', 'Night Monkey', 'White-faced Saki', 'Tufted Capuchin', 
            'Rhesus Macaque', 'Black-and-white Colobus', 'Wooly Monkey', 'Grey-cheeked Mangabey',
            'Chimpanzee', 'Bonobo', 'Gorilla', 'Human')
plt.xticks(T, x_labels,rotation=90)

plt.savefig('barplot_depth.jpg', dpi=500, bbox_inches='tight')


