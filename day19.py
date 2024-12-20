import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
towels, patterns = f.split("\n\n")
towels = towels.replace(' ', '').split(',')
patterns = patterns.split("\n")
print(towels)

def p1():
    tot = 0
    for pattern in patterns:
        print(f"{pattern=}")
        if can_make_pattern(pattern):
            tot+=1
    print(tot)

C = {}
def can_make_pattern(pattern):
    i=len(pattern)

    while i>=0:
        if (pattern, i) in C:
            return C[(pattern, i)]
        pi = pattern[:i]
        #print(f"{i=} {pi=} ")
        if pi not in towels:
            i=i-1
            continue

        remaining = pattern[i:]
        if remaining == "":
            C[(pattern, i)] = True
            return True
        print(f"continuing with {remaining=}")
        cmp = can_make_pattern(remaining)
        if not cmp:
            C[(pattern, i)] = False
            i=i-1
            print(f"backtracking at {i=}")
            continue

        return True

    return False




p1()

