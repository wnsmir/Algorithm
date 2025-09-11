# BOJ 15683 감시 (sys 없이 input만 사용)

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 방향: 상(0), 우(1), 하(2), 좌(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# CCTV 타입별 가능한 방향 세트
orient = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5: [[0, 1, 2, 3]],
}

cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] <= 5:
            cctvs.append((i, j, board[i][j]))

def watch_once(x, y, d):
    changed = []
    nx, ny = x + dx[d], y + dy[d]
    while 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:
        if board[nx][ny] == 0:
            board[nx][ny] = 7
            changed.append((nx, ny))
        nx += dx[d]
        ny += dy[d]
    return changed

def apply_dirs(x, y, dset):
    changed_total = []
    for d in dset:
        changed_total.extend(watch_once(x, y, d))
    return changed_total

def undo(changed_list):
    for (x, y) in changed_list:
        board[x][y] = 0

ans = float('inf')

def dfs(idx):
    global ans
    if idx == len(cctvs):
        blind = sum(row.count(0) for row in board)
        ans = min(ans, blind)
        return
    x, y, t = cctvs[idx]
    for dset in orient[t]:
        changed = apply_dirs(x, y, dset)
        dfs(idx + 1)
        undo(changed)

dfs(0)
print(ans)