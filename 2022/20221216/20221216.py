# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 13:47:17 2023

@author: david
"""
# %%
with open("input.txt", "r") as f:
    lines = [line.strip('\n') for line in f.readlines()]


# %%

'''
I need to check every path and see which one releases more pressure, keeping
track of the largest return value I get. To know which path gives the highest
return value, I need to spend all my 30 min because later moves might give high
rates of return.
'''

# parse input
paths = dict()
for line in lines:
    words = [w.strip(';,') for w in line.split()]
    curr_pos = words[1]
    curr_flowrate = int(words[4].split("=")[-1])
    curr_avail_valves = words[9:]
    paths[curr_pos] = dict()
    paths[curr_pos]["flowrate"] = curr_flowrate
    paths[curr_pos]["avail_valves"] = curr_avail_valves
    paths[curr_pos]["valve_open"] = False

important_nodes = dict()
for key, val in paths.items():
    if not val['flowrate'] == 0:
        important_nodes[key] = val

# get the shortest path from each valve to each important valve

def bfs_route(source_node, destination_node):
    global paths
    path_index = 0
    path_list = [[source_node]]
    previous_nodes = {source_node}
    if source_node == destination_node:
        return path_list[0]
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = paths[last_node]["avail_valves"]
        if destination_node in next_nodes:
            current_path.append(destination_node)
            return current_path
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                previous_nodes.add(next_node)
        path_index += 1
    return []

node2important_node = dict()
for key1 in paths.keys():
    node2important_node[key1] = dict()
    for key2 in important_nodes.keys():
        route = bfs_route(key1, key2)
        # assign as minutes to key
        node2important_node[key1][key2] = len(route)-1
# %%
import itertools
from functools import cache
# brute force every order
valves = list(important_nodes.keys())
open_valves = {valve: False for valve in valves}


def search_route(route):
    global valves
    global important_nodes
    time = 30
    steam = 0
    curr_node = 'AA'
    for valve in route:
        travel_time = node2important_node[curr_node][valve]
        time -= travel_time
        if time <= 1:
            break
        else:
            curr_node = valve
            # open valve
            time -= 1
            steam += time * important_nodes[valve]['flowrate']
    return steam

# %%


@cache
def solve_pt1():
    global valves
    max_steam = 0
    for route in itertools.permutations(valves):
        steam = search_route(route)
        if steam > max_steam:
            max_steam = steam
    return max_steam

max_steam = solve_pt1()
print(max_steam)
