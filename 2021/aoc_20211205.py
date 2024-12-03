# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:51:44 2024

@author: david
"""

# %% Parse input

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

coords = []
for line in lines:
    c1, c2 = line.split("->")
    c1 = list(map(int, c1.strip().split(",")))
    c2 = list(map(int, c2.strip().split(",")))
    coords.append([c1, c2])

# %% Part 1

import numpy as np

# assume grid is resonably sized (coords rep by 3 digit int)
arr = np.zeros(1000*1000).reshape(1000, 1000)

for (x1, y1), (x2, y2) in coords:
    # if horizontal
    if x1 == x2:
        s = min([y1, y2])
        e = max([y1, y2]) + 1
        arr[s:e, x1] += 1
    # if vertical
    elif y1 == y2:
        s = min([x1, x2])
        e = max([x1, x2]) + 1
        arr[y1, s:e] += 1

x, y = np.where(arr >= 2)
print(len(x))

# %% Part 2

# assume grid is resonably sized (coords rep by 3 digit int)
arr = np.zeros(1000*1000).reshape(1000, 1000)

for (x1, y1), (x2, y2) in coords:
    # if horizontal
    if x1 == x2:
        s = min([y1, y2])
        e = max([y1, y2]) + 1
        arr[s:e, x1] += 1
    # if vertical
    elif y1 == y2:
        s = min([x1, x2])
        e = max([x1, x2]) + 1
        arr[y1, s:e] += 1
    # diagonal
    else:
        # there might be a nifty geometric way to solve, but I will loop force
        xr = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)[::-1]
        yr = range(y1, y2+1) if y1 < y2 else range(y2, y1+1)[::-1]
        for r, c in zip(yr, xr):
            arr[r, c] +=1

x, y = np.where(arr >= 2)
print(len(x))
