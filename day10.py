from collections import deque


with open("10.in") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def p1():
    grid = [[int(c) for c in line] for line in lines]
    trailheads = []
    Y = len(grid)
    X = len(grid[0])

    print_grid(grid)

    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 0:
                trailheads.append((x, y))

    tot = 0
    for trailhead in trailheads:
        print(f"starting at {trailhead=}")
        ends = bfs(trailhead, grid, X, Y)
        tot += len(ends)
    print(tot)

def p2():
    grid = [[int(c) for c in line] for line in lines]
    trailheads = []
    Y = len(grid)
    X = len(grid[0])

    print_grid(grid)

    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 0:
                trailheads.append((x, y))

    tot = 0
    for trailhead in trailheads:
        print(f"starting at {trailhead=}")
        ends = bfs2(trailhead, grid, X, Y)
        tot += ends
    print(tot)


DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

def bfs(trailhead, grid, X, Y):
    Q = deque()
    Q.append(trailhead)
    ends = set()
    while len(Q) > 0:
        (x, y) = Q.pop()
        #print(f"{x=} {y=} {Q=}")
        val = grid[y][x]

        for d in DIRS:
            c = add_coords((x, y), d)
            xc, yc = c
            cv = grid[yc][xc] if in_bounds(c, X, Y) else None
            #print(f"{c=} {cv=}")
            if in_bounds(c, X, Y) and cv == val+1:
                if cv == 9:
                    ends.add(c)
                else:
                    Q.append(c)
    return ends

def bfs2(trailhead, grid, X, Y):
    Q = deque()
    Q.append(trailhead)
    ends = 0
    while len(Q) > 0:
        (x, y) = Q.pop()
        #print(f"{x=} {y=} {Q=}")
        val = grid[y][x]

        for d in DIRS:
            c = add_coords((x, y), d)
            xc, yc = c
            cv = grid[yc][xc] if in_bounds(c, X, Y) else None
            #print(f"{c=} {cv=}")
            if in_bounds(c, X, Y) and cv == val+1:
                if cv == 9:
                    ends += 1
                else:
                    Q.append(c)
    return ends



def add_coords(one, two):
    x1, y1 = one
    x2, y2 = two
    return (x1 + x2, y1 + y2)

def in_bounds(coord, X, Y):
    x, y = coord
    return x >= 0 and x < X and y >= 0 and y < Y

def print_grid(grid):
    s = ""
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            s+=str(grid[y][x])
        s+="\n"
    print(s)


p1()
p2()
