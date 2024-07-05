from collections import defaultdict, deque

N = int(input())
R = int(input())
adj = defaultdict(list)

for _ in range(R):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
visited = set()
stack = deque([1])
len = 0
while stack:
    node = stack.popleft()
    if node not in visited:
        visited.add(node)
        len += 1
        for neighbor in adj[node]:
            stack.append(neighbor)
print(len - 1)