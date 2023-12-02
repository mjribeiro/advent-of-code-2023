# Part 1: What is the sum of all the calibration values?
with open('day1-input.txt') as f:
    lines = f.readlines()

# Remove all non-numeric characters from each line and convert to calibration values
no_letters = [''.join(filter(str.isdigit, line)) for line in lines]
calibration_vals = [int("".join([line[0], line[-1]])) for line in no_letters]

print(sum(calibration_vals))

# Part 2: What is the sum of all the calibration values, bearing in mind digits can also be spelled out?
digits = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
max_digit_len = max([len(value) for value in digits.values()])

# Replace all spelled out digits with their numeric counterparts
new_lines = []

for line in lines:
    new_line = ""

    for idx in range(len(line)):
        for key, value in digits.items():

            if line[idx:].startswith(value):
                new_line = "".join([new_line, str(key)])

        if line[idx].isdigit():
            new_line = "".join([new_line, line[idx]])

    new_lines.append(new_line)

# Remove all non-numeric characters from each line and convert to calibration values
no_letters = [''.join(filter(str.isdigit, line)) for line in new_lines]
calibration_vals = [int("".join([line[0], line[-1]])) for line in no_letters]

print(sum(calibration_vals))
