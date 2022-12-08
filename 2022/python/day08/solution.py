from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')
data = [[int(tree) for tree in list(row)] for row in data.split('\n')]

n = len(data)

# ------
# Part 1
# ------

count = 0
visited = set()

# Left
for r in range(n):
    tree_max = -1
    for c in range(n):
        tree = data[r][c]
        if tree > tree_max:
            if (r, c) not in visited:
                count += 1
            tree_max = tree
            visited.add((r, c))
        if tree_max == 9:
            break

# Right
for r in range(n):
    tree_max = -1
    for c in reversed(range(n)):
        tree = data[r][c]
        if tree > tree_max:
            if (r, c) not in visited:
                count += 1
            tree_max = tree
            visited.add((r, c))
        if tree_max == 9:
            break

# Top
for c in range(n):
    tree_max = -1
    for r in range(n):
        tree = data[r][c]
        if tree > tree_max:
            if (r, c) not in visited:
                count += 1
            tree_max = tree
            visited.add((r, c))
        if tree_max == 9:
            break

# Bottom
for c in range(n):
    tree_max = -1
    for r in reversed(range(n)):
        tree = data[r][c]
        if tree > tree_max:
            if (r, c) not in visited:
                count += 1
            tree_max = tree
            visited.add((r, c))
        if tree_max == 9:
            break

result = count
print(count)

# ------
# Part 2
# ------

nearest_ref = {
        0: None,
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
    }

visible = dict()

# Left
for r in range(n):
    nearest = nearest_ref.copy()
    for c in range(n):
        tree = data[r][c]
        visible_dist = c
        for nearest_hight, nearest_coord in nearest.items():
            if nearest_hight >= tree and nearest_coord is not None:
                visible_dist = c - nearest_coord
                break
        if (r, c) in visible:
            visible[(r, c)] *= visible_dist
        else:
            visible[(r, c)] = visible_dist
        nearest[tree] = c

# Right
for r in range(n):
    nearest = nearest_ref.copy()
    for c in reversed(range(n)):
        tree = data[r][c]
        visible_dist = n - 1 - c
        for nearest_hight, nearest_coord in nearest.items():
            if nearest_hight >= tree and nearest_coord is not None:
                visible_dist = nearest_coord - c
                break
        if (r, c) in visible:
            visible[(r, c)] *= visible_dist
        else:
            visible[(r, c)] = visible_dist
        nearest[tree] = c

# Top
for c in range(n):
    nearest = nearest_ref.copy()
    for r in range(n):
        tree = data[r][c]
        visible_dist = r
        for nearest_hight, nearest_coord in nearest.items():
            if nearest_hight >= tree and nearest_coord is not None:
                visible_dist = r - nearest_coord
                break
        if (r, c) in visible:
            visible[(r, c)] *= visible_dist
        else:
            visible[(r, c)] = visible_dist
        nearest[tree] = r

# Bottom
for c in range(n):
    nearest = nearest_ref.copy()
    for r in reversed(range(n)):
        tree = data[r][c]
        visible_dist = n - 1 - r
        for nearest_hight, nearest_coord in nearest.items():
            if nearest_hight >= tree and nearest_coord is not None:
                visible_dist = nearest_coord - r
                break
        if (r, c) in visible:
            visible[(r, c)] *= visible_dist
        else:
            visible[(r, c)] = visible_dist
        nearest[tree] = r

result = max(visible.values())
print(result)
