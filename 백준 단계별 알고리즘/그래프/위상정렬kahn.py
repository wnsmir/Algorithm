def kahn_topological_sort(edges):
    # 모든 노드를 수집
    nodes = set()
    for src, dest in edges:
        nodes.add(src)
        nodes.add(dest)
    
    # 각 노드의 들어오는 간선의 수를 저장할 딕셔너리 초기화
    in_degree = {node: 0 for node in nodes}
    # 인접 리스트를 저장할 딕셔너리 초기화
    adj_list = {node: [] for node in nodes}

    # 간선 리스트를 순회하며 in_degree와 adj_list를 업데이트
    for src, dest in edges:
        adj_list[src].append(dest)
        in_degree[dest] += 1

    # 들어오는 간선의 수가 0인 노드들을 리스트로 저장
    zero_in_degree_list = []
    for node in in_degree:
        if in_degree[node] == 0:
            zero_in_degree_list.append(node)

    topological_order = []

    # 위상 정렬 수행
    while zero_in_degree_list:
        vertex = zero_in_degree_list.pop()
        topological_order.append(vertex)

        if vertex in adj_list:
            for neighbor in adj_list[vertex]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree_list.append(neighbor)

    # 모든 노드를 방문했는지 확인
    if len(topological_order) == len(nodes):
        return topological_order
    else:
        return []  # 사이클이 존재하는 경우 빈 리스트 반환

# 예제 사용법
edges = [('A', 'C'), ('B', 'C'), ('C', 'E'), ('D', 'E'), ('E', 'F')]
print(kahn_topological_sort(edges))