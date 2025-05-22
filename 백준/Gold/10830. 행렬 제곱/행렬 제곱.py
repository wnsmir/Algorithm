def mat_mul(A, B, mod):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= mod
    return result

def mat_pow(mat, power, mod):
    n = len(mat)
    # 단위행렬로 초기화
    result = [[int(i == j) for j in range(n)] for i in range(n)]
    while power > 0:
        if power % 2 == 1:
            result = mat_mul(result, mat, mod)
        mat = mat_mul(mat, mat, mod)
        power //= 2
    return result

n, k = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
mod = 1000
ans = mat_pow(mat, k, mod)
for row in ans:
    print(*row)