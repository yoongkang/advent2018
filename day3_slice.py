import re
from collections import defaultdict

PATTERN = re.compile(r'#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)')


def get_cells(x_s, y_s, w, h):
    for x in range(x_s, x_s + w):
        for y in range(y_s, y_s + h):
            yield (x, y)


def build_cells(data):
    cells = defaultdict(lambda: tuple())
    for r in data:
        id_, x_s, y_s, w, h = [int(x) for x in PATTERN.match(r).groups()]
        for x, y in get_cells(x_s, y_s, w, h):
            cells[(x, y)] += (id_,)
    return cells


def run_slice(data):
    cells = build_cells(data)
    return sum(1 for v in cells.values() if len(v) > 1)


def run_slice2(data):
    cells = build_cells(data)
    for r in data:
        id_, x_s, y_s, w, h = [int(x) for x in PATTERN.match(r).groups()]
        if all(len(cells[(x, y)]) == 1 for x, y in get_cells(x_s, y_s, w, h)):
            return id_



if __name__ == '__main__':
    with open('./data/day3.txt') as f:
        data = f.readlines()
    print(run_slice(data))
    print(run_slice2(data))

