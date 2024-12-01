# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 00:45:04 2022

@author: david
"""

# part1
print(max([sum([int(c) for c in b]) for b in [a.split("\n") for a in open("input.txt", "r").read().split("\n\n")]]))

# part 2
print(sum(sorted([sum([int(c) for c in b]) for b in [a.split("\n") for a in open("input.txt", "r").read().split("\n\n")]], reverse = True)[:3]))
