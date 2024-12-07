with open("7.in") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]
calibrations = []
for line in lines:
    l = line.split(":")
    test_val = int(l[0])
    numbers = [int(n) for n in l[1].split()]
    calibrations.append((test_val, numbers))

def p1():
    tot = 0
    for c in calibrations:
        test, _ = c
        if can_be_calibrated(c, operators):
            tot += test
    print(tot)

def p2():
    tot = 0
    for c in calibrations:
        test, _ = c
        if can_be_calibrated(c, operators_p2):
            tot += test
    print(tot)

operators = ['*', '+']
operators_p2 = ['*', '+', '|']

def can_be_calibrated(c, operators):
    test, nums = c
    results = [nums[0]]
    for n in nums[1:]:
        new_results = []
        for operator in operators:
            for result in results:
                r = operate(operator, result, n)
                new_results.append(r)
        results = new_results

    return test in results

def operate(operator, l, r):
    if operator == '*':
        return l * r
    if operator == '+':
        return l + r
    if operator == '|':
        return int(str(l) + str(r))

p1()
p2()
