# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 23:59:21 2024

@author: david
"""
# %% Parse input

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# hard code the split between page ordering and pages to produce at row 1176
orders = [list(map(int, l.split("|"))) for l in lines[:1176]]
prints = [list(map(int, l.split(","))) for l in lines[1177:]]

# %% Part 1

# generate order to dictionary/hashmap
# Key = page number, val = list of pages it comes before
ord_dict = dict()
for x, y in orders:
    try:
        ord_dict[x].append(y)
    except KeyError:
        ord_dict[x] = [y]

# correct edge case where last print in y column produces a KeyError
for x, y in orders:
    if y not in ord_dict.keys():
        ord_dict[y] = []

# %%

def correctOrder(ord_dict, prnt):
    # checks print if correct order
    # return True if correct False if not
    ordered_mask = []
    for i in range(len(prnt)-1):
        cur = prnt[i]
        subseq = set(prnt[i+1:])
        ord_lst = set(ord_dict[cur])
        if not subseq - ord_lst:
            # current value correctly placed before all following values
            # set containing subsequent values completely contained by order_dictionary
            ordered_mask.append(True)
        else:
            # some values not in correct order for cur:subsequent
            ordered_mask.append(False)
    if all(ordered_mask):
        # all in correct order
        return True
    else:
        # at least some aren't in correct order
        return False

ans1 = 0
for p in prints:
    if correctOrder(ord_dict, p):
        middle_val = p[len(p)//2] # assume there is a true median
        ans1 += middle_val
print(ans1)

# %% Part 2

def orderPrint(ord_dict, p):
    # return list in corrected order
    # quick solution is recursive pop/append to a deque until correct order
    need2sort = p.copy()
    sorted_list = []
    while need2sort:
        # recursive sort with deque. Ends when fully sorted
        cur = need2sort[0]
        subseq = set(need2sort[1:])
        ord_lst = set(ord_dict[cur])
        if not subseq - ord_lst:
            # 1st value in correct spot
            sorted_list.append(cur)
            # pop from deque
            need2sort.pop(0)
        else:
            # incorrect order, pop and append
            need2sort.append(cur)
            need2sort.pop(0)
    return sorted_list


ans2 = 0
for p in prints:
    if correctOrder(ord_dict, p):
        # Pt1 stuff
        pass
    else:
        sorted_list = orderPrint(ord_dict, p)
        middle_val = sorted_list[len(sorted_list)//2] # assume a true median
        ans2 += middle_val
print(ans2)

# %% Thoughts
"""
I'm actually suprised I got this as quick as I did. I don't really have intuition
of BFS or DFS algorithms but after using them in previous AoC's, they sort of
inspired my orderPrint function that worked pretty well for Part 2. I'm sure
there are more elegant solutions than recursive sorting and set operations,
but good enough!
"""
