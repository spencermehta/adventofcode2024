import math
import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
registers, program_in = f.split("\n\n")

def p1():
    a,b,c = registers.split("\n")
    a = int(a.split(" ")[2])
    b = int(b.split(" ")[2])
    c = int(c.split(" ")[2])

    program = [int(n) for n in program_in.split()[1].split(',')]

    output = []
    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]

        if opcode == 0:
            numerator = a
            denominator = 2 ** (combo(operand, a, b, c))
            v = math.floor(numerator / denominator)
            a = v
        elif opcode == 1:
            v = b ^ operand
            b = v
        elif opcode == 2:
            v = combo(operand, a, b, c) % 8
            b = v
        elif opcode == 3:
            if a != 0:
                i=operand
                continue
        elif opcode == 4:
            v = b ^ c
            b = v
        elif opcode == 5:
            v = combo(operand, a, b, c) % 8
            output.append(v)
        elif opcode == 6:
            numerator = a
            denominator = 2 ** (combo(operand, a, b, c))
            v = math.floor(numerator / denominator)
            b = v
        elif opcode == 7:
            numerator = a
            denominator = 2 ** (combo(operand, a, b, c))
            v = math.floor(numerator / denominator)
            c = v

        i+=2

    s = ""
    for o in output:
        s += str(o) + ","
    print(s)

def p2():
    a,b,c = registers.split("\n")
    a = int(a.split(" ")[2])
    b = int(b.split(" ")[2])
    c = int(c.split(" ")[2])

    program = [int(n) for n in program_in.split()[1].split(',')]

    i = 2
   #i=252776563040076
    i=35184386948113
    prev = 0
    while True:
        a = i
        output = run(a,b,c, program)

        if output[:7] == [2,4,1,3,7,5,0]:
            print(i, output, len(output) - len(program), i-prev)
            prev = i
        if output == program:
            print(i)
            break
        if len(output) < len(program):
            i*=2
        else:
            #i+=1
            #i+=261787
            i+=260736



def run(a, b, c, program):
    output = []
    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]

        if opcode == 0:
            numerator = a
            denominator = 2 ** (combo(operand, a, b, c))
            v = math.floor(numerator / denominator)
            a = v
        elif opcode == 1:
            v = b ^ operand
            b = v
        elif opcode == 2:
            v = combo(operand, a, b, c) % 8
            b = v
        elif opcode == 3:
            if a != 0:
                i=operand
                continue
        elif opcode == 4:
            v = b ^ c
            b = v
        elif opcode == 5:
            v = combo(operand, a, b, c) % 8
            output.append(v)
        elif opcode == 6:
            numerator = a
            denominator = 2 ** (combo(operand, a, b, c))
            v = math.floor(numerator / denominator)
            b = v
        elif opcode == 7:
            numerator = a
            denominator = 2 ** (combo(operand, a, b, c))
            v = math.floor(numerator / denominator)
            c = v

        i+=2
    return output

def combo(operand, a, b, c):
    if operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    elif operand == 7:
        print("ERROR")
    return 0


p1()
p2()
