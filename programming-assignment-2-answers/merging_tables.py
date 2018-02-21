# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
parent = list(range(0, n))
ans = max(lines)

def find(i):
    while i != parent[i]:
        i = find(parent[i])
    return i

def merge(i, j):
    i_id = find(i)
    j_id = find(j)
    if i_id == j_id:
        return lines[i_id]
    if lines[i_id] > lines[j_id]:
        parent[j_id] = i_id
        lines[i_id] += lines[j_id]
        return lines[i_id]
    else:
        parent[i_id] = parent[j_id]
        lines[j_id] += lines[i_id]
        return lines[j_id]

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    k = merge(destination - 1, source - 1)
    if k > ans: ans = k
    print(ans)
