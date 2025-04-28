import numpy as np

def floyd_warshall(graph):
    # 정점의 개수
    V = len(graph)
    
    # 결과 거리를 초기화합니다. 입력 그래프의 복사본을 사용합니다.
    dist = np.array(graph, copy=True)
    
    # Floyd-Warshall 알고리즘
    for k in range(V):
        for i in range(V):
            for j in range(V):
                # dist[i][j]를 dist[i][k] + dist[k][j]와 비교하여 최솟값을 갱신합니다.
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

# 예제 그래프
graph = [
    [0, 3, np.inf, 7],
    [8, 0, 2, np.inf],
    [5, np.inf, 0, 1],
    [2, np.inf, np.inf, 0]
]

# 결과 계산
result = floyd_warshall(graph)

print("최단 경로 행렬:")
print(result)