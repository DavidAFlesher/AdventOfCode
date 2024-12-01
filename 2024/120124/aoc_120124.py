# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:51:25 2024

@author: david
"""

# %% Parse input

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


data1 = []
data2 = []
for line in lines:
    l1, l2 = line.split()
    data1.append(int(l1))
    data2.append(int(l2))
data1.sort()
data2.sort()


# %% Part 1

ans = 0
for d1, d2 in zip(data1, data2):
    diff = abs(d2 - d1)
    ans += diff
print(ans)
# %% Part 2

# brute force
ans = 0
for d1 in data1:
    n = 0
    for d2 in data2:
        if d1 == d2:
            n +=1
    ans += d1 * n
print(ans)

# %% Thoughts
'''
This year I'm going to write some thoughts down for each problem.

This year's day 1 was really easy again, which is a nice change compared
to 2023! I lost a few moments because I thought the difference was based
on the original list index, so I did a list of lists then sorted by a key, 
but its actually just very straightforward. For part2, for a speed up, you 
could add some 'break' logic after passing your int in the sorted list, but 
brute force is good enough.
'''