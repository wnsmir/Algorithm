from itertools import combinations
from collections import deque

board = [list(input().strip()) for _ in range(5)]
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def is_connected(cands):
    q = deque([cands[0]])
    visited = set([cands[0]])
    cands_set = set(cands)
    while q:
        cur = q.popleft()
        x, y = cur // 5, cur % 5
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0<=nx<5 and 0<=ny<5:
                nxt = nx*5+ny
                if nxt in cands_set and nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
    return len(visited) == 7

for cands in combinations(range(25), 7):
    S_cnt = sum(1 for idx in cands if board[idx//5][idx%5]=='S')
    if S_cnt >= 4 and is_connected(cands):
        ans += 1

print(ans)