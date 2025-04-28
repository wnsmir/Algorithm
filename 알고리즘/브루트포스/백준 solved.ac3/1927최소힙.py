import heapq
import sys
input = sys.stdin.readline
min_heap = []

N = int(input())
for _ in range(N):
    num = int(input())
    if num > 0:
        heapq.heappush(min_heap, num)
    elif num == 0:
        if len(min_heap) == 0:
            print(0)
        else:
            min = heapq.heappop(min_heap)
            print(min)