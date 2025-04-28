def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0
    
    # 두 리스트를 비교하여 작은 값을 결과 리스트에 추가합니다.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    
    # 남아있는 요소들을 결과 리스트에 추가합니다.
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])
    
    return sorted_list
import sys
input = sys.stdin.readline

N = int(input().strip())
arr = []
for _ in range(N):
    a = int(input().strip())
    arr.append(a)

sorted_arr = merge_sort(arr)
for num in sorted_arr:
    print(num)