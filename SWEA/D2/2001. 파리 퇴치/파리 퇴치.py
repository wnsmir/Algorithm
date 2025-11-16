T = int(input())
tc = 0
for _ in range(T):
    tc += 1
    N, M = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(N)]
    max_kill = 0

    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            total_kill = 0
            for k in range(M):
                for l in range(M):
                    total_kill += grid[i+k][j+l]
            if max_kill > total_kill:
                pass
            else:
                max_kill = total_kill

    print(f"#{tc} {max_kill}")