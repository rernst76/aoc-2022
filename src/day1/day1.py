from itertools import groupby

with open("src/day1/input.txt", "r") as f:
    data = [x for x in f.readlines()]

# Part 1
# Convert all non-blank lines to integers
data = [int(x.strip()) if x != "\n" else "\n" for x in data]

# Create list of list, split by newline
data = [list(g) for k, g in groupby(data, lambda x: x == "\n") if not k]

# For each list in data, sum the list, and return the largest sum
print(max([sum(x) for x in data]))

# Part 2
# Create a list of all of the sums, and find the three largest sums
sums = [sum(x) for x in data]
sums.sort(reverse=True)

top_three = sums[:3]
print(sum(top_three))
