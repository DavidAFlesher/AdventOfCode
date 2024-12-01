# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:54:19 2024

@author: david
"""

# %% Parse input
import numpy as np

with open("input.txt", "r") as f:
    pos = np.array(list(map(int, f.read().split(","))))

# %% Part 1 and Part2

def resPt1(pos, guess):
    # get residual of crab position to guess position, Part 1
    res = np.sum(np.absolute(pos - guess))
    return res

def resPt2(pos, guess):
    # get distance traveled in Part 2
    res = np.absolute(pos - guess)
    # formula gets bionomial, aka the total fuel cost by total dist traveled
    res = sum([int((n**2 + n)/2) for n in res])
    return res

pt1_res = []
pt2_res = []
for guess in range(min(pos), max(pos)):
    pt1_res.append(resPt1(pos, guess))
    pt2_res.append(resPt2(pos, guess))

print(min(pt1_res)) # Part 1 answer
print(min(pt2_res)) # Part 2 answer
