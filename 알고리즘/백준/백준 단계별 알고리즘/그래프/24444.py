import sys
from collections import defaultdict, deque

def read_input():
    input = sys.stdin.read
    data = input().strip().split()

    index = 0
    N = int(data[index])
    M = int(data[index + 1])
    R = int(data[index + 2])

    index = index + 3
    adj = defaultdict(list)
    for _ in range(M):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].append(v)
        adj[v].append(u)
        index = index + 2
    return adj, N, R

def bfs(adj, N, R):
    visited = set()
    queue = deque([R])
    order = [0] * (N+1)
    count = 1
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order[node] = count
            count += 1
            for neighbor in sorted(adj[node], reverse=True):
                if neighbor not in visited:
                    queue.append(neighbor)
    return order
adj, N, R = read_input()
order = bfs(adj, N, R)

for i in range(1, N + 1):
    print(order[i])