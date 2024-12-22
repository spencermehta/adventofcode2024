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
    sequences_to_prices = []
    for num in lines:
        sequences, prices = simulate_buyer(num)
        all_seqs.append(sequences)
        all_prices.append(prices)
        seq_to_price = get_sequence_to_price(sequences, prices)
        sequences_to_prices.append(seq_to_price)

    best = 0
    buy_sequences = set()
    for i in range(len(lines)):
        print(f"{i=}")
        sequences = all_seqs[i]
        for low in range(2000-4):
            high = low+4
            buy_seq = tuple(sequences[low:high])
            buy_sequences.add(buy_seq)
    print(len(buy_sequences))

    for i, buy_seq in enumerate(buy_sequences):
        if i % 1000 == 0:
            print(f"{i=}")
        tots = []
        for j in range(len(lines)):
            if buy_seq in sequences_to_prices[j]:
                price = sequences_to_prices[j][buy_seq]
                tots.append(price)
                if buy_seq == tuple([-2,1,-1,3]):
                    print(f"{j=} {tots=}")


        if sum(tots) > best:
            best = sum(tots)
            print(f"best {best=} found at {i=} from {tots=} and {buy_seq=}")
    print(f"{best=}")

def get_sequence_to_price(sequences, prices):
    sequence_map = {}
    for low in range(len(sequences)-4):
        high = low + 4
        buy_seq = tuple(sequences[low:high])
        if buy_seq not in sequence_map:
            sequence_map[buy_seq] = prices[high-1]
        
    return sequence_map


def simulate_buyer(num):
    sequences = []
    prices = []
    n = num
    price = int(str(n)[len(str(n))-1:len(str(n))])
    for _ in range(2001):
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

