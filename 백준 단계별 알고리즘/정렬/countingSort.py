import sys
input = sys.stdin.readline
    
MAX_NUM = 10000
count = [0] * (MAX_NUM + 1)
    

N = int(input().strip())
    

for _ in range(N):
    num = int(input().strip())
    count[num] += 1
    

for i in range(MAX_NUM + 1):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)