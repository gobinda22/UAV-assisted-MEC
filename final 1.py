# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:36:46 2021

@author: Gobinda
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame.from_dict({'x' : [0,27,29,27,13,27,32,27,56,63,76,63,73,63,99,63,15,22,38,22,0],
                             'y' : [0,26,12,26,14,26,45,26,2,17,24,17,4,17,46,17,63,98,85,98,0]})
x = df['x'].values
y = df['y'].values

u = np.diff(x)
v = np.diff(y)
pos_x = x[:-1] + u/2

pos_y = y[:-1] + v/2

norm = np.sqrt(u**2+v**2)

fig, ax = plt.subplots()
ax.plot(x, y,
    linewidth=0.5,
    linestyle='-',
    color='b',
    marker='o',
    markersize=10,
    markerfacecolor=('r'))
ax.plot(63, 17,
    linewidth=0.5,
    linestyle='-',
    color='b',
    marker='s',
    markersize=10,
    markerfacecolor=('b'))
ax.plot(27, 26,
    linewidth=0.5,
    linestyle='-',
    color='b',
    marker='s',
    markersize=10,
    markerfacecolor=('b'))
ax.plot(22, 98,
    linewidth=0.5,
    linestyle='-',
    color='b',
    marker='s',
    markersize=10,
    markerfacecolor=('b'))
# ax.plot(56, 30,
#     linewidth=0.5,
#     linestyle='-',
#     color='b',
#     marker='s',
#     markersize=10,
#     markerfacecolor=('b'))
# ax.plot(73, 89,
#     linewidth=0.5,
#     linestyle='-',
#     color='b',
#     marker='s',
#     markersize=10,
#     markerfacecolor=('b'))
# ax.plot(100, 48,
#     linewidth=0.5,
#     linestyle='-',
#     color='b',
#     marker='s',
#     markersize=10,
#     markerfacecolor=('b'))

ax.quiver(pos_x, pos_y, u/norm, v/norm, angles="xy",pivot="mid")
plt.show()