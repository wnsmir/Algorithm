# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
테스트 시에만 사용하고, 제출 시에는 반드시 주석 처리해야 합니다.
'''
# import sys
# sys.stdin = open("input.txt", "r")


def count_horizontal(grid, N, K, visited_h):
    answer = 0

    for i in range(N):
        for j in range(N):
            # 흰 칸이고, 아직 가로로 방문 안 한 칸만 시작 후보
            if grid[i][j] != 1 or visited_h[i][j]:
                continue

            # 왼쪽이 1이면 이미 앞에서 시작한 구간의 중간이므로 패스
            if j > 0 and grid[i][j - 1] == 1:
                continue

            # 오른쪽으로 K칸 연속 1인지 확인
            nj = j
            cnt = 0
            ok = True
            while cnt < K:
                # 범위 벗어나면 실패
                if nj >= N:
                    ok = False
                    break
                # 중간에 벽(0)이 나오면 실패
                if grid[i][nj] == 0:
                    ok = False
                    break
                cnt += 1
                nj += 1

            # K칸 못 채웠으면 패스
            if not ok or cnt != K:
                continue

            # K칸 뒤가 경계이거나 0이면 "딱 K칸"짜리
            if nj == N or grid[i][nj] == 0:
                answer += 1
                # 그 K칸들 가로 방문 처리
                for b in range(K):
                    visited_h[i][j + b] = True

    return answer


def count_vertical(grid, N, K, visited_v):
    answer = 0

    for i in range(N):
        for j in range(N):
            # 흰 칸이고, 아직 세로로 방문 안 한 칸만 시작 후보
            if grid[i][j] != 1 or visited_v[i][j]:
                continue

            # 위가 1이면 이미 위에서 시작한 구간의 중간이므로 패스
            if i > 0 and grid[i - 1][j] == 1:
                continue

            # 아래로 K칸 연속 1인지 확인
            ni = i
            cnt = 0
            ok = True
            while cnt < K:
                # 범위 벗어나면 실패
                if ni >= N:
                    ok = False
                    break
                # 중간에 벽(0)이 나오면 실패
                if grid[ni][j] == 0:
                    ok = False
                    break
                cnt += 1
                ni += 1

            # K칸 못 채웠으면 패스
            if not ok or cnt != K:
                continue

            # K칸 뒤가 경계이거나 0이면 "딱 K칸"짜리
            if ni == N or grid[ni][j] == 0:
                answer += 1
                # 그 K칸들 세로 방문 처리
                for b in range(K):
                    visited_v[i + b][j] = True

    return answer


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    visited_h = [[False] * N for _ in range(N)]
    visited_v = [[False] * N for _ in range(N)]

    ans = 0
    ans += count_horizontal(grid, N, K, visited_h)
    ans += count_vertical(grid, N, K, visited_v)

    print(f"#{test_case} {ans}")
    # ///////////////////////////////////////////////////////////////////////////////////