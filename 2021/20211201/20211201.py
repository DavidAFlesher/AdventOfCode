# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 04:18:39 2023

@author: david
"""

with open("input.txt", "r") as f:
    lines = [int(line.strip('\n')) for line in f.readlines()]

# %%

counter_pt1 = 0
prev = None
for line in lines:
    if not prev == None:
        if line > prev:
            counter_pt1 += 1
    prev = line
print(counter_pt1) # Answer: 1692

# %%
counter_pt2 = 0
prev_pt2 = None
curr = None
for i in range(len(lines)-2):
    if not prev_pt2 == None:
        curr = [lines[i], lines[i+1], lines[i+2]]
        if sum(curr) > sum(prev_pt2):
            counter_pt2 += 1
    prev_pt2 = [lines[i], lines[i+1], lines[i+2]]
print(counter_pt2)
