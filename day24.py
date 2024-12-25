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
    pairs = [
        ("thm", "z08"),
        ("wrm", "wss"),
        ("hwq", "z22"),
        ["gbs", "z29"]

    ]

    for l,r in pairs:
        swap(l, r)

    i = 0
    while True:
        if not verify(i):
            break
        i+=1
    print(i)

    all_pairs = []
    for l,r in pairs:
        all_pairs.append(l)
        all_pairs.append(r)
    print(",".join(sorted(all_pairs)))
def swap(left, right):
    temp = ops[left]
    ops[left] = ops[right]
    ops[right] = temp

def ppp(num):
    print(pp(make_wire("z", num)))

def pp(wire, d=0):
    if wire[0] in "xy":
        return d * "  " + wire
    
    op, left, right = ops[wire]
    return d * "  " + op + "(" + wire + ")\n" + pp(left, d+1) + "\n" + pp(right, d+1)

# watched hyperneutrino's video for tips
def verify_z(wire, num):
    print("vz", wire, num)
    op, left, right = ops[wire]

    if op != "XOR":
        return False
    if num == 0:
        return (sorted([left, right]) == ["x00", "y00"])

    return verify_intermediate_xor(left, num) and verify_carry_bit(right, num) or verify_intermediate_xor(right, num) and verify_carry_bit(left, num)

def verify_intermediate_xor(wire, num):
    print("vx", wire, num)
    op, left, right = ops[wire]
    if op != "XOR": return False 
    return sorted([left, right]) == [make_wire("x", num), make_wire("y", num)]

def verify_carry_bit(wire, num):
    print("vc", wire, num)
    op, left, right = ops[wire]
    if num == 1:
        if op != "AND":
            return False
        return sorted([left, right]) == ["x00", "y00"]
    if op != "OR":
        return False 
    return verify_direct_carry(left, num - 1) and verify_recarry(right, num - 1) or verify_direct_carry(right, num - 1) and verify_recarry(left, num - 1)

def verify_direct_carry(wire, num):
    print("vd", wire, num)
    op, left, right = ops[wire]
    if op != "AND":
        return False
    return sorted([left, right]) == [make_wire("x", num), make_wire("y", num)]

def verify_recarry(wire, num):
    print("vr", wire, num)
    op, left, right = ops[wire]
    if op != "AND":
        return False
    return verify_intermediate_xor(left, num) and verify_carry_bit(right, num) or verify_intermediate_xor(right, num) and verify_carry_bit(left, num)

def verify(num):
    return verify_z(make_wire("z", num), num)

def make_wire(char, num):
    return char + str(num).rjust(2, "0")




#p1()
p2()
