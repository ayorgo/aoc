from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')

def parse_stacks(stacks: str) -> list:
    stacks_shrinked = [stack.replace('    ', '[-]').replace(' ', '').replace('[', '').replace(']', '') for stack in stacks.split('\n')[::-1]]
    stack_numbers = stacks_shrinked.pop(0)
    stacks_pivoted = []
    for _ in stack_numbers:
        stacks_pivoted.append([])
    for level in stacks_shrinked:
        for stack, crate in enumerate(level):
            if crate != '-':
                stacks_pivoted[stack].append(crate)
    return stacks_pivoted

def parse_instructions(instructions: str) -> list:
    return [list(map(lambda i: int(instruction.split(' ')[i]), [1, 3, 5])) for instruction in instructions.split('\n')]

# ------
# Part 1
# ------

stacks, instructions = data.split('\n\n')
stacks = parse_stacks(stacks)
instructions = parse_instructions(instructions)
for count, source, destination in instructions:
    crane_hook = [stacks[source - 1].pop() for _ in range(count)]
    stacks[destination - 1].extend(crane_hook)

result = ''.join([stack[-1] for stack in stacks])
print(result)

# ------
# Part 2
# ------

stacks, instructions = data.split('\n\n')
stacks = parse_stacks(stacks)
instructions = parse_instructions(instructions)
for count, source, destination in instructions:
    crane_hook = [stacks[source - 1].pop() for _ in range(count)]
    stacks[destination - 1].extend(reversed(crane_hook))

result = ''.join([stack[-1] for stack in stacks])
print(result)
