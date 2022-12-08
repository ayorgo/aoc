from collections import Counter
from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')

def get_marker(data: str, size: int = 4) -> int:
    win_unique = Counter(data[:size])
    for i in range(size, len(data)):
        if len(win_unique) == size:
            return i
        win_unique[data[i - size]] -= 1
        if win_unique[data[i - size]] == 0:
            win_unique.pop(data[i - size])
        win_unique[data[i]] += 1
    return None

# ------
# Part 1
# ------

result = get_marker(data)
print(result)

# ------
# Part 2
# ------

result = get_marker(data, 14)
print(result)
