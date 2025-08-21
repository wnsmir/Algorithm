from collections import Counter

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# 누적합 구하기
def prefix_sums(arr):
    prefix = [0]
    for x in arr:
        prefix.append(prefix[-1] + x)
    return prefix

prefixA = prefix_sums(A)
prefixB = prefix_sums(B)

# 부 배열 합 리스트 만들기
def subarray_sums(prefix):
    sums = []
    n = len(prefix)-1
    for i in range(1, n+1):
        for j in range(i, n+1):
            sums.append(prefix[j] - prefix[i-1])
    return sums

subA = subarray_sums(prefixA)
subB = subarray_sums(prefixB)

# subB 빈도 세기
countB = Counter(subB)

# 정답 구하기
answer = 0
for a in subA:
    answer += countB[T - a]

print(answer)