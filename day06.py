with open("6.in") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]


directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
]

def part_one():
    grid = [[c for c in line] for line in lines]
    start = (-1, -1)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            cell = lines[y][x]
            if cell == '^':
                start = (y, x)
                break
    

    direction = directions[0]
    position = start

    while True:
        grid[position[0]][position[1]] = 'X'
        next_position = add_tuples(position, direction)
        if (next_position[0] >= len(grid) or next_position[0] < 0 or next_position[1] >= len(grid[0]) or next_position[1] < 0):
            break
        if grid[next_position[0]][next_position[1]] == '#':
            direction = directions[(directions.index(direction) + 1) % len(directions)] 
            next_position = add_tuples(position, direction)
        position = next_position

    cells_stepped = count_cells(grid)
    print(cells_stepped)
    return grid

def part_two():
    grid = [[c for c in line] for line in lines]
    dirgrid = [[[] for _ in line] for line in lines]
    start = (-1, -1)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            cell = lines[y][x]
            if cell == '^':
                start = (y, x)
                break
    

    direction = directions[0]
    position = start
    loopable = 0

    while True:
        grid[position[0]][position[1]] = 'X'
        dirgrid[position[0]][position[1]].append(direction)
        #print(print_grid(grid), "\n")
        if would_loop(position, direction, grid, dirgrid):
            loopable += 1 
            print("at ", position)
            print(print_grid(grid), "\n")
        next_position = add_tuples(position, direction)
        if not in_bounds(next_position, grid):
            break
        while grid[next_position[0]][next_position[1]] == '#':
            direction = directions[(directions.index(direction) + 1) % len(directions)] 
            next_position = add_tuples(position, direction)
        position = next_position

    print(loopable)

def would_loop(position, direction, walked_grid, dirgrid):
    pos_to_block = add_tuples(position, direction)
    if not in_bounds(pos_to_block, walked_grid) or walked_grid[pos_to_block[0]][pos_to_block[1]] == 'X' or walked_grid[pos_to_block[0]][pos_to_block[1]] == '#':
        return False
    new_direction = directions[(directions.index(direction) + 1) % len(directions)] 
    new_pos = add_tuples(position, new_direction)
    while walked_grid[new_pos[0]][new_pos[1]] == '#':
        new_direction = directions[(directions.index(new_direction) + 1) % len(directions)] 
        new_pos = add_tuples(position, direction)
    while in_bounds(new_pos, walked_grid):
        if walked_grid[new_pos[0]][new_pos[1]] == '#':
            return False
        if walked_grid[new_pos[0]][new_pos[1]] == 'X' and new_direction in dirgrid[new_pos[0]][new_pos[1]]:
            print("can block ", pos_to_block)
            return True
        new_pos = add_tuples(new_pos, new_direction)
        
    return False

def in_bounds(position, grid):
    return not (position[0] >= len(grid) or position[0] < 0 or position[1] >= len(grid[0]) or position[1] < 0)


def add_tuples(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])

def count_cells(grid):
    cells = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            cell = grid[y][x]
            if cell == 'X':
                cells += 1
    return cells


def print_grid(grid):
    lines = []
    for y in range(len(grid)):
        line = ""
        for x in range(len(grid[0])):
            cell = grid[y][x]
            line += cell
        lines.append(line)
    return "\n".join(lines)

def part_two_v2():
    loopables = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            grid = [[c for c in line] for line in lines]
            if grid[y][x] == '.':
                grid[y][x] = '#'
                loops = simulate(grid)
                if loops:
                    loopables += 1
    print(loopables)



def simulate(grid):
    dirgrid = [[[] for _ in line] for line in lines]
    start = (-1, -1)
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            cell = lines[y][x]
            if cell == '^':
                start = (y, x)
                break
    

    direction = directions[0]
    position = start

    while True:
        if grid[position[0]][position[1]] == 'X' and direction in dirgrid[position[0]][position[1]]:
            return True
        grid[position[0]][position[1]] = 'X'
        dirgrid[position[0]][position[1]].append(direction)

        next_position = add_tuples(position, direction)
        if not in_bounds(next_position, grid):
            break
        while grid[next_position[0]][next_position[1]] == '#':
            direction = directions[(directions.index(direction) + 1) % len(directions)] 
            next_position = add_tuples(position, direction)
        position = next_position

    return False

part_one()
part_two_v2()
