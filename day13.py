import sys
import numpy as np

file_name = sys.argv[1]
with open(file_name) as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
sys.setrecursionlimit(10**6)

def p1():
    machines = []
    for i in range(0, len(lines), 4):
        sp = lines[i].split()
        ax = int(sp[2].replace(',', '').split('+')[1])
        ay = int(sp[3].replace(',', '').split('+')[1])

        sp = lines[i+1].split()
        bx = int(sp[2].replace(',', '').split('+')[1])
        by = int(sp[3].replace(',', '').split('+')[1])

        sp = lines[i+2].split()
        tx = int(sp[1].replace(',', '').split('=')[1])
        ty = int(sp[2].replace(',', '').split('=')[1])

        machine = ((ax, ay), (bx, by), (tx, ty))
        machines.append(machine)
    print(machines)

    tot = 0

    for machine in machines:
        ((ax, ay), (bx, by), (cx, cy)) = machine
        cost = {}
        cost[(0, 0)] = 0
        for num_a in range(101):
            for num_b in range(101):
                
                #print(num_a, num_b)

                final_x = num_a * ax + num_b * bx
                final_y = num_a * ay + num_b * by
                c = num_a * 3 + num_b
                if (final_x, final_y) in cost:
                    prev_c = cost[(final_x, final_y)]
                    if c < prev_c:
                        cost[(final_x, final_y)] = c
                else:
                    cost[(final_x, final_y)] = c

        if (cx, cy) in cost:
            tot += cost[(cx, cy)]

    print(tot)

def p2():
    machines = []
    for i in range(0, len(lines), 4):
        sp = lines[i].split()
        ax = int(sp[2].replace(',', '').split('+')[1])
        ay = int(sp[3].replace(',', '').split('+')[1])

        sp = lines[i+1].split()
        bx = int(sp[2].replace(',', '').split('+')[1])
        by = int(sp[3].replace(',', '').split('+')[1])

        sp = lines[i+2].split()
        tx = int(sp[1].replace(',', '').split('=')[1]) + 10000000000000
        ty = int(sp[2].replace(',', '').split('=')[1]) + 10000000000000

        machine = ((ax, ay), (bx, by), (tx, ty))
        machines.append(machine)
    print(machines)

    tot = 0

    for machine in machines:
        ((ax, ay), (bx, by), (cx, cy)) = machine
        a = np.array([[ax, bx], [ay, by]])
        b = [[cx], [cy]]
        res = np.linalg.solve(a, b)
        aa = round(res[0,0])
        bb = round(res[1,0])

        if aa * ax + bb * bx == cx and aa * ay + bb * by == cy:
            tot += 3 * aa + bb

    print(tot)
MC = {}

p1()
p2()
