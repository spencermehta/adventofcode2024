with open("9.in") as f:
    line = f.readline().strip()

def p1():
    chars = [int(c) for c in line]
    file_number = 0
    memory = []
    for i, c in enumerate(chars):
        if i % 2 == 0:
            for _ in range(c):
                memory.append(file_number)
            file_number+=1
        else:
            for _ in range(c):
                memory.append('.')

    for i in range(len(memory)-1, -1, -1):
        lowest_free = memory.index('.')
        if lowest_free >= i:
            break

        memory[lowest_free] = memory[i]
        memory[i] = '.'

    #print("".join([str(c) for c in memory]))
    print(checksum(memory))


def p2():
    chars = [int(c) for c in line]
    file_number = 0
    memory = []
    memory_len = 0

    files = []
    empties = []

    for i, c in enumerate(chars):
        if i % 2 == 0:
            files.append((file_number, c, memory_len))
            for _ in range(c):
                memory.append(file_number)
            memory_len += c
            file_number+=1
        else:
            empties.append((c, memory_len))
            for _ in range(c):
                memory.append('.')
            memory_len += c

    L = ['.' for _ in memory]
    for i in range(len(files)-1, -1, -1):
        file_num, file_len, file_start = files[i]

        empty_index = 0
        empty_len, empty_start = empties[empty_index]
        while empty_len < file_len:
            empty_index += 1
            if len(empties) == empty_index:
                empty_len, empty_start = 0, 1
                break
            empty_len, empty_start = empties[empty_index]

        if file_start < empty_start or empty_len < file_len:
            for i in range(file_start, file_start + file_len):
                L[i] = file_num
            continue

        new_file_start = empty_start

        for i in range(new_file_start, new_file_start + file_len):
            L[i] = file_num

        new_empty_len = empty_len - file_len
        if new_empty_len == 0:
            del empties[empty_index]
        else:
            empties[empty_index] = (new_empty_len, empty_start + file_len)

    # print("".join([str(c) for c in L]))
    print(checksum(L))

def checksum(arr):
    tot = 0
    for i, c in enumerate(arr):
        if c != '.':
            tot += (i * c)
    return tot


p1()
p2()
