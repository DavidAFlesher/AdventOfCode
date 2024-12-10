# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:56:32 2024

@author: david
"""
# %% Parse input

with open("demo_input.txt", "r") as f:
    # open file and conver to ints
    grid = [list(map(int, line.strip())) for line in f.readlines()]

# %% Parse input

with open("input.txt", "r") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

# %% General data/functions

# get trailheads
trailheads = set()
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            trailheads.add((r, c))

def possibleMoves(coord, visited):
    # get coordinates of possible moves from any one spot
    global grid
    global nines
    ncoords = []
    r = coord[0]
    c = coord[1]
    h = grid[r][c]
    moves = ([-1, 0], [0, 1], [1, 0], [0, -1]) # up, right, down, left
    for m in moves:
        nr = coord[0] + m[0]
        nc = coord[1] + m[1]
        if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0])):
            # out of bounds
            continue
        elif (nr, nc) in visited:
            # already been there
            continue
        elif grid[nr][nc] == h + 1:
            # coodinate is one heigher than curr spot
            ncoords.append((nr, nc))
    return ncoords

def dfs(coord):
    # standard dfs search of graph (aka our map)
    # return coord list where reached max height of 9
    global grid
    visited = {coord}
    deque = list()
    # initialize deque
    for move in possibleMoves(coord, visited):
        deque.append(move)
    nines = []
    while deque:
        coord = deque.pop()
        visited.add(coord)
        if grid[coord[0]][coord[1]] == 9:
            nines.append([coord[0], coord[1]])
        for move in possibleMoves(coord, visited):
            deque.append(move)
    return nines



# %% Part 1
ans1 = 0
for th in trailheads:
    ans1 += len(dfs(th))
print(ans1)


# %% Part 2

# Only diff in Pt2 is that I do breath first search
def bfs(coord):
    # standard bfs search of graph (aka our map)
    # return coord list where reached max height of 9
    global grid
    visited = {coord}
    deque = list()
    # initialize deque
    for move in possibleMoves(coord, visited):
        deque.append(move)
    nines = []
    while deque:
        coord = deque.pop(0)
        visited.add(coord)
        if grid[coord[0]][coord[1]] == 9:
            nines.append([coord[0], coord[1]])
        for move in possibleMoves(coord, visited):
            deque.append(move)
    return nines

ans2 = 0
for th in trailheads:
    ans2 += len(bfs(th))
print(ans2)


# %% Thoughts
"""
I liked this one. In my regular work, I never need to do any searching, so it
is a good exercise to code a dfs and bfs algorith. I have to look up hints online,
but I'm definetely much faster than I use to be when I started doing AoC!!
"""
