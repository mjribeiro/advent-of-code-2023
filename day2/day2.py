import re

from functools import reduce

# Part 1: What is the sum of the IDs of those games?
with open('day2-input.txt') as f:
    lines = f.readlines()

max_possible = {"red": 12, "green": 13, "blue": 14}

ids_sum = 0
for idx, line in enumerate(lines):
    color_info = re.sub(r'^.*?:', '', line)

    for key, value in max_possible.items():
        color_info = color_info.replace(key, str(value))
    
    color_info = color_info.replace(',','').replace(';','')
    color_info = [int(x) for x in color_info.split()]
    color_diffs = [color_info[i] - color_info[i + 1] for i in range(0, len(color_info) - 1, 2)]

    if all(diff <= 0 for diff in color_diffs):
        # idx is game id - 1
        ids_sum += idx + 1

print(ids_sum)

# Part 2: Find the minimum set of cubes that must have been present. 
# What is the sum of the power of these sets?
sum_power = 0
for idx, line in enumerate(lines):
    minimums = {"red": 0, "green": 0, "blue": 0}
    color_info = re.sub(r'^.*?:', '', line).replace(' ', '')
    color_sets = [group.split(',') for group in color_info.split(';')]

    for color_set in color_sets:

        for round in color_set:
            for key in minimums.keys():
                num_cubes = re.findall(r'\d+', round)[0]

                if (key in round) and (int(num_cubes) > int(minimums[key])):
                    minimums[key] = num_cubes
        
    game_min = list(map(int, minimums.values()))
    power = reduce(lambda x, y: x * y, game_min)
    sum_power += power

print(sum_power)
