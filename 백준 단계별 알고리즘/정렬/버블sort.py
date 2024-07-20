n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

for i in range(len(arr)):
    for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

for num in arr:
     print(num)