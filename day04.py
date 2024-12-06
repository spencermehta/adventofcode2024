with open("4.in") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

            # up
            # down
            # left
            # right
            # diag up left
            # diag up right
            # diag down left
            # diag down right
directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
    [-1, -1],
    [-1, 1],
    [1, -1],
    [1, 1]
]

lines = ['.' + line + '.' for line in lines]
nl = ''.join(['.' for c in lines[0]])
lines = [nl] + lines + [nl]
def part_one():
    xmases = 0
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            if lines[y][x] == "X":
                for d in directions:
                    if lines[y+d[0]][x+d[1]] == "M":
                        if lines[y+2*d[0]][x+2*d[1]] == "A":
                            if lines[y+3*d[0]][x+3*d[1]] == "S":
                                xmases += 1
    
    print(xmases)

def part_two():
    xmases = 0
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            if lines[y][x] == "A":
                if (
                        (lines[y-1][x-1] == "M" and lines[y+1][x+1] == "S") or (lines[y-1][x-1] == "S" and lines[y+1][x+1] == "M")
                        ) and (
                        (lines[y-1][x+1] == "M" and lines[y+1][x-1] == "S") or (lines[y-1][x+1] == "S" and lines[y+1][x-1] == "M")
                        ):
                            xmases += 1

    print(xmases)


part_one()
part_two()
