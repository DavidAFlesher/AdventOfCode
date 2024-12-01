# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:57:35 2022

@author: david
"""

# %%
import json, os
with open("input.txt", "r") as f:
    lines = [line.strip('\n') for line in f.readlines()]


# %%

files = dict()
directories = dict()
full_contents = dict()
path = ''
for line in lines:
    if line[0:4] == '$ cd':
        if line[-2:] == '..':
            # change pwd to up one dir
            path = os.path.split(path)[0]
        else:
            # update pwd to new current directory
            path = os.path.join(path, line.split()[-1])
    elif line[:4] == '$ ls':
        # prepare list for ls results corresponding to the current pwd
        full_contents[path] = []
    else:
        if line.split()[0] == 'dir': # if ls yields a subdirectory
            dir_name = os.path.join(path, line.split()[-1])
            directories[dir_name] = []
            full_contents[path].append([dir_name])
        else: # if ls yields a file
            fsize, fname = line.split()
            full_fname = os.path.join(path, fname) # include pwd
            files[full_fname] = int(fsize)
            full_contents[path].append([full_fname, int(fsize)])

# %%

def file_drill(folder):
    # to drill down folders structure to find all subfiles
    # in: 'folder', str for key in full_contents
    # return: a list of all files and subfiles
    subfiles = []
    content = full_contents[folder]
    for item in content:
        if len(item) == 2: # is file
            subfiles.append(item)
        else: # is subfolder
            subfolder = item[0] # subfolder pathname
            sub_subfiles = file_drill(subfolder) # recursively look in new subfolder
            subfiles += sub_subfiles # concat to list of subfiles
    return subfiles

# %%
# showing every file and subfile in each directory
# excludes home directory
for key, val in directories.items():
    sub_files = file_drill(key)
    directories[key] = sub_files
# %%
# get directory total filesize
directory_totals = {}
for key, val in directories.items():
    directory_totals[key] = 0
    for file in val:
        directory_totals[key] += int(file[-1])
# %%
# get directories who's size is <= 100,000
total_size_100000 = 0
for key, val in directory_totals.items():
    if val <= 100000:
        total_size_100000 += val
print(total_size_100000) # 1428881

# %% Part 2
total_space_used = 0
for val in files.values():
    total_space_used += val
print(total_space_used) # 48518336

avail_space = 70000000 - total_space_used
space_needed = 30000000 - avail_space

# look for directories bigger than the space needed
contenders = []
for key, val in directory_totals.items():
    if val >= space_needed:
        contenders.append([key, val])
print(sorted(contenders, key = lambda x: x[-1])[0]) # ['/jsv\\bwc\\jwrhclh', 10475598]
