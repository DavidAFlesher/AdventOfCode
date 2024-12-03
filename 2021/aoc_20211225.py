# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:19:58 2024

@author: david
"""

# %% input

with open("input.txt", "r") as f:
    lines = [list(l.strip()) for l in f.readlines()]
# input is 139 by 137 row:column
array = lines

# %% Part 1


# East moves first, then South

# Function that checks if space is empty then rewites array
# I happen to loop through array in direction, so sequential movement isn't a
# problem for now

# If i were going to rewrite this, I would just keep a list of cucumbers that
# can move in any iteration then loop through that list and move them.
def migrate(direction, array):
    # direction = "east"
    herd = {"east": ">", "south": "v"}
    movement = False
    moved_pos = []
    new_empty = []
    for i, row in enumerate(array):
        for j, col in enumerate(row):
            curr_pos = [i, j]
            curr_herd = array[i][j]
            if direction == "east":
                mig_pos = [i, (j+1)%139]
            elif direction == "south":
                mig_pos = [(i+1)%137, j]
            # check if curr pos has already moved
            if curr_pos in moved_pos:
                # already moved
                pass
            # check if mig pos previously occupied
            elif mig_pos in new_empty:
                # wasn't orignally empty
                pass
            # check if moving that herd this iter
            elif not curr_herd == herd[direction]:
                # not moving
                pass
            # check if new pos empty
            elif array[mig_pos[0]][mig_pos[1]] == ".":
                # space is empty, good to move
                array[mig_pos[0]][mig_pos[1]] = herd[direction]
                # update array after move
                array[i][j] = "."
                # someone moved
                movement = True
                # add add to illegal move lists
                moved_pos.append(mig_pos)
                new_empty.append(curr_pos)
            else:
                pass
    return array, movement


iter_move = True
step = 0
while iter_move:
    array, east_move = migrate("east", array)
    array, south_move = migrate("south", array)
    step += 1
    if not east_move and not south_move:
        iter_move = False
        # no one has moved. done movign
print(step)


# %% Part 2

# huh, there is no pt 2
