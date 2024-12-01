# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:46:18 2023

@author: david
"""

#%% Advent of Code 2023, Dec 01

with open("input.txt", "r") as f:
    lines = [line.strip('\n') for line in f.readlines()]

#%% part 1

calibration_vals = []
for line in lines:
    nums = [num for num in line if num.isnumeric()]
    calibration_val = int(nums[0] + nums[-1])
    calibration_vals.append(calibration_val)

total_sum = sum(calibration_vals) # answer 1: 54940
print(total_sum)

# %% part 2

digit_strings = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

# TODO: replace the find and rfind to extract only the first and last digits
calibration_vals = []
for line in lines:
    found_digits = []
    for key, val in digit_strings.items():
        ind = line.find(key)
        if ind != -1:
            found_digits.append([ind, key, val])
        ind = line.rfind(key) # sloppy way to find last instance, will add duplicates
        if ind != -1:
            found_digits.append([ind, key, val])
    found_digits.sort(key=lambda x: x[0])
    calibration_val = str(found_digits[0][-1]) + str(found_digits[-1][-1])
    calibration_vals.append(int(calibration_val))

total_sum = sum(calibration_vals) # answer 2: 54208
print(total_sum)
