def insertion_sort(strings):
    for i in range(1, len(strings)):
        key = strings[i]
        j = i - 1
        while j >= 0 and strings[j] > key:
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = key
    return strings
import sys
input = sys.stdin.readline
N = int(input().strip())
words = []

for _ in range(N):
    word = input().strip()
    if word not in words:
        words.append(word)

sorted_words = insertion_sort(words)
for word in sorted_words:
    print(word)