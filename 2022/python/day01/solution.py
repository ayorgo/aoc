import heapq
from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')

loads_inverted = [-sum(map(int, elf_load)) for elf_load in [elf_load_raw.split('\n') for elf_load_raw in data.split('\n\n')]]
heapq.heapify(loads_inverted)

# ------
# Part 1
# ------

result = -loads_inverted[0]
print(result)

# ------
# Part 2
# ------

result = -sum(heapq.nsmallest(3, loads_inverted))
print(result)
