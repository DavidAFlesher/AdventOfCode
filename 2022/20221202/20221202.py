# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 01:30:07 2022

@author: david
"""

with open("input.txt", "r") as f:
    lines = [line.strip('\n').split(" ") for line in f.readlines()]

# %%

convert_dict = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

def outcome(you, me, convert_dict):
    ## return the score of the match
    if you == "A" and me == "Y":
        # your rock loses to my paper
        return 6 + convert_dict[me]
    elif you == "A" and me == "Z":
        # your rock beats my scissors
        return convert_dict[me]
    elif you == "B" and me == "X":
        # your paper beats my rock
        return convert_dict[me]
    elif you == "B" and me == "Z":
        # your paper loses to my scissors
        return 6 + convert_dict[me]
    elif you == "C" and me == "X":
        # your scissors loses to my rock
        return 6 + convert_dict[me]
    elif you == "C" and me == "Y":
        # your scissors beats my paper
        return convert_dict[me]
    else:
        # tie
        return 3 + convert_dict[me]
# %% Part 1

round_outcome = []
for line in lines:
    round_outcome.append(outcome(*line, convert_dict))

print(sum(round_outcome))

# %% Part 2

def outcome_2(you, me):
    if me == "X":
        # I lose options
        if you == "A":
            return 3
        elif you == "B":
            return 1
        elif you == "C":
            return 2
    elif me == "Y":
        # I draw options
        if you == "A":
            return 3 + 1
        elif you == "B":
            return 3 + 2
        elif you == "C":
            return 3 + 3
    elif me == "Z":
        # I win options
        if you == "A":
            return 6 + 2
        elif you == "B":
            return 6 + 3
        elif you == "C":
            return 6 + 1

round_outcome_2 = []
for line in lines:
    round_outcome_2.append(outcome_2(*line))

print(sum(round_outcome_2))
