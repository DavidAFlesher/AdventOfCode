# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:39:20 2022

@author: david
"""

redundant_asses = []
unique_asses = []
with open("input.txt", "r") as f:
    assignments = f.readlines()
    for i, asses in enumerate(assignments):
        #print(asses)
        ass_1, ass_2 = asses.strip('\n').split(",")
        ass_1_start, ass_1_end = ass_1.split("-")
        ass_2_start, ass_2_end = ass_2.split("-")

        ass_1_start = int(ass_1_start)
        ass_1_end = int(ass_1_end)
        ass_2_start = int(ass_2_start)
        ass_2_end = int(ass_2_end)

        # if either edge matches, one of the elves
        # will be redudant guarenteed.
        if ass_1_start == ass_2_start:
            redundant_asses.append(asses)
        elif ass_1_end == ass_2_end:
            redundant_asses.append(asses)
        elif ass_1_start > ass_2_end:
            # ass_2 before ass_1
            unique_asses.append(asses)
        elif ass_2_start > ass_1_end:
            # ass_1 before ass_2
            unique_asses.append(asses)
        elif ass_1_start < ass_2_start:
            if ass_1_end > ass_2_end:
                # ass_2 within ass_1
                redundant_asses.append(asses)
        elif ass_1_start > ass_2_start:
            if ass_1_end < ass_2_end:
                # ass_1 within ass_2
                redundant_asses.append(asses)

print(len(redundant_asses))
print(len(unique_asses))
