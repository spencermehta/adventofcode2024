import sys
with open("11.in") as f:
    line = f.readline().strip()
sys.setrecursionlimit(10**6)

def p1():
    nums = [int(n) for n in line.split()]

    for _ in range(25):
        nums = blink(nums)
        #print(nums)
        nums = nums
    print(len(nums))

def p2():
    full_nums = [int(n) for n in line.split()]
    tot=0

    for num in full_nums:
        tot+= blink2(num, 75)

    print(tot)

def blink(nums):
    new_nums = []
    for n in nums:
        if n == 0:
            new_nums.append(1)
        elif len(str(n)) % 2 == 0:
            l = len(str(n))
            left = str(n)[:l//2]
            right = str(n)[l//2:]
            new_nums.append(int(left))
            new_nums.append(int(right))
        else:
            new_nums.append(n * 2024)
    return new_nums

CACHE = {}

def blink2(num, r):
    if (num, r) in CACHE:
        return CACHE[(num, r)]

    if r <= 0:
        val = 1
    elif num == 0:
        val = blink2(1, r-1)
    elif len(str(num)) % 2 == 0:
        l = len(str(num))
        left = str(num)[:l//2]
        right = str(num)[l//2:]

        val = blink2(int(left), r-1) + blink2(int(right), r-1)
    else:
        val = blink2(num * 2024, r-1)

    CACHE[(num, r)] = val
    return val

p1()
p2()
