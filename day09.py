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

    #print("".join([str(c) for c in memory]))

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
    files = []
    for i, c in enumerate(chars):
        if i % 2 == 0:
            files.append((file_number, c, len(memory)))
            for _ in range(c):
                memory.append(file_number)
            file_number+=1
        else:
            for _ in range(c):
                memory.append('.')

    #print("".join([str(c) for c in memory]))
    for j in range(len(files)-1, -1, -1):
        (file_num, file_length, file_start) = files[j]
        #print("\n\n", file_num, file_length, "\n\n")

        lowest_free, lowest_free_length = get_lowest_free(memory)

        #print(lowest_free, lowest_free_length)
        #print("".join([str(c) for c in memory]))
        while lowest_free_length < file_length and lowest_free_length != 0:
            #print("looping")
            olf = lowest_free
            olfl = lowest_free_length
            lowest_free, lowest_free_length = get_lowest_free(memory[lowest_free + lowest_free_length+1:])
            lowest_free += olf + olfl + 1
            #print(lowest_free, lowest_free_length)
            #print("".join([str(c) for c in memory]))

        if lowest_free_length >= file_length and lowest_free < file_start:
            #print("writing")
            for i in range(file_length):
                memory[lowest_free + i] = memory[file_start + i]
                memory[file_start + i] = '.'


    #print("".join([str(c) for c in memory]))
    print(checksum(memory))

def get_lowest_free(memory):
    if '.' not in memory:
        return 0, 0
    lowest_free = memory.index('.')
    lowest_free_length = 1
    while memory[lowest_free + lowest_free_length] == '.':
        lowest_free_length+=1
        if len(memory) <= lowest_free + lowest_free_length:
            break
    return lowest_free, lowest_free_length


def checksum(arr):
    tot = 0
    for i, c in enumerate(arr):
        if c != '.':
            tot += (i * c)
    return tot


p1()
p2()
