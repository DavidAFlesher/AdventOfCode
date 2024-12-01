# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 02:33:29 2022

@author: david
"""
import numpy as np

with open("input.txt", "r") as f:
    lines = [line.strip('\n') for line in f.readlines()]

# %%
## Form the grid for the cave ##
coords = []
for line in lines:
    line_split = line.split(' -> ')
    rock_edges = []
    for coord in line_split:
        x, y = coord.split(',')
        x = int(x)
        y = int(y)
        rock_edges.append([x, y])
    for i in range(len(rock_edges)-1):
        xs = [rock_edges[i][0], rock_edges[i+1][0]]
        ys = [rock_edges[i][1], rock_edges[i+1][1]]
        if xs[0] == xs[1]:
            # y changes
            y_range = list(range(min(ys), max(ys)+1))
            for yy in y_range:
                coords.append([xs[0], yy])
        elif ys[0] == ys[1]:
            # x changes
            x_range = list(range(min(xs), max(xs)+1))
            for xx in x_range:
                coords.append([xx, ys[0]])

x_max = max([coord[0] for coord in coords])
x_min = min([coord[0] for coord in coords])
x_diff = x_max - x_min
y_max = max([coord[1] for coord in coords])
y_min = min([coord[1] for coord in coords])
y_diff = y_max - y_min

y_val = [coord[1] for coord in coords]
grid = np.zeros((x_diff+1, y_max+2)) # pad bottom by 1 for indicator
for x, y in coords:
    xx = x -x_min
    yy = y
    #print(xx, yy)
    grid[xx, yy] = 1
    grid[500-x_min, 0] = 10
    grid[:, -1] = -1
grid = np.transpose(grid)


# %%
# start is grid[0, 52]

def falling(x, y):
    # recursive function to determine the resting position when dropping a sand
    # from the input coordinates in the cave 'grid'
    global grid
    l1 = [grid[y-1, x-1], grid[y-1, x], grid[y-1, x+1]]
    l2 = [grid[y, x-1], grid[y, x], grid[y, x+1]]
    l3 = [grid[y+1, x-1], grid[y+1, x], grid[y+1, x+1]]
    local_grid = np.array([l1, l2, l3])
    if local_grid[2, 1] == 0:
        # empty below, continue falling
        newx, newy = falling(x, y+1)
        return newx, newy
    elif local_grid[2, 0] == 0:
        # empty bottom left, fall there
        newx, newy = falling(x-1, y+1)
        return newx, newy
    elif local_grid[2, 2] == 0:
        # empty bottom right, fall there
        newx, newy = falling(x+1, y+1)
        return newx, newy
    elif local_grid[2, 1] == -1:
        # false bottom, falling off the ground, return default value
        return 0, 0
    else:
        # on solid ground below. stay put
        return x, y
# %%

# input falls from 52, 1
new_sand_pos = []
for i in range(1000):
    tx, ty = falling(52, 1)
    if (tx == 0) and (ty == 0):
        # default value, so falling off edge
        break
    new_sand_pos.append([tx, ty])
    grid[ty, tx] = 2
print(len(new_sand_pos)) # answer: 692

# save for pretty visualizations
# np.savetxt('part1_filled.csv', grid, delimiter=',', fmt = '%i')

# %% Part 2

# pad the previous grid by 500 to leave plenty of room
pad = 500
halfpad = pad//2
grid2 = np.zeros((x_diff+1+pad, y_max+4)) # pad bottom for floor and ceiling
for x, y in coords:
    xx = x -x_min + halfpad # add 250 to center after padding
    yy = y+1
    grid2[xx, yy] = 1
    grid2[500-x_min+halfpad, 1] = 10 #sand inlet
    grid2[:, -1] = 1

grid2 = np.transpose(grid2)
np.savetxt('part2_empty.csv', grid2, delimiter=',', fmt = '%i')

def falling2(x, y):
    # recursive function to determine the resting position when dropping a sand
    # from the input coordinates in the cave 'grid'. Edited for part2
    global grid2
    l1 = [grid2[y-1, x-1], grid2[y-1, x], grid2[y-1, x+1]]
    l2 = [grid2[y, x-1], grid2[y, x], grid2[y, x+1]]
    l3 = [grid2[y+1, x-1], grid2[y+1, x], grid2[y+1, x+1]]
    local_grid2 = np.array([l1, l2, l3])
    if local_grid2[2, 1] == 0:
        # empty below, continue falling
        newx, newy = falling2(x, y+1)
        return newx, newy
    elif local_grid2[2, 0] == 0:
        # empty bottom left, fall there
        newx, newy = falling2(x-1, y+1)
        return newx, newy
    elif local_grid2[2, 2] == 0:
        # empty bottom right, fall there
        newx, newy = falling2(x+1, y+1)
        return newx, newy
    else:
        # on solid ground below. stay put
        return x, y
# %%
# input falls from 302, 1 when padded
new_sand_pos_part2 = []
for i in range(100**10):
    tx, ty = falling2(302, 1)
    if (tx == 302) and (ty == 1):
        # inlet is filled
        new_sand_pos_part2.append([tx, ty])
        grid2[ty, tx] = 2
        break
    new_sand_pos_part2.append([tx, ty])
    grid2[ty, tx] = 2
print(len(new_sand_pos_part2)) # Answer: 31706

# save for pretty visualizations
# np.savetxt('part2_filled.csv', grid2, delimiter=',', fmt = '%i')
