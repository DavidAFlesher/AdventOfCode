# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:34:09 2023

@author: david
"""

#%% Advent of Code 2023, Dec 03

import numpy as np

with open("input.txt", "r") as f:
    lines = [[x for x in line.strip('\n')] for line in f.readlines()]

# add border ot schematic to handle edge cases
schematic = np.full((len(lines)+2, len(lines[0])+2), ".")
schematic[1:-1, 1:-1] = np.array(lines)
borderless_schematic = np.array(lines)

# %% Part 1
period_mask = (schematic == ".")
number_mask = np.invert(np.char.isnumeric(schematic))
# You could fine the symbols based on in "str", but this protects against
# Weird symbols that aren't period or a number
symbol_mask = np.invert(np.logical_xor(period_mask, number_mask))

# Look around border of all numbers by shifting the symbol mask to look for overlap
n = np.logical_or(number_mask[1:-1, 1:-1], symbol_mask[2:, 1:-1])
e = np.logical_or(number_mask[1:-1, 1:-1], symbol_mask[1:-1, :-2])
s = np.logical_or(number_mask[1:-1, 1:-1], symbol_mask[:-2, 1:-1])
w = np.logical_or(number_mask[1:-1, 1:-1], symbol_mask[1:-1, 2:])
ne = np.logical_or(number_mask[1:-1, 1:-1], symbol_mask[2:, :-2])
se = np.logical_or(number_mask[1:-1, 1:-1], symbol_mask[:-2, :-2])
sw = np.logical_or(number_mask[1:-1, 1:-1], symbol_mask[:-2, 2:])
nw = np.logical_or(number_mask[1:-1, 1:-1], symbol_mask[2:, 2:])
touch_nums = n * e * s * w * ne * se * sw * nw # combine all masks
touch_nums_flat = np.invert(touch_nums).flatten() # flatten and have legal numbers True

legal_num = []
number_buffer = []
for bool_check, number in zip(touch_nums_flat, borderless_schematic.flatten()):
    if bool_check:
        legal_buffer = True
    if number.isnumeric():
        #print(i, j)
        number_buffer.append(number)
    elif len(number_buffer) > 0:
        buff_num = int("".join(number_buffer))
        if legal_buffer:
            legal_num.append(buff_num)
        number_buffer = []
        legal_buffer = False

print(sum(legal_num)) # Answer part 1: 546563

# %% Part 2

# I'm just going to brute force this one. Can't think of anything clever.

gear_mask = np.invert(schematic == "*")
n = np.logical_or(number_mask[1:-1, 1:-1], gear_mask[2:, 1:-1])
e = np.logical_or(number_mask[1:-1, 1:-1], gear_mask[1:-1, :-2])
s = np.logical_or(number_mask[1:-1, 1:-1], gear_mask[:-2, 1:-1])
w = np.logical_or(number_mask[1:-1, 1:-1], gear_mask[1:-1, 2:])
ne = np.logical_or(number_mask[1:-1, 1:-1], gear_mask[2:, :-2])
se = np.logical_or(number_mask[1:-1, 1:-1], gear_mask[:-2, :-2])
sw = np.logical_or(number_mask[1:-1, 1:-1], gear_mask[:-2, 2:])
nw = np.logical_or(number_mask[1:-1, 1:-1], gear_mask[2:, 2:])
gear_touch = np.invert(n * e * s * w * ne * se * sw * nw)
gear_touch_bordered = np.full((len(gear_touch)+2, len(gear_touch)+2), False)
gear_touch_bordered[1:-1, 1:-1] = gear_touch


def check4gear(ni, nj, gear_touch_bordered):
    # look around the "*" gear for numbers the gear touches
    relative_touch_coord = []
    ni = int(ni)
    nj = int(nj)
    if gear_touch_bordered[ni+1, nj]:
        relative_touch_coord.append([1, 0])
    if gear_touch_bordered[ni-1, nj]:
        relative_touch_coord.append([-1, 0])
    if gear_touch_bordered[ni, nj+1]:
        relative_touch_coord.append([0, 1])
    if gear_touch_bordered[ni, nj-1]:
        relative_touch_coord.append([0, -1])
    if gear_touch_bordered[ni+1, nj+1]:
        relative_touch_coord.append([1, 1])
    if gear_touch_bordered[ni+1, nj-1]:
        relative_touch_coord.append([1, -1])
    if gear_touch_bordered[ni-1, nj+1]:
        relative_touch_coord.append([-1, 1])
    if gear_touch_bordered[ni-1, nj-1]:
        relative_touch_coord.append([-1, -1])
    return relative_touch_coord

def get_digit(ni, nj, schematic):
    # staring with one digit, find the complete number via recursive search
    # left align then pull digits left to right
    ni = int(ni)
    nj = int(nj)
    digit_buffer = []
    while schematic[ni, nj-1].isnumeric():
        nj -= 1
        # break out when [ni-1, nj] is not the digit, aka left aligned
    while schematic[ni, nj].isnumeric(): # scan digits left2right
        digit_buffer.append(schematic[ni, nj])
        nj += 1
        # break out when finished finding digit
    buff_num = int("".join(digit_buffer))
    return buff_num


# try assuming no gear touches 3 parts, only 1 or 2
gear_ratios = []
dual_gear_loc = []
for i in range(1, len(schematic)-1):
    for j in range(1, len(schematic)-1):
        number_buffer = []
        if gear_mask[i, j]:
            pass
        elif len(check4gear(i, j, gear_touch_bordered)) < 2:
            #print("mono", i, j)
            pass
        else: #gear good
            dual_gear_loc.append([i, j])
            temp = [i, j]
            touch_coord = check4gear(i, j, gear_touch_bordered)
            buff_numbers = []
            for x, y in touch_coord:
                buff_numbers.append(get_digit(i+x, j+y, schematic))
            gear_numbers = list(set(buff_numbers))
            assert len(gear_numbers) <= 2
            if len(gear_numbers) == 2:
                gear_ratio = np.prod(gear_numbers)
                gear_ratios.append(gear_ratio)

print(sum(gear_ratios))

# %% Part 2

# I'm just going to brute force this one. Can't think of any clever matrix manipulation.

gear_mask = np.invert(schematic == "*")

def check4gear(ni, nj, schematic):
    # look around the "*" gear for numbers the gear touches, record relative coord
    relative_touch_coord = []
    ni = int(ni)
    nj = int(nj)
    if schematic[ni+1, nj].isnumeric():
        relative_touch_coord.append([1, 0])
    if schematic[ni-1, nj].isnumeric():
        relative_touch_coord.append([-1, 0])
    if schematic[ni, nj+1].isnumeric():
        relative_touch_coord.append([0, 1])
    if schematic[ni, nj-1].isnumeric():
        relative_touch_coord.append([0, -1])
    if schematic[ni+1, nj+1].isnumeric():
        relative_touch_coord.append([1, 1])
    if schematic[ni+1, nj-1].isnumeric():
        relative_touch_coord.append([1, -1])
    if schematic[ni-1, nj+1].isnumeric():
        relative_touch_coord.append([-1, 1])
    if schematic[ni-1, nj-1].isnumeric():
        relative_touch_coord.append([-1, -1])
    return relative_touch_coord

def get_digit(ni, nj, schematic):
    # staring with one digit, find the complete number via while loops
    # left align then pull digits left to right
    ni = int(ni)
    nj = int(nj)
    digit_buffer = []
    while schematic[ni, nj-1].isnumeric():
        nj -= 1
        # break out when [ni-1, nj] is not the digit, aka left aligned
    while schematic[ni, nj].isnumeric(): # scan digits left2right
        digit_buffer.append(schematic[ni, nj])
        nj += 1
        # break out when finished recordign complete digit
    buff_num = int("".join(digit_buffer))
    return buff_num

# try assuming no gear touches 3 parts, only 1 or 2
gear_ratios = []
for i in range(1, len(schematic)-1):
    for j in range(1, len(schematic)-1):
        number_buffer = []
        if gear_mask[i, j]:
            pass
        elif len(check4gear(i, j, schematic)) < 2:
            #print("mono", i, j)
            pass
        else: #gear good
            dual_gear_loc.append([i, j])
            temp = [i, j]
            touch_coord = check4gear(i, j, schematic)
            buff_numbers = []
            for x, y in touch_coord:
                buff_numbers.append(get_digit(i+x, j+y, schematic))
            gear_numbers = list(set(buff_numbers)) # remove gear touching same number n>1
            assert len(gear_numbers) <= 2 # sniff if input has gear touching 3 numbers
            if len(gear_numbers) == 2:
                gear_ratio = np.prod(gear_numbers)
                gear_ratios.append(gear_ratio)

print(sum(gear_ratios)) # Answer 2: 91031374
