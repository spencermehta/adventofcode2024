import sys
from collections import deque
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
initials, rules = f.split("\n\n")
initials = initials.split("\n")
rules = rules.split("\n")

initials = [i.replace(" ", '').split(":") for i in initials]
initials = [(x[0], (int(x[1]))) for x in initials]

values = {}
for x,y in initials:
    values[x] = y

operations = []
ops = {}
for rule in rules:
    s = rule.split(" ")
    left = s[0]
    op = s[1]
    right = s[2]
    out = s[4]
    operations.append((left, op, right, out))
    ops[out] = (op, left, right)

def p1():
    q = deque()
    for operation in operations:
        q.append(operation)
    while len(q) > 0:
        operation = q.popleft()
        left, op, right, out = operation
        if left not in values or right not in values:
            q.append(operation)
            continue
        vl = values[left] 
        vr = values[right] 
        if op == "AND":
            res = vl and vr
            values[out] = res
        elif op == "OR":
            res = vl or vr
            values[out] = res 
        elif op == "XOR":
            res = vl ^ vr 
            values[out] = res
        else:
            raise Exception("err")

    ans = [0 for _ in range(64)]
    for k in values:
        if k[0] == "z":
            num = int(k[1:])
            v = values[k]
            ans[num] = v
    ans.reverse()
    anss = int("".join([str(x) for x in ans]), 2)
    print(anss)

def p2():
    print(pp("z00"))

    for i in range(44):
        s = ["0" for _ in range(44)]
        s[i] = "1"
        bin_num = int(s, 2)

def ppp(wire):
    print(pp(wire))

def pp(wire, d=0):
    if wire[0] in "xy":
        return d * "  " + wire
    
    op, left, right = ops[wire]
    return d * "  " + op + "(" + wire + ")\n" + pp(left, d+1) + "\n" + pp(right, d+1)

#p1()
p2()
