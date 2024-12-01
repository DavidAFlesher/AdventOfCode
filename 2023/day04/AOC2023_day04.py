# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 00:49:54 2023

@author: david
"""

# %%

with open("input.txt", "r") as f:
    lines = [line.strip('\n') for line in f.readlines()]

# %% Part 1

# Look for my numbers in winner numbers. Value = 2**n(winners-1)

# parse
cards = []
for line in lines:
    card_id, digits = line.split(":")
    winners, mine = digits.split("|")
    winners = [int(num) for num in winners.split()]
    mine = [int(num) for num in mine.split()]
    cards.append([winners, mine])

# get value per card
values = []
for winners, mine in cards:
    wins = 0
    for num in mine:
        if num in winners:
            wins += 1
    value = int(2**(wins-1)) # int to round down
    values.append(value)

print(int(sum(values))) # Answer 1: 23673

# %% Part 2

# Number of wins gives 1 copy of card[i+1:i+n(wins)+1]
# How many scratch cards did you use?

card_copies = [1] * len(cards) # start with one copy of each card
for i, (winners, mine) in enumerate(cards):
    wins = 0
    for num in mine:
        if num in winners:
            wins += 1
    # for each copy of the current card, add that many to subsequent cards
    n_current_card = card_copies[i]
    for j in range(i+1, i+wins+1): # if no winners, doesn't iterate
        card_copies[j] += n_current_card # add to existing card copy counter

print(sum(card_copies)) # Answer 2: 12263631
