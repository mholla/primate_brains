#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:43:28 2022

@author: nagehan
"""
import matplotlib.pyplot as plt
import numpy as np

# Cortical thickness with respect to shape

# Surface area small

t1 = [[0.93,1.44,1.56],
        [0.90,1.37,1.45],
        [0.89,1.21,1.32]]

error1 = [[0.0,0.0,0.0],
          [0.0,0.0,0.0],
          [0.0,0.0,0.0]]

# Surface area medium

t2 = [[1.65,2.07,1.44,1.63,2.02],
        [1.52,1.81,1.37,1.54,1.85],
        [1.34,1.56,1.22,1.37,1.70]]

error2 = [[0.0,0.14,0.0,0.0,0.0],
          [0.0,0.12,0.0,0.0,0.0],
          [0.0,0.11,0.0,0.0,0.0]]

# Surface area large

t3 = [[2.08,2.57,2.93],
        [1.95,2.25,2.52],
        [1.75,1.90,2.11]]

error3 = [[0.10,0.0,0.0],
          [0.07,0.0,0.0],
          [0.09,0.0,0.0]]

# surface area XL

t4 = [[2.96],
        [2.70],
        [2.33]]

error4 = [[0.17],
          [0.17],
          [0.17]]

X = np.arange(3)
Y = np.array([4,5,6,7,8])
Z = np.array([10,11,12])
Q = np.array([14])

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

ax.bar(X - 0.25, t1[2], color = '#FDE725', width = 0.25, yerr = error1[0], bottom=0)
ax.bar(X + 0.00, t1[1], color = '#1F9E89', width = 0.25, yerr = error1[1], bottom=0)
ax.bar(X + 0.25, t1[0], color = '#54278f', width = 0.25, yerr = error1[2], bottom=0)

ax.bar(Y - 0.25, t2[2], color = '#FDE725', width = 0.25, yerr = error2[0], bottom=0)
ax.bar(Y + 0.00, t2[1], color = '#1F9E89', width = 0.25, yerr = error2[1], bottom=0)
ax.bar(Y + 0.25, t2[0], color = '#54278f', width = 0.25, yerr = error2[2], bottom=0)

ax.bar(Z - 0.25, t3[2], color = '#FDE725', width = 0.25, yerr = error3[0], bottom=0)
ax.bar(Z + 0.00, t3[1], color = '#1F9E89', width = 0.25, yerr = error3[1], bottom=0)
ax.bar(Z + 0.25, t3[0], color = '#54278f', width = 0.25, yerr = error3[2], bottom=0)

ax.bar(Q - 0.25, t4[2], color = '#FDE725', width = 0.25, yerr = error4[0], bottom=0)
ax.bar(Q + 0.00, t4[1], color = '#1F9E89', width = 0.25, yerr = error4[1], bottom=0)
ax.bar(Q + 0.25, t4[0], color = '#54278f', width = 0.25, yerr = error4[2], bottom=0)

ax.legend(labels=['concave', 'saddle', 'convex'], loc='upper left', fontsize=10)
ax.set(ylim=(0.0, 4.0))

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

plt.savefig('barplot_grouped.jpg', dpi=500, bbox_inches='tight')


