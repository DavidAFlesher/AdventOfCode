# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 23:18:21 2022

@author: david
"""
# %%

import numpy as np

with open("input.txt", "r") as f:
    lines = [list(line.strip('\n')) for line in f.readlines()]
grid = np.array(lines)
# %%

# Loop through every tree, adding 1 to the visibility score if there is a taller
# tree in each of the cardinal directions

visibility_score = np.zeros(99*99).reshape(99,99)

for i in range(1, 98):
    for j in range(1, 98):
        vis_score = 0

        tree_height = grid[i, j]
        up_heights = grid[:i, j]
        right_heights = grid[i, j+1:]
        down_heights = grid[i+1:, j]
        left_heights = grid[i, :j]

        if max(up_heights) >= tree_height:
            vis_score += 1
        if max(right_heights) >= tree_height:
            vis_score += 1
        if max(down_heights) >= tree_height:
            vis_score += 1
        if max(left_heights) >= tree_height:
            vis_score += 1

        if vis_score == 4: # more elegent to skip this if check, but idc
            visibility_score[i][j] = 1

hidden_trees = np.where(visibility_score)
total_hidden_trees = np.sum(visibility_score) # 8098
total_visible_trees = 99*99 - total_hidden_trees # 1703
# %%

scenic_scores = np.zeros(99*99).reshape(99,99)

def counter(tree_list, tree_height):
    # compared to a list, if the comparison tree is smaller then inspected tree
    # add a counter and continue until finding a taller tree then stop, returning
    # scenic score in that direction
    counter = 0
    for tree in tree_list:
        if tree < tree_height:
            #print(tree_height, tree)
            counter += 1
            pass
        else:
            counter += 1
            break
    return counter

for i in range(1, 98): # edge trees always have 0 scenic score so ignore
    for j in range(1, 98):
        #i = 62
        #j = 64
        #i = 1
        #j = 1
        tree_height = grid[i, j]
        up_heights = grid[:i, j]
        right_heights = grid[i, j+1:]
        down_heights = grid[i+1:, j]
        left_heights = grid[i, :j]

        scenic_score = [] # get scenic score using function in each direction
        scenic_score.append(counter(np.flip(up_heights), tree_height))
        scenic_score.append(counter(right_heights, tree_height))
        scenic_score.append(counter(down_heights, tree_height))
        scenic_score.append(counter(np.flip(left_heights), tree_height))
        scenic_scores[i, j] = np.prod(scenic_score)

max_scenic_tree = np.max(scenic_scores) # 8736 too low
print(max_scenic_tree) # 496650
