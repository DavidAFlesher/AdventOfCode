# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 20:41:19 2022

@author: david
"""

with open("input.txt", "r") as f:
    lines = [line.strip('\n').split() for line in f.readlines()]

# %%
register = 1
register_history = []
for line in lines:
    if line[0] == "addx":
        # record register val for two cycles
        # update registrar at the end of two cycles
        register_history.append(register)
        register_history.append(register)
        register += int(line[1])
        pass
    elif line[0] == "noop":
        # sleep cycle. record the register val
        register_history.append(register)
        pass

# offset for zero indexing
signal_strengths = [20*register_history[19],
                   60*register_history[59],
                   100*register_history[99],
                   140*register_history[139],
                   180*register_history[179],
                   220*register_history[219]]
print(sum(signal_strengths)) # 15680
# %%
pixel_record = []
for i, register_val in enumerate(register_history):
    # center piel on register_val
    pixel_range = [register_val-1, register_val, register_val+1]
    # modulo yields the column regardless of row
    crt_position = i%40
    if crt_position in pixel_range:
        pixel_record.append(True) # pixel on
    else:
        pixel_record.append(False) # pixel off

with open('output.txt', 'w+') as f:
    for i, pixel in enumerate(pixel_record):
        if pixel:
            f.write('X')
        else:
            f.write('-')
        if i%40 == 39:
            f.write('\n')
# =============================================================================
#
# XXXX-XXXX-XXX--XXXX-X--X--XX--X--X-XXX--
# ---X-X----X--X-X----X--X-X--X-X--X-X--X-
# --X--XXX--XXX--XXX--XXXX-X----X--X-X--X-
# -X---X----X--X-X----X--X-X-XX-X--X-XXX--
# X----X----X--X-X----X--X-X--X-X--X-X----
# XXXX-X----XXX--X----X--X--XXX--XX--X----
#
# =============================================================================
