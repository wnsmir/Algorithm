#N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.
import numpy as np
N, M = map(int,input().split())

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for _ in range(N):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

C = A + B
for row in C:
    print(" ".join(map(str, row)))