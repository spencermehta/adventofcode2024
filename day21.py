import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")

directional_keypad = [
    [ None, '^', 'A'],
    [ '<', 'v', '>']
]

numerical_keypad = [
    [ '7', '8', '9'],
    [ '4', '5', '6'],
    [ '1', '2', '3'],
    [ None, '0', 'A']
]

def p1_v2():
    for line in lines:
        last_robot = (2, 3)
        intermediate_robots = [
            (2, 0),
            (2, 0),
            #(2, 0)
        ]
        last_robot_moves = ""
        intermediate_robot_moves = [
            "",
            ""
        ]

        for button in line:
            coords = get_numerical_coords(button)
            diff = tuple_diff(coords, last_robot)
            moves = get_moves(diff) + 'A'
            last_robot_moves += moves
            last_robot = coords

            for ri, ir in enumerate(intermediate_robots):
                
                while len(moves) > 0:
                    cheapest_move_i = get_cheapest_move(ir, moves)
                    cheapest_move = moves[cheapest_move_i]
                    moves = moves[:cheapest_move_i] + moves[cheapest_move_i+1:]
                    intermediate_robot_moves[ri] += cheapest_move
                    ir = get_directional_coords(cheapest_move)




def get_cheapest_move(p, moves):
    minimum = 999999
    minimum_i = -1
    for i, move in enumerate(moves):
        coords = get_directional_coords(move)
        dx, dy = tuple_diff(coords, p)
        if abs(dx) + abs(dy) < minimum:
            minimum = abs(dx) + abs(dy)
            minimum_i = i
    return minimum_i

def p1():
    tot=0
    for line in lines:
        last_robot = (2, 3)
        intermediate_robots = [
            (2, 0),
            (2, 0),
            #(2, 0)
        ]

        last_robot_moves = ""
        for button in line:
            coords = get_numerical_coords(button)
            diff = tuple_diff(coords, last_robot)
            moves = get_moves(diff) + 'A'
            last_robot_moves += moves
            last_robot = coords
            #print(f"{button=} {coords=} {diff=} {moves=}")

        print(f"{last_robot_moves=}")

        buttons_to_press = last_robot_moves
        for ir in intermediate_robots:
            robot = ir
            intermediate_moves = ""
            for button in buttons_to_press:
                coords = get_directional_coords(button)
                diff = tuple_diff(coords, robot)
                moves = get_moves(diff) + 'A'
                intermediate_moves += moves
                robot = coords

            buttons_to_press = intermediate_moves

            print(f"{buttons_to_press=}")
        num_code = int(line[:len(line)-1])
        res = num_code * len(buttons_to_press)
        print(num_code, len(buttons_to_press), res)
        tot+=res
    print(tot)



            

def get_numerical_coords(button):
    for y in range(len(numerical_keypad)):
        for x in range(len(numerical_keypad[0])):
            if numerical_keypad[y][x] == button:
                return (x,y)

def get_directional_coords(button):
    for y in range(len(directional_keypad)):
        for x in range(len(directional_keypad[0])):
            if directional_keypad[y][x] == button:
                return (x,y)

def tuple_diff(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return x1-x2, y1-y2

def get_moves(diff):
    x, y = diff
    moves = ""
    if x > 0:
        for _ in range(x):
            moves += ">"
    if y < 0:
        for _ in range(abs(y)):
            moves += "^"
    if y > 0:
        for _ in range(y):
            moves += "v"
    if x < 0:
        for _ in range(abs(x)):
            moves += "<"

    
    return moves

p1()
