# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:57:35 2022

@author: david
"""

import json


with open("input.txt", "r") as f:
    lines = [line.strip('\n') for line in f.readlines()]
with open("input.txt", "r") as f:
    text = f.read().replace('\n', '')

# %%
# list of files
files = dict()
directories = dict()
#directory = 'empty'
full_contents = dict()
#folder_contents = []
#ls_content = []
for line in lines:
    if line[0:4] == '$ cd':
        if line[-2:] == '..':
            #print(line)
            pass
        else:
            directory = line.split()[-1]
            #print(directory)
    elif line[:4] == '$ ls':
        #print(line)
        #folder_contents.append(ls_content)

        #ls_content = {directory: []}
        full_contents[directory] = []
    else:
        if line.split()[0] == 'dir':
            dir_name = line.split()[-1]
            directories[dir_name] = []
            #ls_content[directory].append([dir_name])
            full_contents[directory].append([dir_name])
        else:
            fsize, fname = line.split()
            files[fname] = int(fsize)
            #ls_content[directory].append([fname, int(fsize)])
            full_contents[directory].append([fname, int(fsize)])
# %%
total_test = 0
for fsize in files.values():
    total_test += fsize
print(total_test) # 31232735


# %%
with open('full_contents.json', 'w') as f:
    json.dump(full_contents, f, indent = 4)

# %%

def recursive(folder):
    # in: 'folder', str for key in full_contents
    # return: a list of all files and subfiles
    subfiles = []
    content = full_contents[folder]
    for item in content:
        if len(item) == 2: # is file
            subfiles.append(item)
        else:
            subfolder = item[0]
            sub_subfiles = recursive(subfolder)
            subfiles += sub_subfiles
    return subfiles

# %%

for key, val in directories.items():
    sub_files = recursive(key)
    directories[key] = sub_files
# %%
directory_totals = {}
for key, val in directories.items():
    directory_totals[key] = 0
    for file in val:
        directory_totals[key] += int(file[-1])
# %%
total_size_100000 = 0
for key, val in directory_totals.items():
    if val <= 100000:
        total_size_100000 += val
print(total_size_100000) # 1191739
