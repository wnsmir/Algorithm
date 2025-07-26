import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
start, end = map(int, input().split())

def bfs(weight):
    visited = [False] * (N+1)
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        if now == end:
            return True
        for nxt, limit in edges[now]:
            if not visited[nxt] and limit >= weight:
                visited[nxt] = True
                q.append(nxt)
    return False

left = 1
right = 1_000_000_000
answer = 0

while left <= right:
    mid = (left + right) // 2
    if bfs(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)