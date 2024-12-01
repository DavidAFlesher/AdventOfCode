# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:56:43 2024

@author: david
"""

# %% Parse input

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

orgfish = list(map(int, lines[0].split(",")))

# %%

import numpy as np

fish = np.array(orgfish)

for i in range(80):
    fish += -1
    nf = np.where(fish == -1)
    fish[nf] = 6
    fish = np.append(fish, [8]*len(nf[0]))
    print(i+1, fish)

print(len(fish))


# %%

fishdict = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for f in orgfish:
    fishdict[f] += 1

for _ in range(256):
    nfishdict = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    for k, v in fishdict.items():
        if k == 0:
            nfishdict[8] += v
            nfishdict[6] += v
        else:
            nfishdict[k-1] += v
    fishdict = nfishdict
    #print(fishdict)

print(sum([v for v in fishdict.values()]))
