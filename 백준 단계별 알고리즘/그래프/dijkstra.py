import heapq

def dijkstra(graph, start):
    # 시작 노드에서 다른 노드로의 최단 경로 값을 저장할 딕셔너리 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (거리, 노드)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 이미 처리된 노드이면 무시
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 현재 노드를 거쳐서 인접한 노드로 가는 거리가 기존 거리보다 짧다면 갱신
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# 그래프는 딕셔너리 형태로 정의합니다. {노드: {인접노드: 가중치, ...}, ...}
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 'A' 노드에서 출발하는 최단 경로를 계산
print(dijkstra(graph, 'A'))