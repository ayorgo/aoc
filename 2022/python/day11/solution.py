import re
from math import prod
import heapq
from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')

# Fix the inconsistent formatting
data = re.sub(r'Monkey (\d)(:)', r'Monkey\2 \1', data)

data = data.split('\n\n')

class Monkey:
    def __init__(self, monkey_raw: str):
        monkey_semi = [tuple(piece.strip() for piece in line.split(':')) for line in monkey_raw.split('\n')]
        for item in monkey_semi:
            match item:
                case ('Monkey', name):
                    self.name = name
                case ('Starting items', items):
                    self.items = [int(worry) for worry in items.split(', ')]
                case ('Operation', op):
                    self.inspect = lambda old: eval(op.replace('new = ', ''))
                case ('Test', expr):
                    self.divisible_by = int(re.search(r'\d+', expr).group(0))
                case ('If true', throw_true):
                    self.if_true = re.search(r'\d+', throw_true).group(0)
                case ('If false', throw_false):
                    self.if_false = re.search(r'\d+', throw_false).group(0)

        self.test = lambda x: self.if_true if x % self.divisible_by == 0 else self.if_false
        self.inspected = 0

def process_round(monkeys: list, manage_worry = lambda x: x) -> None:
    monkeys_hashed = {monkey.name: monkey for monkey in monkeys}
    for monkey in monkeys:
        monkey.items = [manage_worry(monkey.inspect(item)) for item in monkey.items]
        throws = [(monkey.test(item), item) for item in monkey.items]
        monkey.inspected += len(throws)
        monkey.items = []
        for throw_to_monkey, item in throws:
            monkeys_hashed[throw_to_monkey].items.append(item)

def calculate_monkey_business(monkeys, n=2):
    inspected = [monkey.inspected for monkey in monkeys]
    heapq.heapify(inspected)
    return prod(heapq.nlargest(n, inspected))

# ------
# Part 1
# ------

monkeys = [Monkey(monkey_raw) for monkey_raw in data]

for _ in range(20):
    process_round(monkeys, lambda x: int(x/3))

result = calculate_monkey_business(monkeys)
print(result)

# ------
# Part 2
# ------

monkeys = [Monkey(monkey_raw) for monkey_raw in data]

modulo = prod(monkey.divisible_by for monkey in monkeys)
for _ in range(10_000):
    process_round(monkeys, lambda x: x % modulo)

result = calculate_monkey_business(monkeys)
print(result)
