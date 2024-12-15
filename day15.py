import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
warehouse, moves = f.split("\n\n")
warehouse = warehouse.split("\n")
grid = [[c for c in line] for line in warehouse]
moves = moves.replace("\n", "")
Y = len(grid)
X = len(grid[0])

DIRS = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0)
}

def p1():
    start = (-1, -1)
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == '@':
                start = (x, y)
    x, y = start
    
    for move in moves:
        dx, dy = DIRS[move]
    
        to_move = []
        to_move.append((x, y))
    
        cx = x + dx
        cy = y + dy
    
        while True:
            check = grid[cy][cx]
            if check == '.':
                to_move.reverse()
                for (tmx, tmy) in to_move:
                    nx = tmx + dx
                    ny = tmy + dy
                    temp = grid[tmy][tmx]
                    grid[tmy][tmx] = '.'
                    grid[ny][nx] = temp
                x, y = x + dx, y + dy
                break
            elif check == '#':
                break
            elif check == 'O':
                to_move.append((cx, cy))
                cx += dx
                cy += dy
    print(score(grid, X, Y))

def p2():
    grid = [[c for c in line] for line in warehouse]
    G = [['' for _ in range(X*2)] for _ in range(Y)]


    start = (-1, -1)
    for y in range(Y):
        for x in range(X):
            v = grid[y][x]
            if v == '#':
                G[y][2*x] = '#'
                G[y][2*x+1] = '#'
            elif v == 'O':
                G[y][2*x] = '['
                G[y][2*x+1] = ']'
            elif v == '.':
                G[y][2*x] = '.'
                G[y][2*x+1] = '.'
            elif v == '@':
                G[y][2*x] = '@'
                start = (2*x, y)
                G[y][2*x+1] = '.'
    XX, YY = X*2, Y

    x, y = start

    for i, move in enumerate(moves):
        PG = [[G[i][j] for j in range(XX)] for i in range(YY)]
        dx, dy = DIRS[move]
        d = (dx, dy)

        if d == (1,0) or d == (-1,0):
            to_move = []
            to_move.append((x, y))

            cx = x + dx
            cy = y + dy

            while True:
                check = G[cy][cx]
                if check == '.':
                    to_move.reverse()
                    for (tmx, tmy) in to_move:
                        nx = tmx + dx
                        ny = tmy + dy
                        temp = G[tmy][tmx]
                        G[tmy][tmx] = '.'
                        G[ny][nx] = temp
                    x, y = x + dx, y + dy
                    break
                elif check == '#':
                    break
                elif check == '[' or check == ']':
                    to_move.append((cx, cy))
                    cx += dx
                    cy += dy
        else:
            to_move = []
            to_move.append((x, y))
            check_coords = {(x + dx, y + dy)}

            not_found_hash = True
            while not_found_hash:
                all_empty = True
                ccs = [cc for cc in check_coords]
                for cx, cy in ccs:
                    check = G[cy][cx]
                    if check == '.':
                        check_coords.remove((cx, cy))
                    elif check == '[':
                        all_empty = False
                        to_move.append((cx, cy))
                        to_move.append((cx+1, cy))
                        check_coords.add((cx+1, cy))
                    elif check == ']':
                        all_empty = False
                        to_move.append((cx, cy))
                        to_move.append((cx-1, cy))
                        check_coords.add((cx-1, cy))
                    elif check == '#':
                        all_empty = False
                        not_found_hash = False
                        break
                if all_empty:
                    new = set()
                    new_with_v = set()
                    for (tmx, tmy) in to_move:
                        nx = tmx + dx
                        ny = tmy + dy
                        v = G[tmy][tmx]
                        new.add((nx, ny))
                        new_with_v.add((nx, ny, v))

                    for (nx, ny, v) in new_with_v:
                        G[ny][nx] = v

                    for (tmx, tmy) in to_move:
                        if (tmx, tmy) not in new:
                            G[tmy][tmx] = '.'

                    x, y = x + dx, y + dy
                    break
                else:
                    check_coords = {(cx + dx, cy + dy) for cx, cy in check_coords}
            """
            if len(to_move) > 1 and not_found_hash:
                print("before")
                pg(PG, XX, YY)
                print("after")
                pg(G, XX, YY)
            """

    print(score2(G, XX, YY))

def pg(grid, X, Y):
    s = ""
    for y in range(Y):
        for x in range(X):
            s += grid[y][x]
        s+="\n"
    print(s)

def score(grid, X, Y):
    tot = 0
    for y in range(Y):
        for x in range(X):
            v = grid[y][x]
            if v == 'O':
                p = (100 * y) + x
                tot += p
    return tot

def score2(grid, X, Y):
    tot = 0
    for y in range(Y):
        for x in range(X):
            v = grid[y][x]
            if v == '[':
                p = (100 * y) + x
                tot += p
    return tot

    

p1()
p2()
    

