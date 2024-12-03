# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 23:41:31 2024

@author: david
"""

# %% Parse input

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = [line.split(" ") for line in lines]
    lines = [[direction, int(val)] for direction, val in lines]

# %% Part 1
hor_pos = 0
depth_pos = 0

for _dir, val in lines:
    if _dir == "forward":
        hor_pos += val
    elif _dir == "down":
        depth_pos += val
    elif _dir == "up":
        depth_pos += -val
    else:
        raise ValueError("Unexpected direction")

print(hor_pos * depth_pos)

# %% Part 2

hor_pos = 0
depth_pos = 0
aim = 0

for _dir, val in lines:
    if _dir == "forward":
        hor_pos += val
        depth_pos += aim * val
    elif _dir == "down":
        aim += val
    elif _dir == "up":
        aim += -val
    else:
        raise ValueError("Unexpected direction")

print(hor_pos * depth_pos)
