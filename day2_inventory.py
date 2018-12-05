from collections import Counter


def inventory2(data):
    for a in data:
        for b in data:
            diff = sum(1 for x, y in zip(a, b) if x != y)
            if diff == 1:
                return "".join(x for x, y in zip(a, b) if x == y)


def inventory(data):
    count2, count3 = 0, 0
    for d in data:
        counter = Counter(d)
        if any((c == 3 for c in counter.values())):
            count3 += 1
        if any((c == 2 for c in counter.values())):
            count2 += 1
    return count2 * count3


if __name__ == '__main__':
    with open('./data/day2.txt') as f:
        data = f.readlines()
    print(inventory(data))
    print(inventory2(data))