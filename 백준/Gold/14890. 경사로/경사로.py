def check_row(line, L):
    N = len(line)
    used = [False] * N
    for j in range(N - 1):
        # 같은 높이일 경우 패스
        if line[j] == line[j + 1]:
            continue

        # 앞칸이 뒷칸보다 1 높을 때 (내리막)
        if line[j + 1] + 1 == line[j]:
            count = 0
            for k in range(L):
                idx = j + 1 + k
                if idx >= N or line[idx] != line[j + 1] or used[idx]:
                    return False
                count += 1
            for k in range(L):
                used[j + 1 + k] = True

        # 앞칸이 뒷칸보다 1 낮을 때 (오르막)
        elif line[j + 1] - 1 == line[j]:
            count = 0
            for k in range(j, j - L, -1):
                if k < 0 or line[k] != line[j] or used[k]:
                    return False
                count += 1
            for k in range(j, j - L, -1):
                used[k] = True

        # 높이차가 2 이상이면 실패
        else:
            return False
    return True


# 입력 받기
N, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0

# 행 검사
for i in range(N):
    if check_row(grid[i], L):
        answer += 1

# 열 검사
for j in range(N):
    col = [grid[i][j] for i in range(N)]
    if check_row(col, L):
        answer += 1

print(answer)