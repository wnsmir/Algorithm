list = []
for i in range(100):
    list.append([0]*100)

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    for _ in range(10):
        b = b+1
        for i in range(10):
            list[a-1+i][b-1] = 1

count = 0
for row in list:
    count += row.count(1)

print(count)