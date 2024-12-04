# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 23:53:53 2024

@author: david
"""
# %% parse input

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

import numpy as np

grid = np.array([list(l) for l in lines])
# pad grid
ngrid = np.zeros(150*150,str).reshape(150, 150)
ngrid[5:-5, 5:-5] = grid
# %% Part 1

# limit scope to where X starts
i_coords, j_coords = np.where(ngrid == "X")

def searchXMAS(ic, jc, idir, jdir):
    # ic, jc original coord, idir jdir +/- 1|0 for direction
    # check in given direction for "MAS"
    # return True if found. Assume start at "X"
    global ngrid
    ics = [ic + idir, ic + idir*2, ic + idir*3]
    jcs = [jc + jdir, jc + jdir*2, jc + jdir*3]

    if not ngrid[ics[0], jcs[0]] == "M":
        return False
    elif not ngrid[ics[1], jcs[1]] == "A":
        return False
    elif not ngrid[ics[2], jcs[2]] == "S":
        return False
    else:
        # spelled out XMAS
        return True

ans1 = 0
for ic, jc in zip(i_coords, j_coords):
    # check all directions for "MAS"
    # there is probably a shorter way to type this, but whatever
    if searchXMAS(ic, jc, 0, 1):
        ans1 += 1
    if searchXMAS(ic, jc, 1, 1):
        ans1 += 1
    if searchXMAS(ic, jc, 1, 0):
        ans1 += 1
    if searchXMAS(ic, jc, 1, -1):
        ans1 += 1
    if searchXMAS(ic, jc, 0, -1):
        ans1 += 1
    if searchXMAS(ic, jc, -1, -1):
        ans1 += 1
    if searchXMAS(ic, jc, -1, 0):
        ans1 += 1
    if searchXMAS(ic, jc, -1, 1):
        ans1 += 1
print(ans1)

# %% Part 2

# Find 'A' centers
ni_coords, nj_coords = np.where(ngrid == "A")

def searchCorners(ic, jc):
    # Return True if coord is a MAS crossing. Assume ic,jc == A
    global ngrid
    UR = ngrid[ic+1, jc+1]
    LR = ngrid[ic+1, jc-1]
    LL = ngrid[ic-1, jc-1]
    UL = ngrid[ic-1, jc+1]
    corners = [UR, LR, LL, UL]
    if not (corners.count("S") == 2 and corners.count("M") == 2):
        # not two MAS
        return False
    elif UR == LL or UL == LR:
        # M across from M, S across from S
        return False
    else:
        return True

ans2 = 0
for ic, jc in zip(ni_coords, nj_coords):
    if searchCorners(ic, jc):
        ans2 += 1
print(ans2)
# %% Thoughts
"""
I liked this one. I thought Part 1 was more complicated than Part 2 actually.
There's probably a better way to solve this without padding the input to avoid
index errors, but good enough. You can also avoid using numpy, but I'm more use
to using numpy for 2D arrays than list of lists.
"""
