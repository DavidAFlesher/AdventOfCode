# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 03:38:09 2022

@author: david
"""
# %%


with open("input.txt", "r") as f:
    lines = [line.strip('\n').split() for line in f.readlines()]
# %%

# insight is that if head and tail are not touching, the tail moves to the location
# the head was last at

def direction_translation(direction, head_pos):
    # updates the head position based on the direction in increments of one
    if direction == 'U':
        head_pos[1] += 1
    elif direction == 'R':
        head_pos[0] += 1
    elif direction == 'D':
        head_pos[1] += -1
    elif direction == 'L':
        head_pos[0] += -1
    return head_pos

def tail_touching_head(head_pos, tail_pos):
    # checks if tail is touching head
    x_diff = head_pos[0] - tail_pos[0]
    y_diff = head_pos[1] - tail_pos[1]
    if abs(x_diff) > 1 or abs(y_diff) > 1:
        # aka head isn't touching tail
        return False
    else:
        return True

# initial x, y coords for head and tail
head_pos = [0, 0]
tail_pos = [0, 0]
head_pos_history = [[0, 0]]
tail_pos_history = [[0, 0]]
for line in lines:
    direction, distance = line
    # update head position by direction in increments of one
    for i in range(int(distance)):
        head_pos = direction_translation(direction, head_pos)
        if not tail_touching_head(head_pos, tail_pos):
            # since tail wasn't touching, update to last head position
            tail_pos = head_pos_history[-1]
        head_pos_history.append(head_pos.copy())
        tail_pos_history.append(tail_pos.copy())

# get unique positions. Expensive, but idc
unique_tail_positions = []
for pos in tail_pos_history:
    if pos not in unique_tail_positions:
        unique_tail_positions.append(pos)
print(len(unique_tail_positions)) # 6175

# %%

# dang. insight doesn't work anymore. Oh well.
# for this new problem, the knot0 and knot1 follow the same path as the head
# and tail from last time. Start there.

def move_knot(previous_knot, current_knot):
    # if diagnonal diff, move diagonally, else cardinal translation
    new_coord = current_knot.copy()
    x_diff = previous_knot[0] - current_knot[0]
    y_diff = previous_knot[1] - current_knot[1]
    if abs(x_diff) > 1 and abs(y_diff) == 0:
        # x-axis translation
        new_coord[0] = int(current_knot[0] + x_diff/abs(x_diff)) # move 1 maintaining sign for direction
    elif abs(y_diff) > 1 and abs(x_diff) == 0:
        # y-axis translation
        new_coord[1] = int(current_knot[1] + y_diff/abs(y_diff)) # move 1 maintaining sign for direction
    else:
        # move diagnonally by 1, 1 in the direction of the differences
        new_coord[0] = int(current_knot[0] + x_diff/abs(x_diff))
        new_coord[1] = int(current_knot[1] + y_diff/abs(y_diff))
    return new_coord


knot_pos_histories = []
knot_positions = [[0, 0] for i in range(10)]
for knot_0, knot_1 in zip(head_pos_history, tail_pos_history):
    #new_knot_positions = [[0, 0] for i in range(10)]
    knot_positions[0] = knot_0
    knot_positions[1] = knot_1
    for i in range(2, len(knot_positions)):
        # compare knots after 2nd knot to the previous
        # knot to determine how to move
        if not tail_touching_head(knot_positions[i-1], knot_positions[i]):
            # not touching previous knot
            knot_positions[i] = move_knot(knot_positions[i-1], knot_positions[i])
    knot_pos_histories.append(knot_positions.copy())


# %%
unique_knot_9_positions = []
for knot in knot_pos_histories:
    if knot[9] not in unique_knot_9_positions:
        unique_knot_9_positions.append(knot[9])
print(len(unique_knot_9_positions)) # 2578

# %%
import matplotlib.pyplot as plt
import numpy as np

knot_9_unique_x_pos = [knot[0] for knot in unique_knot_9_positions]
knot_9_unique_y_pos = [knot[1] for knot in unique_knot_9_positions]
color = list(range(len(unique_knot_9_positions)))

# %%
fig, ax = plt.subplots(figsize=(9, 6), dpi=800)
plot = ax.scatter(knot_9_unique_x_pos, knot_9_unique_y_pos, s = 1, marker = '.', c = color)
ax.set_xlabel('x_coord')
ax.set_ylabel('y_coord')
plt.title('Unique Tail Positions in Order')

fig.colorbar(plot, ax = ax)
