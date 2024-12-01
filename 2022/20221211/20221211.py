# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 01:57:43 2022

@author: david
"""

# %%

# good opportunity to practice classes

class Monkey:

    monkey_item_catalog =  dict()
    monkey_inspection_counter = dict()
    stress_relief = 3 # divisor after monkey inspects item
    modulo = 2*7*11*19*3*5*17*13

    def __init__(self, monkey_id, items, operation, value, test_val, test_true, test_false):
        self.monkey_id = str(monkey_id)
        self.items = items # list of items integers
        self.operation = operation # 'multiply', 'plus', or 'square' in my input
        self.value = int(value) # value to operate with, '1' if operation is square
        self.test_val = int(test_val) # value to check if divisible by
        self.test_true = str(test_true) # monkey ID to throw to if true
        self.test_false = str(test_false) # monkey ID to throw to if false
        # store each monkey's current items in a catalog
        Monkey.monkey_item_catalog[self.monkey_id] = self.items
        # keep track of number of items each monkey inspects
        Monkey.monkey_inspection_counter[self.monkey_id] = 0

    def monkey_turn(self):
        # operations for that monkey's turn
        for item in Monkey.monkey_item_catalog[self.monkey_id]:
            # perform inspection operation
            if self.operation == 'plus':
                new = item + self.value
            elif self.operation == 'multiply':
                new = item * self.value
            elif self.operation == 'square':
                new = item**2
            # update item worry level
            # apply mod to keep stress under check
            new = new % Monkey.modulo
            new = new // Monkey.stress_relief
            # run test to throw item to new monkey
            if new%self.test_val == 0:
                # send item to true test monkey
                Monkey.monkey_item_catalog[self.test_true].append(new)
                pass
            else:
                # send item to false test monkey
                Monkey.monkey_item_catalog[self.test_false].append(new)
                pass
            Monkey.monkey_inspection_counter[self.monkey_id] += 1
        # update monkey_item_catalog to be empty after inspecting all items
        Monkey.monkey_item_catalog[self.monkey_id] = []
        return

# %%

Monkey0 = Monkey('0', [66, 59, 64, 51], 'multiply', '3', '2', '1', '4')
Monkey1 = Monkey('1', [67, 61], 'multiply', '19', '7', '3', '5')
Monkey2 = Monkey('2', [86, 93, 80, 70, 71, 81, 56], 'plus', '2', '11', '4', '0')
Monkey3 = Monkey('3', [94], 'square', '1', '19', '7', '6')
Monkey4 = Monkey('4', [71, 92, 64], 'plus', '8', '3', '5', '1')
Monkey5 = Monkey('5', [58, 81, 92, 75, 56], 'plus', '6', '5', '3', '6')
Monkey6 = Monkey('6', [82, 98, 77, 94, 86, 81], 'plus', '7', '17', '7', '2')
Monkey7 = Monkey('7', [54, 95, 70, 93, 88, 93, 63, 50], 'plus', '4', '13', '2', '0')

all_monkeys = [Monkey0, Monkey1, Monkey2, Monkey3, Monkey4, Monkey5, Monkey6, Monkey7]
# %%
for i in range(20):
    for monkey_instance in all_monkeys:
        monkey_instance.monkey_turn()

tmp = sorted(list(Monkey.monkey_inspection_counter.values()))[-2:]
monkey_business = tmp[0] * tmp[1] # Answer: 90294


# %% Part 2

# This part was stupid. I've never even heard of modular arithmetic
# I modified the Monkey class to accomidate this
Monkey.stress_relief = 1

# reinitialize classes. Could just update the Monkey item catalog, but copy paste ezpz
Monkey0 = Monkey('0', [66, 59, 64, 51], 'multiply', '3', '2', '1', '4')
Monkey1 = Monkey('1', [67, 61], 'multiply', '19', '7', '3', '5')
Monkey2 = Monkey('2', [86, 93, 80, 70, 71, 81, 56], 'plus', '2', '11', '4', '0')
Monkey3 = Monkey('3', [94], 'square', '1', '19', '7', '6')
Monkey4 = Monkey('4', [71, 92, 64], 'plus', '8', '3', '5', '1')
Monkey5 = Monkey('5', [58, 81, 92, 75, 56], 'plus', '6', '5', '3', '6')
Monkey6 = Monkey('6', [82, 98, 77, 94, 86, 81], 'plus', '7', '17', '7', '2')
Monkey7 = Monkey('7', [54, 95, 70, 93, 88, 93, 63, 50], 'plus', '4', '13', '2', '0')

all_monkeys = [Monkey0, Monkey1, Monkey2, Monkey3, Monkey4, Monkey5, Monkey6, Monkey7]
# %%
for i in range(10000):
    for monkey_instance in all_monkeys:
        monkey_instance.monkey_turn()

tmp = sorted(list(Monkey.monkey_inspection_counter.values()))[-2:]
monkey_business = tmp[0] * tmp[1] # Answer: 18170818354
