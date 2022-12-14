from math import copysign
from itertools import chain, pairwise, product
from operator import add
from functools import reduce
from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')

structs = [[tuple(map(int, point.split(','))) for point in path.split(' -> ')] for path in data.split('\n')]

# -----------------
# Build the setting
# -----------------

# Define the canvas
structs_flattened = list(chain.from_iterable(structs))
x_min = min(structs_flattened, key=lambda x: x[0])[0]# - 1
x_max = max(structs_flattened, key=lambda x: x[0])[0] + 1
y_min = 0 # min(structs_flattened, key=lambda x: x[1])[1] - 1
y_max = max(structs_flattened, key=lambda x: x[1])[1] + 1

canvas = [['.' for y in range(y_max - y_min)] for x in range(x_max - x_min)]

def set_char(char: str, x: int, y: int, canvas: list) -> None:
    canvas[x - x_min][y - y_min] = char

def get_char(x: int, y: int, canvas: list) -> str:
    return canvas[x - x_min][y - y_min]

def print_struct(struct: list, canvas: list) -> None:
    for start, end in pairwise(struct):
        x_start, y_start = start
        x_end, y_end = end
        range_x = range(*sorted((x_start, x_end)))
        range_y = range(*sorted((y_start, y_end)))
        for x, y in product(range_x or [x_start], range_y or [y_start]):
            set_char('#', x, y, canvas)
        set_char('#', *start, canvas)
        set_char('#', *end, canvas)

# Print the structures
source = (500, y_min)
for struct in structs:
    print_struct(struct, canvas)

# canvas_rendered = '\n'.join([''.join(row) for row in list(map(list, zip(*canvas)))])
# print(canvas_rendered)

# Simulate the sand flow

def move(x: int, y: int, canvas: list) -> tuple:
    assert get_char(x, y, canvas) == '+', 'Not a grain of sand!'

    y_new = y + 1
    if y_new == y_max:
        return None

    if get_char(x, y_new, canvas) == '.':
        return x, y_new

    x_new = x - 1
    if x_new == x_max:
        return None

    if get_char(x_new, y_new, canvas) == '.':
        return x_new, y_new

    x_new = x + 1
    if x_new == x_max:
        return None

    if get_char(x_new, y_new, canvas) == '.':
        return x_new, y_new

    return x, y

count = 0
while True:
    grain = source
    set_char('+', *grain, canvas)
    while True:
        grain_moved = move(*grain, canvas)
        if grain_moved is None:
            break
        if grain_moved == grain:
            set_char('o', *grain, canvas)
            count += 1
            break
        set_char('.', *grain, canvas)
        set_char('+', *grain_moved, canvas)
        grain = grain_moved
    if grain_moved is None:
        break

# canvas_rendered = '\n'.join([''.join(row) for row in list(map(list, zip(*canvas)))])
# print(canvas_rendered)
# print(count)


# ------
# Part 2
# ------

# Redefine the canvas
y_max += 2
x_min = 300
x_max += 200
structs += [[(x_min, y_max - 1), (x_max - 1, y_max - 1)]]
canvas = [['.' for y in range(y_max - y_min)] for x in range(x_max - x_min)]

# Print the structures
source = (500, y_min)
for struct in structs:
    print_struct(struct, canvas)

count = 0
while True:
    grain = source
    set_char('+', *grain, canvas)
    while True:
        grain_moved = move(*grain, canvas)
        if grain_moved == source:
            set_char('o', *grain, canvas)
            count += 1
            break
        if grain_moved is None:
            # set_char('o', *grain, canvas)
            # count += 1
            break
        if grain_moved == grain:
            set_char('o', *grain, canvas)
            count += 1
            break
        set_char('.', *grain, canvas)
        set_char('+', *grain_moved, canvas)
        grain = grain_moved
    if grain_moved == source:
        break

canvas_rendered = '\n'.join([''.join(row) for row in list(map(list, zip(*canvas)))])

path = Path(__file__).with_name('output.txt')
with open(path, 'w') as f:
    f.write(canvas_rendered)
# print(canvas_rendered)
print(count)
