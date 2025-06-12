from heapq import heappush, heappop

def speedrun(r1, c1, r2, c2):
    visited = [[[False]*6 for _ in range(N)] for _ in range(N)]
    pq = []
    heappush(pq, (0, r1, c1, 1))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while pq:
        time, x, y, jump = heappop(pq)
        q_time = time

        # 목적지가 아니고 이미 방문했으면 continue
        if visited[x][y][jump]:
            continue
        
        #방문 안했으면 방문처리
        visited[x][y][jump] = True

        # 목적지면 시간을 반환
        if x == r2 and y == c2:
            return time 

        # 4방향으로
        for i in range(4):
            # 현재의 점프력으로 도달할 수 있는곳이
            nx, ny = x + dx[i] * jump, y + dy[i] * jump
            check = True
            # 격자 밖이라면 pass
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            # 도착지점이 미끄러지는 곳이거나 벽이라면 pass
            if mMap[nx][ny] == 'S' or mMap[nx][ny] == '#':
                continue
            # 목적지까지 가는도중 벽이 있다면 pass
            for dist in range(1, jump +1):
                ax, ay = x + dx[i] * dist, y + dy[i] * dist
                # 가는길 중간에 벽이면 그 방향은 더이상 진행안함
                if mMap[ax][ay] == '#':
                    check = False
                    break
                # 몬스터가 있으면 해당 점프력으로는 불가능

            if check == True:
                heappush(pq, (time + 1, nx, ny, jump))  
            #점프력 증가
        if jump < 5:
            for i in range(1, 5-jump+1):
                time = time + (jump + i) ** 2
                heappush(pq, (time, x, y, jump + i))
            time = q_time

        # 점프력 감소
        for new_jump in range(1, jump):
            heappush(pq, (time + 1, x, y, new_jump))   
               
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