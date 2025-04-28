def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

import sys
input = sys.stdin.readline

N = int(input().strip())
words = set()

for _ in range(N):
    word = input().strip()
    words.add(word)  # 중복 제거

sorted_words = quick_sort(list(words))

for word in sorted_words:
    print(word)