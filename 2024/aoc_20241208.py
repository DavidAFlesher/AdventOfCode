# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 00:14:39 2024

@author: david
"""
# %% Parse input

with open("input.txt", "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

gsize = (len(lines), len(lines[0]))

# %% Part 1
# dict of antennas by their frequency then form a set for their coordinates
antennas = dict()
for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] != ".":
            try:
                antennas[lines[r][c]].append((r, c))
            except KeyError:
                antennas[lines[r][c]] = [(r, c)]

antinodes1 = set()
for k, v in antennas.items():
    # for each antenna frequency, compare to other antennas of same freq
    for ant1 in v:
        for ant2 in v:
            if ant1 == ant2: continue # don't compare antenna to itself
            a1r, a1c = ant1
            a2r, a2c = ant2
            d12r, d12c = a1r - a2r, a1c - a2c
            d21r, d21c = a2r - a1r, a2c - a1c # aka delta12 * -1

            # antinodes
            node12r, node12c = a1r + d12r, a1c + d12c
            if (0 <= node12r < gsize[0]) and (0 <= node12c < gsize[1]):
                antinodes1.add((node12r, node12c))

            node21r, node21c = a2r + d21r, a2c + d21c
            if (0 <= node21r < gsize[0]) and (0 <= node21c < gsize[1]):
                antinodes1.add((node21r, node21c))
ans1 = len(antinodes1)
print(ans1)

# %% Part 2
def getNodes(ant1, ant2, gsize):
    # Similar to pt1, but looks for antinodes recursively
    # returns set of antinode coordinates caused by two towers
    a1r, a1c = ant1
    a2r, a2c = ant2
    d12r, d12c = a1r - a2r, a1c - a2c
    d21r, d21c = a2r - a1r, a2c - a1c # aka delta12 * -1

    # Initialize nodes with the positions of the ants for pt2
    nodes = {(a1r, a1c), (a2r, a2c)}
    # looking in the direction from node1 to node2
    i = 0
    while True:
        node12r, node12c = a1r + d12r * i, a1c + d12c * i
        if (0 <= node12r < gsize[0]) and (0 <= node12c < gsize[1]):
            # add coordinates to nodes
            nodes.add((node12r, node12c))
            i += 1
        else: break # out of bounds
    # Looking in the direction from node2 to node1
    i = 0
    while True:
        node21r, node21c = a2r + d21r * i, a2c + d21c * i
        if (0 <= node21r < gsize[0]) and (0 <= node21c < gsize[1]):
            # add coordinates to nodes
            nodes.add((node21r, node21c))
            i += 1
        else: break # out of bounds
    return nodes

antinodes2 = set()
for k, v in antennas.items():
    # for each antenna frequency, compare to other antennas of same freq
    for ant1 in v:
        for ant2 in v:
            if ant1 == ant2: continue # don't compare antenna to itself
            # antinodes
            anodes = getNodes(ant1, ant2, gsize)
            for a in anodes:
                antinodes2.add(a)
ans2 = len(antinodes2)
print(ans2)

# %% Thoughts
"""
I really liked today. There is probably a cleaner way to write this up because
I have a good amount of 'copy/paste' code, but I thought it was a decent way to
seperate the antinodes in each direction. Good enough for now.
"""
