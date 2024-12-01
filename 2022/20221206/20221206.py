# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 00:03:08 2022

@author: david
"""


with open("input.txt", "r") as f:
    datastream = f.read()

# %% Test1
# datastream len 4096

for i in range(4096-4):
    chunk = datastream[i:i+4]
    chunk_set = set(chunk)
    if len(chunk_set) == 4:
        print(f'{i} : {chunk}')
        break
# i = 1138 so pos 1138+4

# %% Test2

for i in range(4096-14):
    chunk = datastream[i:i+14]
    chunk_set = set(chunk)
    if len(chunk_set) == 14:
        print(f'{i} : {chunk}')
        break
# i = 2789 so pos 2789+14


# %% one line attempt

# Test1
print([i for i in range(4096-4) if len(set(datastream[i:i+4])) == 4][0]+4)
# Test2
print([i for i in range(4096-14) if len(set(datastream[i:i+14])) == 14][0]+14)
