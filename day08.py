from collections import defaultdict


with open("8.in") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def p1():
    grid = [[c for c in line] for line in lines]

    coords = defaultdict(set)
    antinodes = set()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            c = grid[y][x]
            if c != '.':
                coords[c].add((x, y))

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for char in coords:
                distances = [dist((x, y), d) for d in coords[char]]
                for i in range(len(distances)):
                    for j in range(i+1, len(distances)):
                        if distances[i] == tuple_mult(2, distances[j]) or tuple_mult(2, distances[i]) == distances[j]:
                            antinodes.add((x, y))

    print(len(antinodes))


def p2():
    grid = [[c for c in line] for line in lines]

    coords = defaultdict(set)
    antinodes = set()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            c = grid[y][x]
            if c != '.':
                coords[c].add((x, y))

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for char in coords:
                distances = [dist((x, y), d) for d in coords[char]]
                for i in range(len(distances)):
                    for j in range(i+1, len(distances)):
                        x1, y1 = distances[i]
                        x2, y2 = distances[j]

                        if x1 != 0 and y1 != 0 and x2/x1 == y2/y1:
                            antinodes.add((x, y))
                        elif x2 != 0 and y2 != 0 and x1/x2 == y1/y2:
                            antinodes.add((x, y))

    print(len(antinodes))

    #s = ""
    #for y in range(len(grid)):
    #    for x in range(len(grid[0])):
    #        if (x, y) in antinodes:
    #            s += "#"
    #        else:
    #            s += '.'
    #    s += "\n"
    #print(s)


def dist(l, r):
    x1, y1 = l
    x2, y2 = r
    return ((x1-x2), (y1-y2))

def tuple_mult(n, c):
    x, y = c
    return (n*x, n*y)



p1()
p2()
