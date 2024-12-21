from collections import deque
from itertools import product
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

DIRS = {
    '>': (1, 0),
    '<': (-1, 0),
    '^': (0, -1),
    'v': (0, 1)
}

def get_keypad_paths(keypad):
    buttons = {}
    for y in range(len(keypad)):
        for x in range(len(keypad[0])):
            if keypad[y][x] is None:
                continue
            buttons[keypad[y][x]] = (x, y)

    sequences = {}
    for button1 in buttons:
        for button2 in buttons:
            if button1 == button2:
                sequences[(button1, button2)] = ["A"]
                continue

            possible_sequences = []
            q = deque()
            q.append((buttons[button1], ""))
            best_len = 9999
            exceeded_best_len = False

            while len(q) > 0 and not exceeded_best_len:
                (x,y), current_seq = q.popleft()

                for d in DIRS:
                    dx, dy = DIRS[d]
                    nx, ny = x + dx, y + dy

                    if in_bounds(nx, ny, len(keypad[0]), len(keypad)) and keypad[ny][nx] is not None:
                        if (nx, ny) == buttons[button2]:
                            possible_sequences.append(current_seq + d + "A")
                            best_len = len(current_seq+d)
                        if len(current_seq+d) > best_len:
                            exceeded_best_len = True
                            break
                        q.append(((nx, ny), current_seq+d))

            sequences[(button1, button2)] = possible_sequences

    return sequences

def in_bounds(x, y, X, Y):
    return x >= 0 and x < X and y >= 0 and y < Y

numerical_keypad_paths = get_keypad_paths(numerical_keypad)
directional_keypad_paths = get_keypad_paths(directional_keypad)

def compute(paths):
    path_map = {}
    for path in list(product(*paths)):
        path = "".join(path)
        movements = list(zip("A" + path, path))

        possible_paths = []
        for movement in movements:
            paths = directional_keypad_paths[movement]
            possible_paths.append(paths)
        path_map[path] = possible_paths
    return path_map

def p1():
    tot = 0
    for line in lines:
        movements = list(zip("A" + line, line))
        possible_paths = []
        for movement in movements:
            paths = numerical_keypad_paths[movement]
            possible_paths.append(paths)
        pm = compute(possible_paths)
        minimum = float("+inf")

        for p in pm:
            pm2 = compute(pm[p])
            for p2 in pm2:
                for path in list(product(*pm2[p2])):
                    path = "".join(path)
                    if len(path) < minimum:
                        minimum = len(path)

        ans = minimum * int(line[:len(line)-1])
        tot += ans

    print(tot)

C = {}
def compute2(x, y, d):
    if (x, y, d) in C:
        return C[(x,y,d)]
    
    if d == 1:
        return len(directional_keypad_paths[(x,y)][0])

    minimum = float("inf")
    for path in directional_keypad_paths[(x,y)]:
        l = 0
        for (nx, ny) in list(zip("A" + path, path)):
            l += compute2(nx, ny, d-1)
        if l < minimum:
            minimum = l
    C[(x,y,d)] = minimum
    return minimum

def p2():
    tot = 0
    robots = 24
    for line in lines:
        movements = list(zip("A" + line, line))
        possible_paths = []
        for movement in movements:
            paths = numerical_keypad_paths[movement]
            possible_paths.append(paths)
        pm = compute(possible_paths)
        minimum = float("+inf")

        for p in pm:
            for path in list(product(*pm[p])):
                path = "".join(path)
                movements = list(zip("A" + path, path))
                l = 0
                for (x,y) in movements:
                    l += compute2(x, y, robots)
                if l < minimum:
                    minimum = l

        ans = minimum * int(line[:len(line)-1])
        tot += ans
    print(tot)
            

p1()
p2()
