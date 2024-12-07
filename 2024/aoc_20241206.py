# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 23:55:08 2024

@author: david
"""
# %% Parse input

with open("demo_input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


import numpy as np
# I once again prefer using numpy array for a grid
grid = np.array([list(l) for l in lines])
# %% Parse input

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


import numpy as np
# I once again prefer using numpy array for a grid
grid = np.array([list(l) for l in lines])

# %% Part 1

# start row column
pos_r, pos_c = np.where(grid == "^")

# generate mask of where she has been
mask = np.zeros(grid.shape)
mask[pos_r, pos_c] = 1
# saw this online once. express vector as imaginary num allows rotate if mult by -1j
# r = real component, c = img component
_dir = -1 + 0j
# continue until walk off map
while True:
    dr, dc = _dir.real, _dir.imag
    nr, nc = int(pos_r + dr), int(pos_c + dc)
    if not ((0 <= nr < len(grid[:, 0])) and (0 <= nc < (len(grid[0, :])))):
        # out of bounds
        break
    elif grid[nr, nc] == "#":
        # not empty
        # rotate instead and restart
        _dir = _dir * -1j
    else:
        # empty. walk there and update mask
        pos_r, pos_c = nr, nc
        mask[pos_r, pos_c] = True
ans1 = len(np.where(mask == 1)[0])
print(ans1)
# %% Part 2

# just brute force try new obstacle in every pos
# if I ever end up at same pos facing same way, I know I'm in a loop
# so keep track of pos and direction

ans2 = 0
mask = np.zeros(grid.shape)
i = 0
for r in range(len(grid[:, 0])):
    for c in range(len(grid[0, :])):
        if grid[r, c] == ".":
            print(r, c)
            # not already an obs there
            ngrid = grid.copy()
            ngrid[r, c] = "#"
            #print(ngrid)
            #assert len(np.where(ngrid == "#")[0]) - len(np.where(grid == "#")[0]) == 1
            # reset
            pos_r, pos_c = np.where(grid == "^")
            _dir = -1 + 0j
            # this mask keeps a list of directions at each spot
            mask2 = [[[] for j in range(len(ngrid))] for i in range(len(ngrid))]
            mask2[int(pos_r)][int(pos_c)].append(_dir)
            i += 1
            #print(i, r, c)
            while True:
                dr, dc = _dir.real, _dir.imag
                nr, nc = int(pos_r + dr), int(pos_c + dc)
                mask[pos_r, pos_c] = 1
                if not ((0 <= nr < len(ngrid[:, 0])) and (0 <= nc < (len(ngrid[0, :])))):
                    # out of bounds
                    #print("Escaped")
                    mask[pos_r, pos_c] = -1
                    break
                elif ngrid[nr, nc] == "#":
                    # not empty
                    # rotate instead and restart
                    _dir = _dir * -1j
                    #print("turn")
                else:
                    if _dir in mask2[nr][nc]:
                        # already been there, aka in loop, break
                        #print(mask2[nr][nc], _dir)
                        ans2 += 1
                        #print("I have memory of this place")
                        break
                    else:
                        # new and empty. walk there and update mask
                        pos_r, pos_c = nr, nc
                        mask2[pos_r][pos_c].append(_dir)
                        ngrid[pos_r, pos_c] = "X"
                        #print(ngrid)
print(ans2)

# %% Thoughts
