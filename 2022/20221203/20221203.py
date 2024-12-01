# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:42:48 2022

@author: david
"""

with open("input.txt", "r") as f:
    lines = [line.strip('\n') for line in f.readlines()]

item_catalog = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


# %% Part1

duplicate_item = []
duplicate_item_priority = []
for line in lines:
    ind_split = int(len(line)/2)
    # sorted is red for speed
    compartment1 = sorted(line[:ind_split])
    compartment2 = sorted(line[ind_split:])
    # sniff for bad data
    assert len(compartment1) == len(compartment2)
    for item in compartment1:
        if item in compartment2:
            duplicate_item.append(item)
            # could do += but append to list easier troubleshooting
            duplicate_item_priority.append(item_catalog.index(item) + 1)
            # guaranteed only one duplicate item, so break
            break
print(sum(duplicate_item_priority))
# answer: 8176

# %% Part2

badge_item = []
badge_item_priority = []

# loop through items indicies by 3
for i in range(0, len(lines), 3):
    # bag stream to set to drop duplicates, the join to string again
    bag1 = ''.join(set(lines[i]))
    bag2 = ''.join(set(lines[i+1]))
    bag3 = ''.join(set(lines[i+2]))
    collective_group_items = sorted(bag1 + bag2 + bag3)
    for j in range(len(collective_group_items)-2):
        if collective_group_items[j] != collective_group_items[j+1]:
            pass
        elif collective_group_items[j] != collective_group_items[j+2]:
            pass
        else: # collective_group_items[i] matches next two indicies, aka is badge
            duplicate_item = collective_group_items[j]
            badge_item.append(duplicate_item)
            badge_item_priority.append(item_catalog.index(duplicate_item) + 1)
            break
print(sum(badge_item_priority))
# answer 2689
