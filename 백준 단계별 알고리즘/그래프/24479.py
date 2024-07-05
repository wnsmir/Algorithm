from collections import defaultdict
import sys

def read_input():
    input = sys.stdin.read
    data = input().strip().split()

    index = 0
    N = int(data[index])
    M = int(data[index + 1])
    R = int(data[index + 2])

    index += 3

    adj = defaultdict(list)
    for _ in range(M):
        u = int(data[index])
        v = int(data[index + 1])
        adj[u].append(v)
        adj[v].append(u)
        index += 2

    # 인접 리스트를 미리 정렬
    for key in adj:
        adj[key].sort()

    return N, adj, R

# 깊이 우선 탐색(DFS) 함수
def DFS(N, adj, R):
    visited = set()  # 방문한 노드를 기록할 집합
    order = [0] * (N + 1)  # 방문 순서를 기록할 리스트
    stack = [R]
    count = 1

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order[node] = count
            count += 1
            # 이웃 노드를 스택에 추가
            for neighbor in adj[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return order
N, adj, R = read_input()
order = DFS(N, adj, R)
print(order)
print
