from pathlib import Path

path = Path(__file__).with_name('data.txt')
with path.open() as file:
    data = file.read().rstrip('\n')

data = [entry.split() for entry in data.split('\n')]
data = [(direction, int(distance)) for direction, distance in data]

class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.next = None
        self.track = set([(self.x, self.y)])

    def right(self):
        if self.next is not None:
            diff_next = (self.x - self.next.x, self.y - self.next.y)
            if diff_next == (1, -1):
                self.next.down_right()
            elif diff_next == (1, 1):
                self.next.up_right()
            elif diff_next == (1, 0):
                self.next.right()
        self.x += 1
        self.track.add((self.x, self.y))

    def left(self):
        if self.next is not None:
            diff_next = (self.x - self.next.x, self.y - self.next.y)
            if diff_next == (-1, -1):
                self.next.down_left()
            elif diff_next == (-1, 1):
                self.next.up_left()
            elif diff_next == (-1, 0):
                self.next.left()
        self.x -= 1
        self.track.add((self.x, self.y))

    def up(self):
        if self.next is not None:
            diff_next = (self.x - self.next.x, self.y - self.next.y)
            if diff_next == (1, 1):
                self.next.up_right()
            elif diff_next == (-1, 1):
                self.next.up_left()
            elif diff_next == (0, 1):
                self.next.up()
        self.y += 1
        self.track.add((self.x, self.y))

    def down(self):
        if self.next is not None:
            diff_next = (self.x - self.next.x, self.y - self.next.y)
            if diff_next == (1, -1):
                self.next.down_right()
            elif diff_next == (-1, -1):
                self.next.down_left()
            elif diff_next == (0, -1):
                self.next.down()
        self.y -= 1
        self.track.add((self.x, self.y))

    def up_right(self):
        if self.next is not None:
            diff_next = (self.x - self.next.x, self.y - self.next.y)
            if diff_next == (1, -1):
                self.next.right()
            elif diff_next == (-1, 1):
                self.next.up()
            elif diff_next in {(1, 0), (1, 1), (0, 1)}:
                self.next.up_right()
        self.x += 1
        self.y += 1
        self.track.add((self.x, self.y))

    def down_right(self):
        if self.next is not None:
            diff_next = (self.x - self.next.x, self.y - self.next.y)
            if diff_next == (1, 1):
                self.next.right()
            elif diff_next == (-1, -1):
                self.next.down()
            elif diff_next in {(1, 0), (1, -1), (0, -1)}:
                self.next.down_right()
        self.x += 1
        self.y -= 1
        self.track.add((self.x, self.y))

    def up_left(self):
        if self.next is not None:
            diff_next = (self.x - self.next.x, self.y - self.next.y)
            if diff_next == (-1, -1):
                self.next.left()
            elif diff_next == (1, 1):
                self.next.up()
            elif diff_next in {(-1, 0), (-1, 1), (0, 1)}:
                self.next.up_left()
        self.x -= 1
        self.y += 1
        self.track.add((self.x, self.y))

    def down_left(self):
        if self.next is not None:
            diff_next = (self.x - self.next.x, self.y - self.next.y)
            if diff_next == (-1, 1):
                self.next.left()
            elif diff_next == (1, -1):
                self.next.down()
            elif diff_next in {(0, -1), (-1, -1), (-1, 0)}:
                self.next.down_left()
        self.x -= 1
        self.y -= 1
        self.track.add((self.x, self.y))


def drag(head: Knot, steps: list) -> None:
    for direction, distance in steps:
        match direction:
            case 'R':
                for _ in range(distance):
                    head.right()
            case 'L':
                for _ in range(distance):
                    head.left()
            case 'U':
                for _ in range(distance):
                    head.up()
            case 'D':
                for _ in range(distance):
                    head.down()

# ------
# Part 1
# ------

head = Knot()
rope = head
for _ in range(1):
    rope.next = Knot()
    rope = rope.next
tail = rope

drag(head, data)

result = len(tail.track)
print(result)

# ------
# Part 2
# ------

head = Knot()
rope = head
for _ in range(9):
    rope.next = Knot()
    rope = rope.next
tail = rope

drag(head, data)

result = len(tail.track)
print(result)
