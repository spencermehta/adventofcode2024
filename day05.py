from collections import defaultdict

with open("5.in") as f:
    lines = f.readlines()
lines = [line.strip() for line in lines]

def part_one():
    rules = defaultdict(list)
    updates = []
    before_break = True
    for line in lines:
        if line == '':
            before_break = False
            continue
    
        if before_break:
            rule = line.split('|')
            rules[int(rule[1])].append(int(rule[0]))
        else:
            updates.append([int(c) for c in line.split(',')])
    
    s = 0
    for update in updates:
        if is_ordered(update, rules):
            mid = len(update) // 2
            s += update[mid]
    print(s)


def is_ordered(update, rules):
    for (i, num) in enumerate(update):
        remaining = set(update[i+1:])
        must_be_after = rules[num]
        overlap = remaining.intersection(must_be_after)
        if len(overlap) != 0:
            return False
    return True

def part_two():
    rules = defaultdict(list)
    updates = []
    before_break = True
    for line in lines:
        if line == '':
            before_break = False
            continue
    
        if before_break:
            rule = line.split('|')
            rules[int(rule[1])].append(int(rule[0]))
        else:
            updates.append([int(c) for c in line.split(',')])
    
    s = 0
    for update in updates:
        if not is_ordered(update, rules):
            nu = reorder(update, rules)
            print("u ", update, "nu ", nu)
            mid = len(nu) // 2
            s += nu[mid]
    print(s)

def reorder(update, rules):
    reduced_rules = defaultdict(set)
    update_set = set(update)
    new_update = []

    for num in update:
        intersection = update_set.intersection(rules[num])
        reduced_rules[num] = intersection

    update_len = len(update)
    while len(new_update) < update_len:
        for num in update:
            if len(reduced_rules[num]) == 0:
                new_update.append(num)
                update.remove(num)
                for n2 in update:
                    if num in reduced_rules[n2]:
                        reduced_rules[n2].remove(num)

    return new_update

part_one()
part_two()



