n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
arr.sort()
for a in arr:
    print(a)