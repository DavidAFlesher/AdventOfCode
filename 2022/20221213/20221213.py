# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:16:48 2022

@author: david
"""


with open("input.txt", "r") as f:
    pairs = [[eval(pair[0]), eval(pair[1])] for pair in [x.split('\n') for x in f.read().split('\n\n')]]

# %%
def recursive(left, right):
    comp = None
    for l, r in zip(left, right):
        # loop through without resolution. If finish the loop, resolve mismatch length
        if isinstance(l, int) and isinstance(r, int):
            # both are ints, easy comparision
            if l == r:
                # equal val, continue comparision
                pass
            elif l < r:
                # left is smaller, correct order
                comp = True
            elif r < l:
                # right is smaller, incorrect order
                comp = False
        elif isinstance(l, list) and isinstance(r, list):
            # both are lists, so you can list compare
            comp = recursive(l, r)
        elif isinstance(l, list) and isinstance(r, int):
            # reset to list and do comparison
            comp = recursive(l, [r])
        elif isinstance(l, int) and isinstance(r, list):
            # reset to list and do comparison
            comp = recursive([l], r)
        if not comp == None:
            # decision reached
            break
    if comp == None:
        # resolve mismatch length
        if len(left) < len(right):
            # left is shorter, correct order
            comp = True
        elif len(right) < len(left):
            # right is shorter, incorrect order
            comp = False
        else:
            # equivalent pairs so far
            pass
    return comp



# %% Part 1
full_list = []
correct_indicies = []
for i, pair in enumerate(pairs):
    left = pair[0]
    right = pair[1]
    full_list.append(recursive(left, right))
correct_indicies = [i+1 for i, x in enumerate(full_list) if x == True]
print(sum(correct_indicies)) # 5720

# %% Part 2

packets = []
for pair in pairs:
    packets.append(pair[0])
    packets.append(pair[1])

# just sort relative to the divider packets and get index
# aint got no compute for actually sorting
div_1_index = 1
div_2_index = 2
for i, packet in enumerate(packets):
    # start with smaller divider
    comp = recursive(packet, [[2]])
    if comp:
        # other packet smaller than both dividers
        div_1_index += 1
        div_2_index += 1
    else:
        # try the bigger divider
        comp = recursive(packet, [[6]])
        if comp:
            # other packet smaller than 2nd divider
            div_2_index += 1
print(div_1_index*div_2_index) # 23504
