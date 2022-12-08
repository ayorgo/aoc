from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')
data = data.split('\n')
data = [tuple(row.split(' ')) for row in data]

# ------
# Part 1
# ------

def rpc(deal: tuple) -> int:
    match deal:
        case ['A','X']:
            return 1 + 3
        case ['A', 'Y']:
            return 2 + 6
        case ['A', 'Z']:
            return 3 + 0
        case ['B', 'X']:
            return 1 + 0
        case ['B', 'Y']:
            return 2 + 3
        case ['B', 'Z']:
            return 3 + 6
        case ['C', 'X']:
            return 1 + 6
        case ['C', 'Y']:
            return 2 + 0
        case ['C', 'Z']:
            return 3 + 3

result = sum(map(rpc, data))
print(result)

# ------
# Part 2
# ------

def rpc_inside_out(deal: tuple) -> int:
    match deal:
        case ['A','X']:
            return 3 + 0
        case ['A', 'Y']:
            return 1 + 3
        case ['A', 'Z']:
            return 2 + 6
        case ['B', 'X']:
            return 1 + 0
        case ['B', 'Y']:
            return 2 + 3
        case ['B', 'Z']:
            return 3 + 6
        case ['C', 'X']:
            return 2 + 0
        case ['C', 'Y']:
            return 3 + 3
        case ['C', 'Z']:
            return 1 + 6

result = sum(map(rpc_inside_out, data))
print(result)
