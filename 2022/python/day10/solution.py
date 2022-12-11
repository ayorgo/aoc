from collections import deque
from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')

program = deque(instruction.split() + [2] if instruction.startswith('addx') else [instruction, 1] for instruction in data.split('\n'))

# ------
# Part 1
# ------

x = 1
cycle = 1
cache = program.popleft()
cache[-1] -= 1
snaphots = []
while True:
    cycle += 1
    if cache[-1] == 0:

        # Finish current instruction
        if cache[0] == 'addx':
            x += int(cache[1])

        # Queue new instruction
        if not program:
            break
        cache = program.popleft()
    cache[-1] -= 1

    if (cycle - 20) % 40 == 0:
        snaphots.append(cycle*x)

result = sum(snaphots)
print(result)

# ------
# Part 2
# ------

program = deque(instruction.split() + [2] if instruction.startswith('addx') else [instruction, 1] for instruction in data.split('\n'))

x = 1
cycle = 1
cache = program.popleft()
cache[-1] -= 1
image = []
while True:
    sprite = [x - 1, x, x + 1]
    cursor = cycle % 40
    if cursor == 1:
        row = []
        image.append(row)

    # What to print
    if (cursor - 1) in sprite:
        row.append('#')
    else:
        row.append('.')
    cycle += 1

    if cache[-1] == 0:

        # Finish current instruction
        if cache[0] == 'addx':
            x += int(cache[1])

        # Queue new instruction
        if not program:
            break
        cache = program.popleft()
    cache[-1] -= 1

result = '\n'.join(''.join(row) for row in image)
print(result)
