# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 23:57:35 2022

@author: david
"""

import json


with open("input.txt", "r") as f:
    lines = [line.strip('\n') for line in f.readlines()]

# %%

testsize = 0
counter = 0
for line in lines:
    if line[0] == "$":
        pass
    elif line[0] == 'd':
        pass
    else:
        size = int(line.split()[0])
        testsize += size
        counter += 1
# full size = 48518336
print(counter) #279
# %%Part1

# every cd command in order
directories = [line for line in lines if line[:4] == '$ cd']

# convert the .. to define directory
verbose_directories = []
for i, line in enumerate(directories):
    if '..' in line:
        # the cd command 2 prior will tell you destination directory
        # also, I should pull from directories and correct for multiple ..
        # in a row, but since I'm guarenteed to be linear in my dir nav,
        # I'll always be one step ahead of a cd .. command and can pull
        # from my newly constructed list. Janky, but good enough
        verbose_directories.append(verbose_directories[i-2])
    else:
        verbose_directories.append(line)

file_sizes = dict()
for line in lines:
    line_split = line.split()
    if line_split[0] == '$':
        pass
    elif line_split[0] == 'dir':
        pass
    else:
        file_sizes[line_split[-1]] = int(line_split[0])

# group outputs by ls results
mover = []
groups = []
for line in lines:
    if line[:4] == '$ cd':
        groups.append(mover)
        mover = []
    else:
        mover.append(line)
groups.append(mover)
# %%
with open('verbose_directories.txt', 'w') as f:
    for line in verbose_directories:
        f.write(f'{line}\n')
with open('groups.txt', 'w') as f:
    for line in groups:
        f.write(f'{line}\n')
# %%

# groups and verbose_directories are now matching, but shifted by one
# I can then match up the cd directory with the ls results by correcting that shift

del groups[0]

folder_struct = dict()
for directory, group in zip(verbose_directories, groups):
    dir_name = directory.split()[-1]
    if len(group) > 0:
        folder_struct[dir_name] = group[1:]


file_dir = []
for directory, group in zip(verbose_directories, groups):
    dir_name = directory.split()[-1]
    if len(group) > 0:
        for line in group:
            line_split = line.split()
            if line_split[0] == '$':
                pass
            elif line_split[0] == 'dir':
                pass
            else:
                fname = line_split[-1]
                construct = [dir_name, fname]
                file_dir.append(construct)


with open('folder_struct.json', 'w') as f:
    json.dump(folder_struct, f, indent = 4)

# %%

# I now have a dictionary where the key is the directory name
# and the value is a list containing the ls results

# flatten my directories to list every subfile

flattened_folder_struct = folder_struct.copy()

for key, val in flattened_folder_struct.items():
    for i, line in enumerate(val):
        if line[:3] == 'dir':
            dir_name = line.split()[-1]
            dir_contents = flattened_folder_struct[dir_name]
            # update to show those contents
            flattened_folder_struct[key][i] = {dir_name: dir_contents}

final_structured_folder = {'/': flattened_folder_struct['/'].copy()}
with open('final_structured_folder.json', 'w') as f:
    json.dump(final_structured_folder, f, indent = 4)
with open('flattened_structured_folder.json', 'w') as f:
    json.dump(flattened_folder_struct, f, indent = 4)

# %%

# create dictionary of every directory/subdirectory and link with int val
directory_sizes = {key: 0 for key in flattened_folder_struct.keys()}


# %%

# recursive function to drill down through nested dictionaries
def recursive_adder(folder, file_sizes_sum):
    # folder = list
    # filesizzes_sum = float
    for item_func in folder:
        #print(file_sizes_sum)
        if isinstance(item_func, dict):
            #print(type(list(item_func.values())))
            #print((list(item_func.values()))[0])

            sub_folder = list(item_func.values())[0]
            file_sizes_sum += recursive_adder(sub_folder, file_sizes_sum)
        else:
            file_size = int(item_func.split()[0])
            file_sizes_sum += file_size
            #print(file_sizes_sum)
    return file_sizes_sum

# %% verificatyion

with open('final_structured_folder.json', 'r') as f:
    lines = lines = [line.strip('\n').strip() for line in f.readlines()]

all_sizes = []
for line in lines:
    if line[0] in ['{', '}', '[', ']']:
        pass
    elif line[-1] == '[':
        pass
    else:
        size = int(line[1:-1].split()[0])
        all_sizes.append(size)
print(sum(all_sizes)) #28388058
print(len(all_sizes)) #154

# %%

test = flattened_folder_struct['/']
outer_size = recursive_adder(test, 0)

for key, val in flattened_folder_struct.items():
    file_sizes_sum = 0
    dir_total_size = recursive_adder(val, file_sizes_sum)
    directory_sizes[key] = dir_total_size



# %%
small_dirs = []
just_sizes = []
for key, val in directory_sizes.items():
    if val <= 1000000:
        small_dirs.append({key: val})
        just_sizes.append(val)

print(sum(just_sizes))
# %%
directory_sizes = {key: 0 for key in folder_struct.keys()}

for key in directory_sizes.keys():
    file_sizes_sum = 0
    dir_total_size = recursive_adder(folder_struct[key], file_sizes_sum)
    directory_sizes[key] = dir_total_size

# Now I have a dictionary with the total size of every directory in the filestructure

# %%

part1_answer = 0
for key, val in test.items():
    if val <= 100000:
        print(f'{key}: {val}')
        part1_answer += val
print(part1_answer)

# try 1191739, No, too low
# %% Part2
