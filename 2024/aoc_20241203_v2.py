# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 00:02:41 2024

@author: david
"""
"""
I wanted to write a solution that read the characters in, like a data stream
thing, and without regex, just as a fun exercise.
"""

# %% Parse input

with open("input.txt", "r") as f:
    lines = f.readlines()
    stream = "".join([*lines])

# %% Part 1

def mulCheck(i):
    # Check if mul(XXX,XXX)
    # return True if yes, and [X,Y]
    global stream
    if not stream[i:i+4] == "mul(":
        return False, None, None
    else:
        i += 4
        n = 0 # keep track of while cycles
        xstr = str()
        while stream[i].isdigit() and n < 3:
            xstr += stream[i]
            i += 1
            n += 1
        if not stream[i] == ",":
            return False, None, None
        else:
            i += 1
            n = 0
            ystr = str()
            while stream[i].isdigit() and n < 3:
                ystr += stream[i]
                i += 1
                n += 1
            if stream[i] == ")":
                try:
                    x = int(xstr)
                    y = int(ystr)
                    return True, x, y
                except ValueError:
                    # somehow appended not a digit
                    return False, None, None
            else:
                # bad end
                return False, None, None


# pad the stream for overhang
stream = stream + "Fill"*10
ans = 0
for i in range(len(stream)):
    m, x, y = mulCheck(i)
    if m:
        ans += x * y
print(ans)

# %% Part 2

def doCheck(i):
    # check if "do()" is next, return True if yes
    global stream
    if stream[i:i+4] == "do()":
        return True
    else:
        return False

def dontCheck(i):
    # check if "don't()" is next, return True if yes
    global stream
    if stream[i:i+7] == "don't()":
        return True
    else:
        return False


ans2 = 0
mul = True
for i in range(len(stream)):
    if doCheck(i):
        mul = True
    elif dontCheck(i):
        mul = False
    m, x, y = mulCheck(i)
    if m and mul:
        ans2 += x * y
print(ans2)
