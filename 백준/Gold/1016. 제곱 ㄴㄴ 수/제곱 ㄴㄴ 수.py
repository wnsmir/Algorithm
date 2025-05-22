import sys
import math

min_num, max_num = map(int, input().split())
size = max_num - min_num + 1

# 각 숫자가 제곱 ㄴㄴ 수인지 여부를 True로 표시
is_squarefree = [True] * size

for i in range(2, int(math.isqrt(max_num)) + 1):
    square = i * i
    # 시작점: min_num 이상이면서 square로 나누어떨어지는 첫 수
    start = ((min_num + square - 1) // square) * square
    for j in range(start, max_num + 1, square):
        is_squarefree[j - min_num] = False

print(sum(is_squarefree))