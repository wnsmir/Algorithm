import math

A, B, C = map(float, input().split())

def f(x):
    return A * x + B * math.sin(x)

left = 0
right = (C + B) / A + 10  # 충분히 큰 값, +10 여유
for _ in range(100):      # 100번만 반복해도 충분
    mid = (left + right) / 2
    if f(mid) < C:
        left = mid
    else:
        right = mid

print((left + right) / 2)