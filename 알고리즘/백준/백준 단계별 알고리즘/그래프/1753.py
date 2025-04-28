import sys
import heapq
from collections import defaultdict

# 표준 입력에서 데이터를 읽어옴
input = sys.stdin.read

data = input().strip()
lines = data.split('\n')

# 첫 줄에서 V(정점의 수)와 E(간선의 수)를 읽어옴
V, E = map(int, lines[0].split())

# 시작 정점을 읽어옴
start = int(lines[1])

# 그래프 초기화
graph = defaultdict(dict)
index = 2

# 그래프 구성
for _ in range(E):
    u, v, w = map(int, lines[index].split())
    # 기존의 간선보다 작은 가중치의 간선을 선택
    if v not in graph[u] or w < graph[u][v]:
        graph[u][v] = w
    index += 1

def dijkstra(graph, start):
    # distances를 defaultdict로 초기화
    distances = defaultdict(lambda: float('inf'))
    distances[start] = 0
    priority_queue = [(0, start)]  # (거리, 노드)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

result = dijkstra(graph, start)

for node in range(1, V + 1):
    distance = result[node]
    if distance != float('INF'):
        print(distance)
    else:
        print('INF')