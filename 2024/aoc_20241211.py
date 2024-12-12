# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 00:04:28 2024

@author: david
"""

# %% Parse input

with open("input.txt", "r") as f:
    line = f.readline().strip().split()

# %% Part 1
#line = ['125', '17']

for _ in range(25):
    nline = []
    for l in line:
        if l == '0':
            nline.append("1")
        elif len(l)%2 == 0:
            # is even
            n1 = int(l[:len(l)//2])
            n2 = int(l[len(l)//2:])
            nline.append(str(n1))
            nline.append(str(n2))
        else:
            n1 = int(l) * 2024
            nline.append(str(n1))
    line = nline
print(len(line))

# %% Part 2
# can't brute force this one
# Keep a dictionary instead of a list

from collections import defaultdict

# Initialize with starting list of rocks
rocks = defaultdict(int)
for l in line:
    rocks[l] = 1

for _ in range(75):
    curr_rocks = rocks.copy()
    # Loop through rocks and perform rock modifications n number of times
    # where n is the number of rocks (v) of that "type" (with the same label, k)
    for k, v in curr_rocks.items():
        if k == "0":
            rocks["1"] += v
            rocks[k] += -v
        elif len(k)%2 == 0:
            # is even
            n1 = int(k[:len(k)//2])
            n2 = int(k[len(k)//2:])
            rocks[str(n1)] += v
            rocks[str(n2)] += v
            rocks[k] += -v
        else:
            n1 = int(k) * 2024
            rocks[str(n1)] += v
            rocks[k] += -v
print(sum(rocks.values()))

#test = {k:v for k, v in rocks.items() if v != 0}
# %% Thoughts
"""
Part 1 was nice and easy, but obviously was leading into a brute force problem
with part 2. I'm stumped on pt2 for now and I'll have to come back to it later
since this is a busy week and I can't give more time. The key is something about
finding cycles.
I originally wrote this dictionary approach, but I thought I needed to find
a cycle because it was still too slow. However, I realized I just had a bug
that was slowing it down and this dictionary approach is fast enough!
"""
