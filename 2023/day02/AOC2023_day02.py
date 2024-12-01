# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 22:47:58 2023

@author: david
"""

#%% Advent of Code 2023, Dec 02

with open("input.txt", "r") as f:
    lines = [line.strip('\n') for line in f.readlines()]

# %% part 1

# parse game results into list of lists, with n cubes like [red, green, blue]
parsed_record = []
for line in lines:
    game, results = line.split(":")
    record = [hand.split(",") for hand in results.split(";")]
    game_record = []
    for hand in record:
        hand_sum = [0, 0, 0] # red, green, blue
        for draw in hand:
            if "red" in draw:
                num, color = draw.strip().split(" ")
                hand_sum[0] = int(num)
            elif "green" in draw:
                num, color = draw.strip().split(" ")
                hand_sum[1] = int(num)
            elif "blue" in draw:
                num, color = draw.strip().split(" ")
                hand_sum[2] = int(num)
            else:
                raise ValueError("Impossible draw. Check input")
        game_record.append(hand_sum)
    parsed_record.append(game_record)


# bag of 12 red, 13 green, and 14 blue
max_bag = [12, 13, 14]
# look for impossible games, game IDs in order, index starts at 1
possible_game_IDs = set()
for i, game in enumerate(parsed_record):
    possible_game = True
    for hand in game:
        # get difference between the drawn hand and the hypothetical max draw
        # a negative number signifies pulling an impossible cube number
        cube_diff = [max_color - hand_color for hand_color, max_color in zip(hand, max_bag)]
        if min(cube_diff) < 0:
            possible_game = False
            break
    if possible_game:
        possible_game_IDs.add(i+1)

answer1 = sum(possible_game_IDs) # answer1: 3099

# %% part 2

power_record = []
for game in parsed_record:
    color_max = [max(color) for color in zip(*game)] # max pulled cube per color, rgb
    game_power = color_max[0]*color_max[1]*color_max[2]
    power_record.append(game_power)

answer2 = sum(power_record) # answer 2: 72970
