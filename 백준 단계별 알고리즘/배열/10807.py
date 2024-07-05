a = int(input())
b = list(map(int, input().split()))
c = int(input())
sum = 0

for i in range(a):
    if c == b[i]:
        sum = sum + 1

print(sum)