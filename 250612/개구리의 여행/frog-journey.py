from heapq import heappush, heappop

from heapq import heappush, heappop
INF = 10**18

def speedrun(r1, c1, r2, c2):
    dist = [[[INF]*6 for _ in range(N)] for _ in range(N)]
    dist[r1][c1][1] = 0
    pq = [(0, r1, c1, 1)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while pq:
        t, x, y, jump = heappop(pq)
        if t != dist[x][y][jump]:        # 이미 더 짧은 경로 처리됨
            continue
        if (x, y) == (r2, c2):
            return t                     # 최단시간 확정

        # 4방향 이동
        for d in range(4):
            nx, ny = x + dx[d]*jump, y + dy[d]*jump
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if mMap[nx][ny] in ('S', '#'):
                continue
            # 중간에 벽 있는지 체크
            ok = True
            for k in range(1, jump):
                ax, ay = x + dx[d]*k, y + dy[d]*k
                if mMap[ax][ay] == '#':
                    ok = False
                    break
            if not ok:
                continue
            if t+1 < dist[nx][ny][jump]:
                dist[nx][ny][jump] = t+1
                heappush(pq, (t+1, nx, ny, jump))

        # jump 증가 (최대 5)
        for add in range(1, 6-jump):
            new_jump = jump + add
            new_t = t + (jump + add)**2
            if new_t < dist[x][y][new_jump]:
                dist[x][y][new_jump] = new_t
                heappush(pq, (new_t, x, y, new_jump))

        # jump 감소
        for new_jump in range(1, jump):
            if t+1 < dist[x][y][new_jump]:
                dist[x][y][new_jump] = t+1
                heappush(pq, (t+1, x, y, new_jump))

    return -1

N = int(input())
mMap = [list(input()) for _ in range(N)]
Q = int(input())
trips = []
for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    trips.append((r1-1, c1-1, r2-1, c2-1))

for r1, c1, r2, c2 in trips:
    answer = speedrun(r1, c1, r2, c2)
    print(answer)