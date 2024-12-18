from collections import deque
import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")
points = []
for line in lines:
    x,y = line.split(',')
    points.append((int(x), int(y)))

DIRS = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
]

X = 7
Y = 7
X = 71
Y = 71
bytes_to_plot = 1024

def p1():
    sx, sy = 0, 0
    ex, ey = X-1, Y-1

    grid = [['.' for _ in range(X)] for _ in range(Y)]

    for point in points[:bytes_to_plot]:
        plot(point, grid)

    print("\n".join(["".join(line) for line in grid]))

    bfs((sx, sy), (ex, ey), grid, X, Y)

def p2():
    sx, sy = 0, 0
    ex, ey = X-1, Y-1

    grid = [['.' for _ in range(X)] for _ in range(Y)]

    for point in points:
        plot(point, grid)
        res = bfs((sx, sy), (ex, ey), grid, X, Y)
        if res == -1:
            print(point)
            return



def bfs(start, end, grid, X, Y):
    sx, sy = start
    ex, ey = end

    q = deque()
    q.append((sx, sy, 0))

    SEEN = set()

    while len(q) > 0:
        x, y, d = q.popleft()
        if (x,y) in SEEN:
            continue

        SEEN.add((x,y))

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            
            if in_bounds(nx,ny, X, Y) and grid[ny][nx] == '.' and (nx, ny) not in SEEN:
                if (nx,ny) == (ex, ey):
                    return d+1
                q.append((nx, ny, d+1))
    return -1
    
def in_bounds(x,y,X,Y):
    return x >= 0 and x < X and y >= 0 and y < Y

def plot(point, grid):
    x, y = point
    grid[y][x] = '#'

p1()
p2()
