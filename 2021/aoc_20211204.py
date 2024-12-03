# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:30:07 2024

@author: david
"""

# %% Parse input

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

num_seq = list(map(int, lines[0].split(",")))

raw_boards = "\n".join(lines[2:]).split("\n\n")
boards = []
for g in raw_boards:
    board = [list(map(int, gr.split())) for gr in g.split("\n")]
    boards.append(board)


# hacky, but instead of finding a way to measure column winners, copy each board
# and transpose, so vertical winners are horizontal winners of the transpose
# remove marked values, then empty list is winnner

mirror_boards = []
for board in boards:
    mirror_boards.append(list(map(list, zip(*board))))


# %%

def search():
    global boards
    global mirror_boards
    global num

    for i, (b, mb) in enumerate(zip(boards, mirror_boards)):
        for rowb in b:
            try:
                rowb.remove(num)
                if len(rowb) == 0:
                    return True, i, b
            except ValueError:
                pass
        for rowmb in mb:
            try:
                rowmb.remove(num)
                if len(rowmb) == 0:
                    return True, i, mb
            except ValueError:
                pass
    return False, i, []

it = 0
winner = False
while not winner:
    num = num_seq[it]
    print(it, num)
    winner, nboard, b = search()
    it += 1

unmarked_sum = sum([val for row in b for val in row])
print(unmarked_sum * num)


# %% Part 2


# pop boards after they win, then look for last remaining board

def search2():
    global boards
    global mirror_boards
    global num

    for i, (b, mb) in enumerate(zip(boards, mirror_boards)):
        for rowb in b:
            try:
                rowb.remove(num)
            except ValueError:
                pass
        for rowmb in mb:
            try:
                rowmb.remove(num)
            except ValueError:
                pass

    # check for complete boards
    complete_boards = set()
    for i, (b, mb) in enumerate(zip(boards, mirror_boards)):
        for r1, r2 in zip(b, mb):
            if len(r1) == 0 or len(r2) == 0:
                complete_boards.add(i)
    return list(complete_boards)



it = 0
while len(boards) > 1:
    num = num_seq[it]
    #print(it, num)
    complete_boards = search2()
    #print(complete_boards, len(boards))
    # pop all boards in list complete_boards, and mirror boards
    boards = [board for i, board in enumerate(boards) if i not in complete_boards]
    mirror_boards = [mboard for i, mboard in enumerate(mirror_boards) if i not in complete_boards]
    it += 1

# now wait for last board to win. Reuse part 1 method

winner = False
while not winner:
    num = num_seq[it]
    print(it, num)
    winner, nboard, b = search()
    it += 1

unmarked_sum = sum([val for row in b for val in row])
print(unmarked_sum * num)
