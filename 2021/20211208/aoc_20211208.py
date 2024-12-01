# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 01:39:44 2024

@author: david
"""
# %% Parse input

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

inp = []
out = []
for line in lines:
    i, o = line.split("|")
    inp.append(sorted([set(sorted(st)) for st in i.split()]))
    out.append(sorted([set(sorted(st)) for st in o.split()]))

# %% Part 1

# dig:len  1:2, 4:4, 7:3, 8:7

unique_len = [2, 4, 3, 7]
ans = 0
for o in out:
    for st in o:
        if len(st) in unique_len:
            ans += 1
print(ans)

# %% Part 2

solve = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g'}

i = sorted(inp[0], key = len)

one = i[0]
four = i[2]
seven = i[1]
eight = i[9]

two = set()
three =
five =

six =
nine =
zero =

for n in [6, 7, 8]:
    test = (four | seven) ^ i[n]
    if len(test) == 1:
        nine = i[n]



solve["1"] = one ^ seven
solve["2"] = four - one
solve["3"] =
solve["4"] = four - one # eight - zero
solve["5"] = eight - nine
solve["6"] =
solve["7"] =

t1 = (four | seven) ^ i[6] #
t2 = (four | seven) ^ i[7] # 9 len 1 if i[7] 9
t3 = (four | seven) ^ i[8]

t4 = one - i[8] # len 1 if i[8] == six
