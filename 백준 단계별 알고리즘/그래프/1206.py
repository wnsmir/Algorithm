from collections import defaultdict, deque

N, M, R = map(int, input().split())
adj = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
def find_key_by_value(prev, R):
    return [k for k, v in prev.items() if v == R]

def bfs(adj, R):
    bfs_prev = {R: None}
    visited = set()
    queue = deque([R])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in sorted(adj[node]):
                if neighbor not in visited:
                    queue.append(neighbor)
                    bfs_prev[neighbor] = node
    return bfs_prev
# 주어진 그래프 (딕셔너리 형태)
graph = {1: None, 2: 1, 3: 1, 4: 3}

def find_full_path(graph):
    # 루트 노드를 찾기
    root = None
    for node, parent in graph.items():
        if parent is None:
            root = node
            break

    # 모든 노드를 방문하여 경로를 역추적
    def get_path(node):
        path = []
        current = node
        while current is not None:
            path.append(current)
            current = graph[current]
        path.reverse()  # 경로를 올바른 순서로 변경
        return path

    # 전체 경로를 만들기 위한 리스트
    full_path = []

    # 각 노드를 방문하여 경로를 추가
    for node in graph.keys():
        if node != root:
            path = get_path(node)
            for n in path:
                if n not in full_path:
                    full_path.append(n)
    
    return full_path

def dfs(adj, R):
    visited = set()
    stack = [R]
    dfs_prev = {R: None}

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in sorted(adj[node], reverse=True):
                if neighbor not in visited:
                    stack.append(neighbor)
                    dfs_prev[neighbor] = node
    endnode = dfs_prev
    nodes = set(endnode.keys())
    values = set(endnode.values())
    last_visited_node = nodes - values
    last_visited_node = next(iter(last_visited_node))
    return dfs_prev, last_visited_node

def print_path(prev, end):
    path = []
    while end is not None:
        path.append(end)
        end = prev[end]
    path.reverse()
    for node in path:
        print(node, end=' ')
    print('\n',end='')
dfs_prev, last_visited_node = dfs(adj, R)
print_path(dfs_prev, last_visited_node)
bfs_prev = bfs(adj, R)
path = find_full_path(bfs_prev)
for node in path:
    print(node, end=' ')