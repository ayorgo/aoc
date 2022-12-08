import json
from collections import namedtuple
from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')

class Directory:
    def __init__(self, name: str, parent=None, size: int = 0):
        self.name = name
        self.size = size
        self.parent = parent
        self.subdirs = []

Command = namedtuple('Command', ['name', 'args', 'output'])

def parse_log(log: str) -> dict:
    lines = log.split('\n')
    commands = []
    command_current = None
    for line in lines:
        if line.startswith('$'):
            command_line = line[2:]
            command = command_line.split()
            commands.append(Command(name=command[0], args=command[1:], output=[]))
        else:
            commands[-1].output.append(line)
    return commands

commands = parse_log(data)

# --------------
# Build the tree
# --------------

root = Directory('/')
current_dir = root
for command in commands:
    match command.name:
        case 'cd':
            match command.args[0]:
                case '/':
                    current_dir = root
                case '..':
                    current_dir = current_dir.parent
                case _:
                    new_dir = Directory(command.args[0], current_dir)
                    current_dir.subdirs.append(new_dir)
                    current_dir = new_dir
        case 'ls':
            for entry in command.output:
                first, second = entry.split()
                if first.isdigit():
                    current_dir.size += int(first)

print(json.dumps(root, indent=2, default=lambda o: {'name': o.name, 'size': o.size, 'subdirs': o.subdirs}))

# ------
# Part 1
# ------

sizes = []
nodes = [(root, False)]
while nodes:
    node, been_here = nodes.pop()
    if been_here:
        if node.size <= 100_000:
            sizes.append(node.size)
        if node.parent is not None:
            node.parent.size += node.size
        continue
    nodes.append((node, True))
    if node.subdirs:
        nodes.extend([(subdir, False) for subdir in node.subdirs])

result = sum(sizes)
print(result)

# ------
# Part 2
# ------

sizes = []
nodes = [root]
while nodes:
    node = nodes.pop()
    if node.size >= 30_000_000 - (70_000_000 - root.size):
        sizes.append(node.size)
    nodes.extend(node.subdirs)

result = min(sizes)
print(result)
