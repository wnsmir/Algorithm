T = int(input())
tc = 0
for _ in range(T):
    tc += 1
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    # 가로 체크
    for i in range(N):
        for j in range(0, N-K+1):
            # 첫번째 칸 이거나 이전 칸이 벽일 경우
            if j == 0 or grid[i][j-1] == 0:
                flag = True
                for k in range(K):
                    # 가로로 k만큼 빈공간이라면
                    if grid[i][j+k] != 1:
                        flag = False
                # 마지막칸이거나 다음칸이 벽이라면
                if flag == True and (j+K >= N or grid[i][j+K] == 0):
                    answer += 1
    
    # 세로 체크
    for i in range(N):
        for j in range(0, N-K+1):
            # 첫번째 칸 이거나 이전 칸이 벽일 경우
            if j == 0 or grid[j-1][i] == 0:
                flag = True
                for k in range(K):
                    # 가로로 k만큼 빈공간이라면
                    if grid[j+k][i] != 1:
                        flag = False
                # 마지막칸이거나 다음칸이 벽이라면
                if flag == True and (j+K >= N or grid[j+K][i] == 0):
                    answer += 1

    print(f"#{tc} {answer}")