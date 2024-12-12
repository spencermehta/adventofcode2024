from collections import deque


with open("12.in") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def p1():
    grid = [[c for c in line] for line in lines]
    coords = set()
    Y = len(grid)
    X = len(grid[0])

    for y in range(Y):
        for x in range(X):
            coords.add((x, y))

    plots = []
    while len(coords) > 0:
        c = coords.pop()
        plot = bfs(c, grid, X, Y)
        plots.append(plot)
        for co in plot:
            if co in coords:
                coords.remove(co)

    tot = 0
    tot2 = 0
    for plot in plots:
        a = area(plot)
        p = perimeter(plot, grid, X, Y)
        s = sides(plot, grid, X, Y)
        price = a * p
        price2 = a * s
        tot += price
        tot2 += price2
    print(tot)
    print(tot2)

def bfs(start, grid, X, Y):
    Q = deque()
    Q.append(start)

    sx, sy = start
    plant = grid[sy][sx]
    plot = set()
    plot.add(start)
    SEEN = set()

    while len(Q) > 0:
        (x, y) = Q.pop()
        SEEN.add((x, y))
        plot.add((x, y))

        for d in DIRS:
            c = add_coords((x, y), d)
            xc, yc = c
            v = grid[yc][xc] if in_bounds(c, X, Y) else None
            if c not in SEEN and v == plant:
                Q.append(c)
    return plot


DIRS = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

def sides(plot, grid, X, Y):
    side_grid = [[[] for _ in range(X)] for _ in range(Y)]
    for c in plot:
        sides = get_sides_of_point(c, grid, X, Y)
        side_grid[c[1]][c[0]] = sides

    side_count = 0
    for (x, y) in plot:
        for line in side_grid[y][x]:
            (xx, yy) = line
            if yy == None:
                xn, yn = add_coords((x, y), (0, 1))
                if not in_bounds((xn, yn), X, Y) or line not in side_grid[yn][xn]:
                    side_count += 1
            elif xx == None:
                xn, yn = add_coords((x, y), (1, 0))
                if not in_bounds((xn, yn), X, Y) or line not in side_grid[yn][xn]:
                    side_count += 1
    return side_count


def get_sides_of_point(c, grid, X, Y):
    lines = set()
    x, y = c
    plant = grid[y][x]
    for d in DIRS:
        co = add_coords((x, y), d)
        xco, yco = co
        v = grid[yco][xco] if in_bounds(co, X, Y) else None
        if v != plant:
            line = get_line(c, d)
            lines.add(line)
    return lines

def perimeter(plot, grid, X, Y):
    perimeter = 0
    
    for c in plot:
        x, y = c
        plant = grid[y][x]
        for d in DIRS:
            co = add_coords((x, y), d)
            xco, yco = co
            v = grid[yco][xco] if in_bounds(co, X, Y) else None
            
            if v != plant:
                perimeter += 1
    return perimeter

def area(plot):
    return len(plot)

def add_coords(one, two):
    x1, y1 = one
    x2, y2 = two
    return (x1 + x2, y1 + y2)

def get_line(c, d):
    x, y = c
    dx, dy = d
    if dx == 0:
        if dy == -1:
            line = (None, y)
        else:
            line = (None, y+1)
    else:
        if dx == -1:
            line = (x, None)
        else:
            line = (x+1, None)

    return line

def in_bounds(coord, X, Y):
    x, y = coord
    return x >= 0 and x < X and y >= 0 and y < Y


def pg(grid):
    s = ""
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            s += str(grid[y][x])
        s += "\n"
    print(s)

p1()
