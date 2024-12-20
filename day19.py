import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
towels, patterns = f.split("\n\n")
towels = towels.replace(' ', '').split(',')
patterns = patterns.split("\n")

C1 = {}
C = {}
CC = {}

def p1():
    tot = 0
    for pattern in patterns:
        if can_make_pattern(pattern):
            tot+=1
    print(tot)

def p2():
    tot = 0
    for pattern in patterns:
        pats = can_make_pattern(pattern)
        tot+=pats
    print(tot)

def can_make_pattern_p1(pattern):
    i=len(pattern)

    while i>=0:
        if (pattern, i) in C1:
            return C[(pattern, i)]
        pi = pattern[:i]
        if pi not in towels:
            i=i-1
            continue

        remaining = pattern[i:]
        if remaining == "":
            C1[(pattern, i)] = True
            return True
        cmp = can_make_pattern_p1(remaining)
        if not cmp:
            C1[(pattern, i)] = False
            i=i-1
            continue

        return True

    return False

def can_make_pattern(pattern):
    i=len(pattern)

    count = 0
    while i>=0:
        if (pattern, i) in C:
            return C[(pattern,i)]

        pi = pattern[:i]
        if pi not in towels:
            i=i-1
            continue

        remaining = pattern[i:]
        if remaining == "":
            count+=1

        if (remaining) in CC:
            cmp = CC[remaining]
        else:
            cmp = can_make_pattern(remaining)
            CC[remaining] = cmp
        count+=cmp

        i=i-1

    C[(pattern,i)] = count
    return count




p1()
p2()

