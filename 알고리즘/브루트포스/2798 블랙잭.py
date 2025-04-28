N, M = map(int, input().split())
num = list(map(int,input().split()))
best = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            current = num[i] + num[j] + num[k]
            if current <= M and current > best:
                best = current
print(best)