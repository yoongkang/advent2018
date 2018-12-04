import itertools


def chronal(data):
    return sum(map(int, data))


def chronal2(data):
    f = 0
    s = set([0])

    for i in itertools.cycle(data):
        f += int(i)
        if f in s:
            break
        s.add(f)
    return f



if __name__ == '__main__':
    with open('./data/day1.txt') as f:
        data = f.readlines()
    print(chronal(data))
    print(chronal2(data))