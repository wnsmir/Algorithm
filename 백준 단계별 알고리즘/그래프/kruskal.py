class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}  # 각 정점은 자기 자신을 부모로 가짐
        self.rank = {v: 0 for v in vertices}    # 각 정점의 랭크(트리의 높이)를 0으로 초기화

    def find(self, v):
        if self.parent[v] != v:  # 루트가 아니라면
            self.parent[v] = self.find(self.parent[v])  # 경로 압축: 루트를 찾을 때 부모를 루트로 설정
        return self.parent[v]  # 루트를 반환

    def union(self, u, v):
        root_u = self.find(u)  # u의 루트를 찾음
        root_v = self.find(v)  # v의 루트를 찾음

        if root_u != root_v:  # 루트가 다르면
            if self.rank[root_u] > self.rank[root_v]:  # u의 랭크가 더 높으면
                self.parent[root_v] = root_u  # v를 u에 붙임
            elif self.rank[root_u] < self.rank[root_v]:  # v의 랭크가 더 높으면
                self.parent[root_u] = root_v  # u를 v에 붙임
            else:
                self.parent[root_v] = root_u  # 랭크가 같으면
                self.rank[root_u] += 1  # u의 랭크를 1 증가

def get_weight(edge):
        return edge[2]
    
def kruskal(vertices, edges):
    mst = []
    disjoint_set = DisjointSet(vertices)

    edges = sorted(edges, key=get_weight)

    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u,v)
            mst.append(edge)
    return mst


# 예제 사용법
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    ('A', 'B', 4),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 6),
    ('C', 'D', 8),
    ('C', 'E', 10),
    ('D', 'E', 9),
    ('D', 'F', 7),
    ('E', 'F', 5)
]

disjoint_set = DisjointSet(vertices)
print(disjoint_set.find('A'))  # A의 루트 출력
disjoint_set.union('A', 'B')  # A와 B를 하나의 집합으로 합침
print(disjoint_set.find('B'))  # B의 루트 출력 (A여야 함)