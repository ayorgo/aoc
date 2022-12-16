import re
from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')
data = [list(map(int, re.findall(r'-?\d+', line))) for line in data.split('\n')]

def squash_spans(spans: list) -> list:
    spans_sorted = sorted(spans, key=lambda x: x[0])
    spans_squashed = []
    current_start, current_end = spans_sorted[0]
    i = 1
    while i < len(spans_sorted):
        next_start, next_end = spans_sorted[i]
        if current_start <= next_start <= current_end:
            if current_start <= next_end <= current_end:
                pass
            else:
                current_end = next_end
        else:
            spans_squashed.append((current_start, current_end))
            current_start, current_end = next_start, next_end
        i += 1
    spans_squashed.append((current_start, current_end))
    return spans_squashed

# ------
# Part 1
# ------

def get_result(data, Y):
    spans = []
    excludes = set()
    for line in data:
        sensor_x, sensor_y, beacon_x, beacon_y = line
        if beacon_y == Y:
            excludes.add(beacon_x)
        if sensor_y == Y:
            excludes.add(sensor_x)
        dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        if abs(sensor_y - Y) <= dist:
            span_left = sensor_x - (dist - abs(sensor_y - Y))
            span_right = sensor_x + (dist - abs(sensor_y - Y))
            spans.append((span_left, span_right))

    if spans:
        spans_squashed = squash_spans(spans)
        exclude_count = 0
        while excludes:
            exclude = excludes.pop()
            for span in spans_squashed:
                span_start, span_end = span
                if span_start <= exclude <= span_end:
                    exclude_count += 1
                    break
        result = 0
        for span in spans_squashed:
            span_start, span_end = span
            result += span_end - span_start + 1
        return result - exclude_count
    return 0

result = get_result(data, 2_000_000)
print(result)

# Brute force
beacons = set([(line[2], line[3]) for line in data])
sensors = set([(line[0], line[1]) for line in data])
def get_result_brute(data, Y):
    memo = set()
    for ix, line in enumerate(data):
        sensor_x, sensor_y, beacon_x, beacon_y = line
        dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        if abs(sensor_y - Y) > dist:
            continue
        queue = [(sensor_x, sensor_y, 0)]
        tail = set()
        while queue:
            # x, y, length = queue.popleft()
            x, y, length = queue.pop()
            if (x, y) in tail:
                continue
            tail.add((x, y))
            if y == Y:
                if (x, y) not in beacons and (x, y) not in sensors:
                    memo.add(x)
            if length == dist:
                continue
            if y == Y:
                queue.append((x + 1, y, length + 1))
                queue.append((x - 1, y, length + 1))
            elif y < Y:
                queue.append((x, y + 1, length + 1))
            elif y > Y:
                queue.append((x, y - 1, length + 1))
        print(f'{ix + 1} out of {len(data)}')
    return len(memo)

result = get_result_brute(data, 2_000_000)
print(result)

# ------
# Part 2
# ------

def get_result_2(data, Y):
    spans = []
    excludes = set()
    for line in data:
        sensor_x, sensor_y, beacon_x, beacon_y = line
        dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        if abs(sensor_y - Y) <= dist:

            span_left = sensor_x - (dist - abs(sensor_y - Y))
            if span_left < 0:
                span_left = 0
            if span_left > 4_000_000:
                continue

            span_right = sensor_x + (dist - abs(sensor_y - Y))
            if span_right < 0:
                continue
            if span_right > 4_000_000:
                span_right = 4_000_000

            spans.append((span_left, span_right))

    spans_squashed = squash_spans(spans)
    return spans_squashed

for y in range(4_000_001):
    result = get_result_2(data, y)
    if len(result) > 1:
        first, second = result
        first_left, first_right = first
        break

result = (first_right + 1)*4_000_000 + y
print(result)
