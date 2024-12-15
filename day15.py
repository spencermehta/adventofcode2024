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
        #print(move, x, y)
        dx, dy = DIRS[move]
    
        to_move = []
        to_move.append((x, y))
    
        cx = x + dx
        cy = y + dy
    
        i = 0
        while True:
            i+=1
            #if i == 100:
            #    break
            check = grid[cy][cx]
            #print(cy, cx, check)
            if check == '.':
                #print("moving")
                to_move.reverse()
                for (tmx, tmy) in to_move:
                    #print("moving ", tmx, tmy)
                    nx = tmx + dx
                    ny = tmy + dy
                    temp = grid[tmy][tmx]
                    grid[tmy][tmx] = '.'
                    grid[ny][nx] = temp
                x, y = x + dx, y + dy
                break
            elif check == '#':
                #print("not moving")
                break
            elif check == 'O':
                #print("appending")
                to_move.append((cx, cy))
                cx += dx
                cy += dy
        #pg(grid)
    print("Final:")
    pg(grid)
    print(score(grid, X, Y))

def pg(grid):
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

    

p1()
    

