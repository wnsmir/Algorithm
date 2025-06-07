from collections import deque

N = int(input())
population = [list(map(int, input().split())) for _ in range(N)]

def population_sums(area, population):
    sums = [0]*5
    for r in range(N):
        for c in range(N):
            color = area[r][c]
            sums[color-1] += population[r][c]
    return sums

def make_area(N, x, y, d1, d2):
    area = [[0] * N for _ in range(N)]

    #먼저 좌하향 경계값 지정
    for i in range(d1+1):
        area[x+i][y-i] = 5
        area[x+d2+i][y+d2-i] = 5
    #우하향 경계값 지정
    for i in range(d2+1):
        area[x+i][y+i] = 5
        area[x+d1+i][y-d1+i] = 5
    
    #구역 1부터 x, y를 넘지않으며 경계값을만나면 break하도록 설정
    for i in range(x+d1):
        for j in range(y+1):
            if area[i][j] == 5:
                break
            area[i][j] = 1

    #구역 2
    for i in range(x+1+d2):
        for j in range(N-1, y, -1):
            if area[i][j] == 5:
                break
            area[i][j] = 2    
    #구역 3
    for i in range(x+d1, N):
        for j in range(y-d1+d2):
            if area[i][j] == 5:
                break
            area[i][j] = 3    

    #구역 4
    for i in range(x+d2+1, N):
        for j in range(N-1, y-d1+d2-1, -1):
            if area[i][j] == 5:
                break
            area[i][j] = 4

    #구역 5
    for i in range(N):
        for j in range(N):
            if area[i][j] == 0:
                area[i][j] = 5

    return area

min_answer = 10**9
for x in range(N):          # 전체 돌려도 조건으로 거르니 안전
    for y in range(N):
        for d1 in range(N):
            for d2 in range(N):
                if d1 >= 1 and d2 >= 1 and 0 <= x < x+d1+d2 <= N-1 and 0 <= y-d1 < y < y+d2 <= N-1:
                    area = make_area(N, x, y, d1, d2)
                    pops = population_sums(area, population)
                    diff = max(pops) - min(pops)
                    min_answer = min(min_answer, diff)

print(min_answer)