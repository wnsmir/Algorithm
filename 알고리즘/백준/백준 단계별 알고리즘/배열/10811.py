n, m =  map(int, input().split())
a = []
for i in range(n):
    a.append(i+1)

for index in range(m):
    i, j = map(int, input().split())
    a[i-1:j] = a[i-1:j][::-1]

for i in a:
    print(i, end=" ")