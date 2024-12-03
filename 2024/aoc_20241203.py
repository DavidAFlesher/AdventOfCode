# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 00:02:41 2024

@author: david
"""
"""
I didn't know any regex so I wrote a hacky solution at first. Then, I looked up
some regex documentation and wrote a much better regex solution at the bottom.
"""


# %% Parse input

with open("input.txt", "r") as f:
    lines = f.readlines()
    data = "".join([*lines])

# %% Part 1

filter1 = data.split("mul")
# Now, filter out where parenthesis don't immediately follow 'mul'
# Also, set up for exctacting the (X,Y) parenthesis pattern
filter2 = [f.split(")")[0][1:] for f in filter1 if f[0] == "("]
# Filter out if there is a space, even though it looks like there aren't any
filter3 = [f.split(",") for f in filter2 if " " not in f]
# Make sure I should only have two values now, the X and Y
filter4 = [f for f in filter3 if len(f) == 2]


ans = 0
for t in test4:
    try:
        # if they are just numbers, aka valid X and Y, this will work
        x = int(t[0])
        y = int(t[1])
        ans += x * y
    except ValueError:
        # not a number. pass
        pass
print(ans)

# %% Part 2

# my hacky solution to Part 1 doesn't fit part 2 at all. Should have just
# learned regex

# since I split on mul, a do or don't always affects next mul
# lets make a mask to tell us to include the mul or not
mul_list = [True] * len(test)
for i, s in enumerate(test):
    pass
    assert not ("do()" in s and "don't()" in s)
    if "do()" in s:
        # all following are True until a don't is found
        mul_list[i+1:] = [True for _ in mul_list[i+1:]]
    elif "don't()" in s:
        # all following are False until a do is found
        mul_list[i+1:] = [False for _ in mul_list[i+1:]]

# reproduce my filters in Part 1, but also filtering out the mul mask
f2 = []
m2 = []
for s, m in zip(filter1, mul_list):
    if s[0] == "(":
        f2.append(s.split(")")[0][1:])
        m2.append(m)

f3 = []
m3 = []
for s, m in zip(f2, m2):
    if " " not in s:
        f3.append(s.split(","))
        m3.append(m)

f4 = []
m4 = []
for s, m in zip(f3, m3):
    if len(s) == 2:
        f4.append(s)
        m4.append(m)

ans2 = 0
for s, m in zip(f4, m4):
    try:
        x = int(s[0])
        y = int(s[1])
        if m:
            ans2 += x * y
    except ValueError:
        pass
print(ans2)

# %% Thoughts

"""
When I saw the problem, I knew that putting off learning regex was finally catching
up to me. But, for time, I wasn't sure if making a hacky solution would be faster
than learning regex.
"""

# %% REGEX soultion
"""
I decided I should learn some regex. It wasn't that bad. I guess I'm used to seeing
really complicated regex. Turns out learning regex for this would have been faster
that making my hacky solution, haha. If I had the time, I could probably improve the
below, but good enough.
"""

import re

ans1 = 0
vals = re.findall('mul\(\d{1,3},\d{1,3}\)',data)
for v in vals:
    x, y = re.findall("\d{1,3}", v)
    ans1 += int(x) * int(y)
print(ans1)

ans2 = 0
vals = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", data)
mul = True
for v in vals:
    if v[0:3] == "mul" and mul:
        x, y = re.findall("\d{1,3}", v)
        ans2 += int(x) * int(y)
    else:
        mul = True if v == "do()" else False
print(ans2)
