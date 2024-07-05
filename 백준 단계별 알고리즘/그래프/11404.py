import sys
from collections import defaultdict

# 표준 입력에서 데이터를 읽어옴
input = sys.stdin.read

data = input().strip()
lines = data.split('\n')

# 첫 줄에서 V(정점의 수)와 E(간선의 수)를 읽어옴
V = int(lines[0])

# 시작 정점을 읽어옴
E = int(lines[1])

index = 2

INF = int(1e9)

adj_matrix = [[INF] * V for _ in range(V)]
for i in range(V):
    adj_matrix[i][i] = 0 

for _ in range(E):
    u, v, w = map(int, lines[index].split())
    if adj_matrix[u-1][v-1] > w:
        adj_matrix[u-1][v-1] = w
    index += 1

for k in range(V):
    for i in range(V):
        for j in range(V):                
            adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])

for i in range(V):
    for j in range(V):
        if adj_matrix[i][j] == INF:
            adj_matrix[i][j] = 0

for row in adj_matrix:
    for weight in row:
        print(weight, end=' ')
    print()