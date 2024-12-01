# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 23:52:13 2024

@author: david
"""

# %% Parse input

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]

# %% Part 1

# Get gamma by transposing and counting 0/1 then max
# epsilon is opposite gamma
# answer is gamma * epsilon

tran_lines = list(zip(*lines)) # transpose array

gamma = []
epsilon = []
for tline in tran_lines:
    count0 = tline.count("0")
    count1 = tline.count("1")
    if count0 > count1:
        gamma.append('0')
        epsilon.append('1')
    elif count1 > count0:
        gamma.append('1')
        epsilon.append('0')
    else:
        raise ValueError("Equal number bits")

gamma_b = "".join(gamma)
epsilon_b = "".join(epsilon)

gamma_int = int(gamma_b, 2)
epsilon_int = int(epsilon_b, 2)

print(gamma_int * epsilon_int)

# %% Part 2

# oxygen generator rating
# -most common value, 1 wins ties

# CO2 scrubber rating
# - least common value 0 wins ties

oxy = lines
ind = 0
while len(oxy) > 1:
    toxy = list(zip(*oxy))
    count0 = toxy[ind].count("0")
    count1 = toxy[ind].count("1")

    if count0 > count1:
        oxy = [line for line in oxy if line[ind] == "0"]
    elif count1 >= count0:
        oxy = [line for line in oxy if line[ind] == "1"]
    ind += 1

oxy_int = int("".join(oxy[0]), 2)

co2 = lines
ind = 0
while len(co2) > 1:
    tco2 = list(zip(*co2))
    count0 = tco2[ind].count("0")
    count1 = tco2[ind].count("1")

    if count0 <= count1:
        co2 = [line for line in co2 if line[ind] == "0"]
    elif count1 < count0:
        co2 = [line for line in co2 if line[ind] == "1"]
    ind += 1

co2_int = int("".join(co2[0]), 2)

print(oxy_int * co2_int)
