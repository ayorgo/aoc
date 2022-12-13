from functools import cmp_to_key
from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')

def compare(first: list, second: list) -> int:
    queue = [(first, second)]
    while queue:
        first, second = queue.pop()
        match (first, second):
            case (int(), list()):
                queue.append(([first], second))
            case (list(), int()):
                queue.append((first, [second]))
            case (list(), list()):
                if len(first) == len(second) == 0:
                    continue
                if len(first) == 0:
                    return -1
                if len(second) == 0:
                    return 1
                queue.append((first[1:], second[1:]))
                queue.append((first[0], second[0]))
            case (int(), int()):
                if first < second:
                    return -1
                if first > second:
                    return 1
    return 0

# ------
# Part 1
# ------

packets = [[eval(piece) for piece in data.split('\n')] for data in data.split('\n\n')]
result = sum([ix + 1 if compare(*item) == -1 else 0 for ix, item in enumerate(packets)])
print(result)

# ------
# Part 2
# ------
packets = [eval(piece) for piece in data.replace('\n\n', '\n').split('\n')] + [[[2]]] + [[[6]]]
packets_sorted = sorted(packets, key=cmp_to_key(compare))
result = (packets_sorted.index([[2]]) + 1)*(packets_sorted.index([[6]]) + 1)
print(result)
