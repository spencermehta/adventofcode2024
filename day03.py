import re

with open("3.in") as f:
    line = f.readline()
print(line)

def part_one():
    res = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", line)
    instrs = []
    for r in res:
        nr = r.replace("(", " ").replace(",", " ").replace(")", "").split()
        instr = (nr[0], int(nr[1]), int(nr[2]))
        instrs.append(instr)
    
    s = 0
    for (action, left, right) in instrs:
        s += (left * right)
    print(s)
    print(len(instrs))
    

def part_two():
    res = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\)", line)
    print(res)
    instrs = []
    for r in res:
        nr = r.replace("(", " ").replace(",", " ").replace(")", "").split()
        if nr[0] == "mul":
            instr = (nr[0], int(nr[1]), int(nr[2]))
        else:
            instr = (nr[0], None, None)
        instrs.append(instr)
    
    s = 0
    enabled = True
    for (action, left, right) in instrs:
        print(action, left, right)
        if (action == "do"):
            enabled = True
        elif (action == "don't"):
            enabled = False
        elif action == "mul":
            if enabled:
                s += (left * right)

    print(s)

part_two()
    

