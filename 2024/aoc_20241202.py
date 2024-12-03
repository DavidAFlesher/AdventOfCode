# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 00:00:39 2024

@author: david
"""


# %% Parse input

with open("input.txt", "r") as f:
    # split line and convert str to int
    lines = [list(map(int, line.strip().split())) for line in f.readlines()]

# %% Part 1

def safe(line):
    # determine if a line is safe
    # first, get differences between each integer in list
    diffs = []
    for i in range(len(line)-1):
        v1 = line[i]
        v2 = line[i+1]
        diffs.append(v1-v2)
    if not (line == sorted(line) or line == sorted(line, reverse=True)):
        # not all in incr or dec order
        return False
    elif not len([d for d in diffs if 0 < abs(d) <= 3]) == len(diffs):
        # not all diff vals are within the 0 < d <= 3 tolerance
        return False
    else:
        # Level not unsafe, therefore it is safe
        return True

ans = 0
for line in lines:
    if safe(line):
        ans += 1
print(ans)

# %% Part 2

ans = 0
for line in lines:
    if safe(line):
        ans += 1
    else:
        # also try deleting every index in the list and re-evaluating if it
        # is a safe line.
        for i in range(len(line)):
            nline = line.copy()
            nline.pop(i)
            if safe(nline):
                ans += 1
                # break because only need at least one valid solution per line
                # don't want to double count if multiple solutions exist per line
                break
print(ans)

# %% Thoughts

"""
I was really slow today. For part one, I originally wrote a solution that didn't
use a function and it was way clunkier. Then, for part 2, it was obvious I should
have written a function so I converted some of my logic into the new function 'safe'.
I should have kept my worse Part 1 solution for reference, but I deleted it without
thinking.
"""
