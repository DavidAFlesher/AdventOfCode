# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:59:55 2024

@author: david
"""
# %% Parse input

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

equations = []
for l in lines:
    eq, nums = l.split(":")
    nums = nums.split()
    equations.append([int(eq), nums])
# %% Part 1

def try_all_permutations(eq, nums, perm_opers):
    # loop through all operation permutations and see if any produce the corr ans
    # if yes, return True, the ans, and the equation in string format
    valid = False
    ans = "False"
    for op in perm_opers:
        # not needed, just prints a pretty version of the equation to be evaluated
        str_eq = ["" for _ in range((len(nums)*2-1))]
        str_eq[::2] = nums
        str_eq[1::2] = op
        str_eq = "".join(str_eq)
        # Bubble evaluate since eval gives the wrong order of operations
        tmp_nums = nums.copy()
        str_ans = tmp_nums.pop(0)
        while tmp_nums:
            str_ans = str(eval(str_ans+op.pop(0)+tmp_nums.pop(0)))
        if int(str_ans) == eq:
            # correct answer found
            valid = True
            ans = str_ans
            return True, str_ans, str_eq
            break
    return False, -1, "False"

from itertools import product

ans1 = 0
for eq, nums in equations:
    while True:
        # use itertools product to get all permutations of operators
        perm_opers = list(map(list, set(product("+*", repeat = len(nums)-1))))
        valid, ans, str_eq = try_all_permutations(eq, nums, perm_opers)
        if valid:
            # found solution
            ans1 += eq
            break
        else:
            # no solution
            break
print("Pt1:", ans1)

# %% Part 2

# yikes, this is going to take forever. Not sure how not to brute force
def pt2_permutations(eq, nums, perm_opers):
    # loop through all operation permutations and see if any produce the corr ans
    # if yes, return True, the ans, and the equation in string format
    for op in perm_opers:
        # not needed, just prints a pretty version of the equation to be evaluated
        str_eq = ["" for _ in range((len(nums)*2-1))]
        str_eq[::2] = nums
        str_eq[1::2] = op
        str_eq = "".join(str_eq)
        # Bubble evaluate since eval gives the wrong order of operations
        tmp_nums = nums.copy()
        str_ans = tmp_nums.pop(0)
        while tmp_nums:
            _o =  op.pop(0)
            if _o == "|":
                str_ans += tmp_nums.pop(0)
            else:
                str_ans = str(eval(str_ans + _o + tmp_nums.pop(0)))
        if int(str_ans) == eq:
            # correct answer found
            return True, str_ans, str_eq
    return False, "-1", "false"

ans2 = 0
for eq, nums in equations:
    # use itertools permutations to get all permutations of operators
    op_len = len(nums)-1
    perm_opers = list(map(list, set(product("+*|", repeat = op_len))))
    valid, ans, str_eq = pt2_permutations(eq, nums, perm_opers)
    if valid:
        # found solution
        ans2 += eq
print(ans2)
# this took several minutes to run
# %% Thoughts
"""
My solutions for this day are very slow. There are probably ways to optimize,
but honestly nothing comes to mind right now. This was also the first time I've
really used itertools so I spent a bunch of time thinking I neededt to use permutations
or combinations_with_replacement.
"""
