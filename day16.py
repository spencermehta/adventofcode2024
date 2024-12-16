from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")
grid = [[c for c in line] for line in lines]
X = len(grid[0])
Y = len(grid)

DIRS = [
    (1, 0), # right
    (0, -1), # up
    (-1, 0), # left
    (0, 1) # down
]

DIR_TO_C = {
    (1,0): 'R',
    (0, -1): 'U',
    (-1, 0): 'L',
    (0, 1): 'D'
}

def p1():
    start = (-1, -1)
    end = (-1, -1)
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 'S':
                start = (x, y)
            elif grid[y][x] == 'E':
                end = (x, y)

    q = []
    x, y = start
    q.append((x, y, 1, 0, 0))

    visited = set()
    distances = {}

    while len(q) > 0:
        (x, y, fx, fy, d) = get_min(q)

        if (x,y) in visited:
            continue
        visited.add((x,y))

        for dx, dy in  DIRS:
            ddx, ddy = abs(dx-fx), abs(dy-fy)
            cost = d + (max(ddx, ddy) * 1000) + 1


            xp, yp = x + dx, y + dy
            if grid[yp][xp] == '.' or grid[yp][xp] == 'E':
                if (xp, yp) not in distances or cost < distances[(xp, yp)]:
                    distances[(xp, yp)] = cost
                    q.append((xp, yp, dx, dy, cost))

    print(distances[end])

def p2():
    start = (-1, -1)
    end = (-1, -1)
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 'S':
                start = (x, y)
            elif grid[y][x] == 'E':
                end = (x, y)

    q = []
    x, y = start
    q.append((x, y, 1, 0, 0))

    distances = {}
    prevs = defaultdict(set)

    while len(q) > 0:
        (x, y, fx, fy, d) = get_min(q)

        for dx, dy in  DIRS:
            ddx, ddy = abs(dx-fx), abs(dy-fy)
            cost = d + (max(ddx, ddy) * 1000) + 1


            xp, yp = x + dx, y + dy
            if grid[yp][xp] == '.' or grid[yp][xp] == 'E':
                if (xp, yp, dx, dy) not in distances or cost < distances[(xp, yp, dx, dy)]:
                    distances[(xp, yp, dx, dy)] = cost
                    prevs[(xp,yp, dx, dy)].add((x,y, fx, fy))
                    q.append((xp, yp, dx, dy, cost))
                elif (xp, yp, dx, dy) in distances and cost == distances[(xp, yp, dx, dy)]:
                    prevs[(xp,yp, dx, dy)].add((x,y, fx, fy))
                    q.append((xp, yp, dx, dy, cost))
    
    a = (end[0], end[1], 0, 1)
    b = (end[0], end[1], 0, -1)
    c = (end[0], end[1], 1, 0)
    d = (end[0], end[1], -1, 0)
    minimum = 10**9
    letter = a
    if a in distances:
        distt = distances[a]
        if distt < minimum:
            minimum = distt
            letter = a
    if b in distances:
        distt = distances[b]
        if distt < minimum:
            minimum = distt
            letter = b
    if c in distances:
        distt = distances[c]
        if distt < minimum:
            minimum = distt
            letter = c
    if d in distances:
        distt = distances[d]
        if distt < minimum:
            minimum = distt
            letter = d

    coords = set()

    cq = deque()
    cq.append(letter)
    while len(cq) > 0:
        nx, ny, ndx, ndy = cq.popleft()
        coords.add((nx, ny))
        pvs = prevs[(nx, ny, ndx, ndy)]
        for pv in pvs:
            cq.append(pv)
    print(len(coords))

    """
    s = ""
    for y in range(Y):
        for x in range(X):
            if (x,y) in coords:
                s += 'O'
            else:
                s += grid[y][x]
        s+= '\n'
    print(s)
    """

def get_min(q):
    m = 10**9
    mi = -1
    for i, (x, y, fx, fy, d) in enumerate(q):
        if d < m:
            m = d
            mi = i

    e = q[mi]
    del q[mi]
    return e

p1()
p2()
