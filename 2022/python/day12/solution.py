from collections import deque
import string
from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')
area = data.split('\n')

def is_inside(row: int, col: int, height: int = len(area), width: int = len(area[0])):
    return row >= 0 and col >= 0 and row < height and col < width

def find_start(area: list, start: str):
    for row in range(len(area)):
        for col in range(len(area[0])):
            if area[row][col] == start:
                return row, col

def find_path_len(area: list, row: int, col: int, end: str, backwards: bool = False):
    elevations = {char: ix for ix, char in enumerate(string.ascii_lowercase)}
    elevations['S'] = 0
    elevations['E'] = 25

    step = 0
    steps = []
    tail = set()
    nodes = deque([(row, col, None, step)])
    while nodes:
        row, col, prev, step = nodes.popleft()

        if not is_inside(row, col) or (row, col) in tail:
            continue

        curr = area[row][col]
        if prev is not None:
            if backwards:
                if not elevations[prev] <= elevations[curr] + 1:
                    continue
            else:
                if not elevations[curr] <= elevations[prev] + 1:
                    continue

        if area[row][col] == end:
            steps.append(step)
            continue

        nodes.append((row, col + 1, curr, step + 1))
        nodes.append((row, col - 1, curr, step + 1))
        nodes.append((row + 1, col, curr, step + 1))
        nodes.append((row - 1, col, curr, step + 1))
        tail.add((row, col))
    return min(steps)

# ------
# Part 1
# ------

row, col = find_start(area, 'S')
result = find_path_len(area, row, col, 'E')
print(result)

# ------
# Part 2
# ------

row, col = find_start(area, 'E')
result = find_path_len(area, row, col, 'a', True)
print(result)
