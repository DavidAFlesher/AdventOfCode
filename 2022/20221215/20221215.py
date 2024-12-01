# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 05:15:35 2022

@author: david
"""

with open("input.txt", "r") as f:
    lines = [line.strip('\n') for line in f.readlines()]


with open("example.txt", "r") as f:
    exlines = [line.strip('\n') for line in f.readlines()]

# %%

xsensors = []
ysensors = []
distances = []
xbeacons = []
ybeacons = []
x_signals = []
y_ind_inspect = 2000000 # 2000000

for line in lines:
    words = line.split()
    # s = sensor, b = beacon
    sx = int(words[2].split('=')[-1][:-1]) # drop the trailing comma
    sy = int(words[3].split('=')[-1][:-1]) # drop the trailing colon
    bx = int(words[-2].split('=')[-1][:-1]) # drop the trailing comma
    by = int(words[-1].split('=')[-1])
    xsensors.append(sx)
    ysensors.append(sy)
    xbeacons.append(bx)
    ybeacons.append(by)
    dx = abs(sx-bx)
    dy = abs(sy-by)
    distance = dx + dy
    distances.append(distance)
    x_min, x_max = sx-distance, sx+distance
    y_min, y_max = sy-distance, sy+distance
    if y_min < y_ind_inspect < y_max:
        print('beacon is lit')
        if sy < y_ind_inspect:
            pass
            y2br = y_max - y_ind_inspect
            x_signal = list(range(sx-y2br, sx+y2br+1))
        elif sy > y_ind_inspect:
            y2br = y_ind_inspect - y_min
            x_signal = list(range(sx-y2br, sx+y2br+1))
            pass
        else:
            print('oof')
            x_signal = list(range(x_min, x_max+1))
        x_signals.append(x_signal)

# %%
beacons = [[x, y] for x, y in zip(xbeacons, ybeacons)]
x_coord_max = max(xsensors + xbeacons)
x_coord_min = min(xsensors + xbeacons)
y_x = set()
for signal in x_signals:
    for x_coord in signal:
        if [x_coord, y_ind_inspect] in beacons:
            # don't pass when it is a beacon or sensor already there
            print(f'{x_coord}')
            pass
        else:
            y_x.add(x_coord)

print(len(y_x)) #4560025

# %% Part 2

# really slow, probably move the prune loop to a function and call as I find
# every possible x,y coord rather than repeating the loop

possible_coord = set()
for sx, sy, d in zip(xsensors, ysensors, distances):
    # get the edges of the area, manually adding the top and bottom
    print(f'sensor {sx, sy}:')
    x_min, x_max = sx-d, sx+d
    y_min, y_max = sy-d, sy+d
    possible_coord.add((sx, y_min-1))
    possible_coord.add((sx, y_max+1))
    for y_ind in range(y_min, y_max+1):
        if sy < y_ind:
            y2br = y_max - y_ind
            possible_coord.add((sx-y2br-1, y_ind))
            possible_coord.add((sx-y2br+1, y_ind))
        elif sy > y_ind:
            y2br = y_ind - y_min
            possible_coord.add((sx-y2br-1, y_ind))
            possible_coord.add((sx-y2br+1, y_ind))
        else:
            assert y_ind == sy
            possible_coord.add((x_min-1, y_ind))
            possible_coord.add((x_max+1, y_ind))
    # prune possible coords to only remove coords outside the 4e6 range
    # and coords that are closer to the current sensor beacon pair
    print(f'    pre_prune = {len(possible_coord)}')
    pruned_coords = set()
    for x, y in possible_coord:
        if not ((0 <= x <= 4000000) and (0 <= y <= 4000000)):
            # not within the 4e6 range
            pass
        else:
            add_coord = True
            for sx2, sy2, d2 in zip(xsensors, ysensors, distances):
                d2sensor = abs(sx2-x) + abs(sy2-y)
                if d2sensor <= d2:
                    # coord is closer to another sensor than it's beacon, aka
                    # the coord is in that sensor's 'exclusion' range, so mark
                    # this coord to be excluded
                    add_coord = False
            if add_coord:
                pruned_coords.add((x, y))
    possible_coord = pruned_coords
    print(f'    post_prune = {len(possible_coord)}')
possible_coord = list(possible_coord)
print(possible_coord[0][0] * 4000000 + possible_coord[0][1])
