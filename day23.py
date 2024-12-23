from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**6)

file_name = sys.argv[1]
with open(file_name) as f:
    f = f.read().strip()
lines = f.split("\n")

edges = defaultdict(set)
vertices = set()

for line in lines:
    l, r = line.split("-")
    edges[l].add(r)
    edges[r].add(l)
    vertices.add(l)
    vertices.add(r)

def p1():
    connected_components = set()
    for v in vertices:
        components = dfs(v)
        for c in components:
            if len(c) == 3:
                starts_with_t = False
                for vertex in c:
                    if vertex[0] == 't':
                        starts_with_t = True

                if starts_with_t:
                    connected_components.add(c)

    print(len(connected_components))

def p2():
    for v in vertices:
        dfs2(v, {v})

    connected_components = conn_comps

    best = 0
    bestt = set()
    for c in connected_components:
        if len(c) > best:
            best = len(c)
            bestt = c

    b = sorted(bestt)
    print(",".join(b))


def dfs(start):
    q = deque()
    q.append(start)
    SEEN = set()

    for v in edges[start]:
        for v2 in edges[v]:
            if start in edges[v2]:
                SEEN.add(frozenset({start, v, v2}))

    return SEEN

conn_comps = set()
def dfs2(v, party):
    if party in conn_comps:
        return

    conn_comps.add(frozenset(party))
    for v2 in edges[v]:
        if v2 in party:
            continue
        in_all = True
        for s in party:
            if v2 not in edges[s]:
                in_all=False

        if in_all:
            dfs2(v2, {*party, v2})

p1()
p2()


