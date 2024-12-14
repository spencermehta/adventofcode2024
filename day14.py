import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def p1():
    iters = 100
    X = 11
    Y = 7
    X = 101
    Y = 103
    quartiles = {(x, y): 0 for x in range(2) for y in range(2)}

    for line in lines:
        point, velocity = line.split(' ')
        _, x, y = point.replace('=', ',').split(',')
        x, y = int(x), int(y)
        _, vx, vy = velocity.replace('=', ',').split(',')
        vx, vy = int(vx), int(vy)

        fx = (x + (iters * vx)) % X
        fy = (y + (iters * vy)) % Y
        xm = X // 2
        ym = Y // 2
        
        #print(x, y, vx, vy, fx, fy)
        if fx == xm or fy == ym:
            continue
        qx = 0 if fx < xm else 1
        qy = 0 if fy < ym else 1
        quartiles[(qx, qy)] += 1
    
    #print(quartiles)
    prod = 1
    for q in quartiles:
        prod *= quartiles[q]
    print(prod)

def p2():
    X = 11
    Y = 7
    X = 101
    Y = 103

    points = []
    for line in lines:
        point, velocity = line.split(' ')
        _, x, y = point.replace('=', ',').split(',')
        x, y = int(x), int(y)
        _, vx, vy = velocity.replace('=', ',').split(',')
        vx, vy = int(vx), int(vy)
        points.append((x, y, vx, vy))

    iters = 0
    while True:
        check_on_coords = set()
        iters+=1
        for point in points:
            x, y, vx, vy = point

            fx = (x + (iters * vx)) % X
            fy = (y + (iters * vy)) % Y
            check_on_coords.add((fx, fy))

        if len(points) == len(check_on_coords):
            print(len(points), len(check_on_coords), iters)

p1()
p2()
