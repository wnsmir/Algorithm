n, m = map(int, input().split())
b = []
for i in range(1,n+1):
    b.append(i)

for index in range(m):
    i, j = map(int, input().split())
    b[i-1], b[j-1] = b[j-1], b[i-1]

for i in b:
    print(i, end=" ")
