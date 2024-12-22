from collections import deque
import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")
lines = [int(n) for n in lines]

def p1():
    tot = 0
    for num in lines:
        n = num
        for _ in range(2000):
            n = simulate_day(n)
        tot += n
    print(tot)

def p2():
    all_seqs = []
    all_prices = []
    for num in lines:
        sequences, prices = simulate_buyer(num)
        all_seqs.append(sequences)
        all_prices.append(prices)

    best = 0
    for i in range(len(lines[:1])):
        sequences = all_seqs[i]
        for low in range(2000-4):
            high = low+4
            buy_seq = sequences[low:high]

            tot = 0
            for num in lines:
                price = simulate_buyer_buying(num, buy_seq)
                if price is not None:
                    tot+=price
            if tot > best:
                best = tot
    print(best)


def simulate_buyer_buying(num, seq):
    sequences = []
    prices = []
    n = num
    price = int(str(n)[len(str(n))-1:len(str(n))])
    for _ in range(2000):
        prev = price
        n = simulate_day(n)
        price = int(str(n)[len(str(n))-1:len(str(n))])
        sequences.append(price-prev)
        prices.append(price)

        if sequences[len(sequences)-4:len(sequences)] == seq:
            return price
    return None



def simulate_buyer(num):
    sequences = []
    prices = []
    n = num
    price = int(str(n)[len(str(n))-1:len(str(n))])
    print(price)
    for _ in range(2000):
        prev = price
        n = simulate_day(n)
        price = int(str(n)[len(str(n))-1:len(str(n))])
        sequences.append(price-prev)
        prices.append(price)
    return sequences, prices



def simulate_day(num):
    big = num * 64
    num = num ^ big
    num = num % 16777216 

    divided = num // 32
    num = num ^ divided
    num = num % 16777216

    mult = num * 2048
    num = num ^ mult
    num = num % 16777216

    return num

#p1()
p2()

