import string
import numpy as np
from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')
data = data.split('\n')

# ------
# Part 1
# ------

two_compartments = [(set(rucksack[:len(rucksack)//2]) & set(rucksack[len(rucksack)//2:])).pop() for rucksack in data]
mapping = {key:value for value, key in enumerate(string.ascii_letters, 1)}
result = sum(mapping[shared] for shared in two_compartments)
print(result)

# ------
# Part 2
# ------

groups_common = [set.intersection(*[set(item) for item in lst.tolist()]).pop() for lst in np.array_split(data, len(data)//3)]
result = sum(mapping[group] for group in groups_common)
print(result)
