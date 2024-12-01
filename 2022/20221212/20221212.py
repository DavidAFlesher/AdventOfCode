# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 05:19:26 2022

@author: david
"""

# read lines and convert letters to number vals a-z -> 1-26
with open("input.txt", "r") as f:
    lines = [[str(ord(x) - 96) for x in line.strip('\n')] for line in f.readlines()]

with open("grid2.csv", "w+") as f:
    for line in lines:
        f.write(','.join(line))
        f.write('\n')
