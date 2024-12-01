# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 01:26:51 2023

@author: david
"""

# %%

# Parse
with open("input.txt", "r") as f:
    doc = f.read()

# %% Parse
def map_parse(text_block):
    title, text = text_block.split(":")
    values = [line.split() for line in text.strip().split("\n")]
    int_values = [[int(a), int(b), int(c)] for a, b, c in values]
    return int_values

category = doc.split("\n\n")
seeds = [int(num) for num in category[0].split(":")[1].split()]
seed2soil = map_parse(category[1])
soil2fert = map_parse(category[2])
fert2water = map_parse(category[3])
water2light = map_parse(category[4])
light2temp = map_parse(category[5])
temp2hum = map_parse(category[6])
hum2loc = map_parse(category[7])

# %% Part 1

def layer_remap(point_in, layer_map):
    point_out = point_in # same until maped different
    for dest, source, size in layer_map:
        if source <= point_in < source+size:
            spacer = point_in - source
            point_out = dest + spacer
    return point_out

soils = []
for seed in seeds:
    soils.append(layer_remap(seed, seed2soil))
ferts = []
for soil in soils:
    ferts.append(layer_remap(soil, soil2fert))
waters = []
for fert in ferts:
    waters.append(layer_remap(fert, fert2water))
lights = []
for water in waters:
    lights.append(layer_remap(water, water2light))
temps = []
for light in lights:
    temps.append(layer_remap(light, light2temp))
hums = []
for temp in temps:
    hums.append(layer_remap(temp, temp2hum))
locs = []
for hum in hums:
    locs.append(layer_remap(hum, hum2loc))

print(sorted(locs)[0]) # Part1 answer: 173706076

# %% Part 2

bin_in = [858905075, 915841668]
layer_map = seed2soil

def group_remap(bin_in, layer_map):
    bin_start, bin_end = bin_in[0], bin_in[1]
    bin_size = bin_end - bin_start
    out_bins = []
    while bin_in:
        
    for dest_start, source_start, size in layer_map:
        # For each remap, just split the portion of the bin that's in your map.
        # Ignore overhang, it will be taken by later iteration.
        if bin_start != 0 and bin_end != 0:
            # bin fully remapped
            break
        
        dest_start, dest_end = dest_start, dest_start + size
        source_start, source_end = source_start, source_start + size
        source2dest_diff = dest_start - source_start
        if bin_start >= source_start & bin_end <= source_end:
            # bin fully remaped
            out_bin_start = bin_start + source2dest_diff
            out_bin_end = out_bin_start + bin_size
            out_bins.append([out_bin_start, out_bin_end])
            # remaining bin to sort
            bin_start, bin_end = 0, 0
            bin_size = 0
        elif bin_start < source_start & bin_end > source_end:
            # bin hangs both sides
            # remapped portion
            out_bin_start = source_start
            out_bin_end = source_end
            out_bins.append([out_bin_start, out_bin_end])
            # remaining bin to sort
            bin_tran_size = out_bin_end - out_bin_start
            left_hang_size = source_start - bin_start
            bin_start, bin_end = bin_start
            pass
        elif bin_start >= source_start & bin_end > source_end:
            # bin hangs edge right
            out_bin_start = bin_start + source2dest_diff
            out_bin_end = source_end
            out_bins.append([out_bin_start, out_bin_end])
            # remaining bin to sort
            bin_tran_size = out_bin_end - out_bin_start
            bin_start, bin_end = bin_start + bin_tran_size, bin_end
            pass
        elif bin_start < source_start & bin_end <= source_end:
            # bin hangs edge left
            out_bin_start = source_start
            out_bin_end = bin_end + source2dest_diff
            out_bins.append([out_bin_start, out_bin_end])
            # remaining bin to sort
            bin_tran_size = out_bin_end - out_bin_end
            bin_start, bin_end = bin_start, bin_start + bin_tran_size
            pass
        
        elif bin_end <= source_start:
            # bin is left of source
            pass
        elif bin_start >= source_end:
            # bin is right of source
            pass
            
        
        
# %%


        if source_start <= in_start < in_end <= source_end:
            # bin contained. Full remap
            spacer = in_start - source_start
            out_start, out_end = (dest_start + spacer), (dest_start + spacer + in_size)
            out_bins.append([out_start, out_end])
            out_source_bins.append([in_start, in_end])
            print(f'(1{out_source_bins}) -> ({dest_start}, {dest_end}) via {source_start}, {dest_start}')
            pass
        elif source_start <= in_start < source_end < in_end:
            # bin ends later. Remap contained, bump right hanger
            spacer = in_start - source_start
            conversion = dest_start - source_start
            out_start = dest_start + spacer
            out_end = dest_end
            out_bins.append([out_start, out_end])
            out_source_bins.append([in_start, source_end])
            print(f'(2{out_source_bins}) -> ({dest_start}, {dest_end}) via {source_start}, {dest_start}')

            pass
        elif in_start < source_start < in_end <= source_end:
            # bin starts early, ends in range. bump left hanger
            spacer = in_start - source_start
            out_start = dest_start
            out_end = dest_start + spacer + in_size
            out_bins.append([out_start, out_end])
            out_source_bins.append([source_start, in_end])
            print(f'(3{out_source_bins}) -> ({dest_start}, {dest_end}) via {source_start}, {dest_start}')

            pass
        elif in_start < source_start < source_end <= in_end:
            # bin extends across both sizes, bump left and right hanger
            out_start, out_end = dest_start, dest_end
            out_bins.append([out_start, out_end])
            out_source_bins.append([source_start, source_end])
            print(f'(4{out_source_bins}) -> ({dest_start}, {dest_end}) via {source_start}, {dest_start}')

            pass
    out_source_bins.sort()
    pointer = in_start
    new_bins = [] # regions that weren't caught before, so stay the same
    for bin_start, bin_end in out_source_bins:
        if bin_start != pointer:
            # missing chunk of bin
            new_bin = [pointer, bin_start]
            new_bins.append(new_bin)
            pointer = bin_end
        else:
            pointer = bin_end
    out_source_bins = sorted(new_bins + out_source_bins)
    return out_source_bins



bins = [[start, start+size] for start, size in zip(seeds[::2], seeds[1::2])]

soils = []
for bin_ in bins:
    soils.append(group_remap(bin_, seed2soil))
ferts = []
for soil in soils:
    ferts.append(layer_remap(soil, soil2fert))
waters = []
for fert in ferts:
    waters.append(layer_remap(fert, fert2water))
lights = []
for water in waters:
    lights.append(layer_remap(water, water2light))
temps = []
for light in lights:
    temps.append(layer_remap(light, light2temp))
hums = []
for temp in temps:
    hums.append(layer_remap(temp, temp2hum))
locs = []
for hum in hums:
    locs.append(layer_remap(hum, hum2loc))

# %% Part 2







def group_remap(range_in, layer_map):
    range_out = range_in
    in_start, in_end = range_in
    out_range = []
    for dest, source, size in layer_map:
        # For each remap, just split the portion of the bin that's in your map.
        # Ignore overhang, it will be taken by later iteration.
        source_start, source_end = source, source + size
        dest_start, dest_end = dest, dest + size
        if source_start <= in_start < in_end <= source_end:
            # bin contained. Full remap
            spacer = in_start - source_start
            out_start, out_end = (dest_start + spacer), (dest_start + spacer + size)
            out_bins.append([out_start, out_end])
            pass
        elif source_start <= in_start < source_end < in_end:
            # bin ends later. Remap contained, bump right hanger
            spacer = in_start - source_start
            out_start, out_end = (dest_start + spacer), (dest_start + spacer + size)
            out_bins.append([out_start, out_end])
            pass
        elif in_start < source_start < in_end <= source_end:
            # bin starts early, ends in range. bump left hanger
            pass
        elif in_start < source_start < source_end <= in_end:
            # bin extends across both sizes, bump left and right hanger
            pass
        elif in_start < in_end < source_start < source_end:
            # bin is left of range, ignore
            pass
        elif source_start < source_end <= in_start < in_end:
            # bin is right of range, ignore
            pass



bins = [[start, start+size] for start, size in zip(seeds[::2], seeds[1::2])]

soils = []
for bin_ in bins:
    soils.append(group_remap(bin_, seed2soil))
