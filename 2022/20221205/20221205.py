# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 01:10:33 2022

@author: david
"""

stacks = dict()
stacks['1'] = ['D', 'H', 'R', 'Z', 'S', 'P', 'W', 'Q']
stacks['2'] = ['F', 'H', 'Q', 'W', 'R', 'B', 'V']
stacks['3'] = ['H', 'S', 'V', 'C']
stacks['4'] = ['G', 'F', 'H']
stacks['5'] = ['Z', 'B', 'J', 'G', 'P']
stacks['6'] = ['L', 'F', 'W', 'H', 'J', 'T', 'Q']
stacks['7'] = ['N', 'J', 'V', 'L', 'D', 'W', 'T', 'Z']
stacks['8'] = ['F', 'H', 'G', 'J', 'C', 'Z', 'T', 'D']
stacks['9'] = ['H', 'B', 'M', 'V', 'P', 'W']


with open("input_parsed.txt", "r") as f:
    protocol = f.readlines()
    protocol = [line.strip("\n") for line in protocol]
    protocol_parsed = [l.split(" ")[1::2] for l in protocol]


# %%

def interpreter_9000(stacks, i, j, k):
    mover = stacks[j][:int(i)]
    stacks[j] =  stacks[j][int(i):]
    destination = mover[::-1] + stacks[k]
    stacks[k] = destination
    return None


# %%

stacks_9000 = stacks.copy()
for step in protocol_parsed:
    interpreter_9000(stacks_9000, *step)

# %%

## PART 2

def interpreter_9001(stacks, i, j, k):
    mover = stacks[j][:int(i)]
    stacks[j] =  stacks[j][int(i):]
    destination = mover + stacks[k]
    stacks[k] = destination
    return None


stacks_9001 = stacks.copy()
for step in protocol_parsed:
    interpreter_9001(stacks_9001, *step)

# %%

# tests
# 56 total crates to start
for k, v in stacks_9000.items():
    print(len(v))

for k, v in stacks_9001.items():
    print(len(v))

# %%

with open("input.txt", "r") as f:
    test = f.readlines()

test[:15]
