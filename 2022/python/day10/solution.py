from collections import deque
from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')

data = deque(instruction.split() + [2] if instruction.startswith('addx') else [instruction, 1] for instruction in data.split('\n'))

# ------
# Part 1
# ------

x = 1
cycle = 1
cache = data.popleft()
cache[-1] -= 1
snaphots = []
while True:
    cycle += 1
    if cache[-1] == 0:

        # Finish current instruction
        if cache[0] == 'addx':
            x += int(cache[1])

        # Queue new instruction
        if not data:
            break
        cache = data.popleft()
    cache[-1] -= 1

    if (cycle - 20) % 40 == 0:
        snaphots.append(cycle*x)
print(sum(snaphots))

# ------
# Part 2
# ------

x = 1
cycle = 1
cache = data.popleft()
cache[-1] -= 1
image = []
row = []
while True:
    cycle += 1
    if cache[-1] == 0:

        # Finish current instruction
        if cache[0] == 'addx':
            x += int(cache[1])

        # Queue new instruction
        if not data:
            break
        cache = data.popleft()
    cache[-1] -= 1

    if cycle % 40 == 0:
        snaphots.append(cycle*x)
print(image)
