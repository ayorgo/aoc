from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')
data = data.split('\n')
data = [[tuple(map(int, elf_assignment.split('-'))) for elf_assignment in pair.split(',')] for pair in data]

# ------
# Part 1
# ------

def is_full_overlap(pair: list) -> bool:
    first, second = pair
    start_first, end_first = first
    start_second, end_second = second

    if start_first <= start_second and end_first >= end_second:
        return True
    elif start_second <= start_first and end_second >= end_first:
        return True
    else:
        return False

result = sum(map(is_full_overlap, data))
print(result)

# ------
# Part 2
# ------

def is_partial_overlap(pair: list) -> bool:
    first, second = pair
    start_first, end_first = first
    start_second, end_second = second

    if start_first <= start_second and end_first >= start_second:
        return True
    elif start_second <= start_first and end_second >= start_first:
        return True
    else:
        return False

result = sum(map(is_partial_overlap, data))
print(result)
