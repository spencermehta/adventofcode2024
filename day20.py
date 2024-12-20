from collections import defaultdict, deque
import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")

grid = [[c for c in line] for line in lines]
Y = len(grid)
X = len(grid[0])

DIRS = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
]
        
def p1():
    sx, sy = -1, -1
    ex, ey = -1, -1

    costs = [[-1 for _ in range(X)] for _ in range(Y)]

    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 'S':
                sx, sy = x, y
            elif grid[y][x] == 'E':
                ex, ey = x, y

    q = deque()
    SEEN = set()

    q.append((ex, ey, 0))
    costs[ey][ex] = 0

    while len(q) > 0:
        (x, y, d) = q.popleft()
        if (x,y) in SEEN:
            continue
        SEEN.add((x, y))
        costs[y][x] = d

        for dx, dy in DIRS:
            cx, cy = x + dx, y + dy
            #print(cx, cy)
            if in_bounds(cx, cy, X, Y) and grid[cy][cx] == '.' or grid[cy][cx] == 'S' and (cx, cy) not in SEEN:
                q.append((cx, cy, d+1))

    savings = []

    for y in range(Y):
        for x in range(X):
            if costs[y][x] == -1:
                continue

            #print(f"{x=} {y=} {costs[y][x]}")
            for di in range(len(DIRS)):
                for dj in range(len(DIRS)):
                    dx1, dy1 = DIRS[di]
                    dx2, dy2 = DIRS[dj]

                    nx = x + dx1 + dx2
                    ny = y + dy1 + dy2
                    #print(f"{nx=} {ny=} {costs[ny][nx]}")

                    if not in_bounds(nx, ny, X, Y) or costs[ny][nx] == -1:
                        continue
                    
                    saving = costs[y][x] - costs[ny][nx] - 2
                    if saving > 0:
                        #print(f"{nx=}{ny=}{saving=}")
                        savings.append(saving)

    grouped_savings = {}
    tot = 0
    threshold = 100
    for saving in savings:
        if saving not in grouped_savings:
            grouped_savings[saving] = 0
        grouped_savings[saving] += 1

        if saving >= threshold:
            tot+=1

    #print(grouped_savings)

    print(tot)


                


            



"""
    print("\n".join(["".join(line) for line in grid]))
    s = ""
    for y in range(Y):
        for x in range(X):
            s+=str(costs[y][x]) + "\t"
        s+="\n"
    print(s)
"""
def in_bounds(x, y, X, Y):
    return x >=0 and x < X and y >= 0 and y < Y


p1()
