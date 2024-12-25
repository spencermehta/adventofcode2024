import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
objects = f.split("\n\n")

locks = []
keys = []

for o in objects:
    o = o.split("\n")
    if all(c == '#' for c in o[0]):
        oo = [list(row) for row in zip(*o[1:])]
        lock = [row.count('#') for row in oo]
        locks.append(lock)
    else:
        oo = [list(row) for row in zip(*o[:len(o)-1])]
        print(oo)
        key = [row.count('#') for row in oo]
        keys.append(key)

tot = 0
for lock in locks:
    for key in keys:
        possible = True
        for column in range(len(lock)):
            if lock[column] + key[column] > 5:
                possible = False
                break
        if possible:
            tot+=1
print(tot)



