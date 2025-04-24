def lower_bound(arr, x):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def lis_length(sequence):
    tails = []
    for x in sequence:
        # x를 어디에 놓아야 tails가 오름차순을 유지하며
        # '끝값 최소' 상태를 지킬 수 있는지 찾는다
        i = lower_bound(tails, x)
        if i == len(tails):
            # x가 지금까지 모든 끝값보다 크다면
            # 새로운 길이의 수열을 만들 수 있음
            tails.append(x)
        else:
            # 길이 i+1짜리 수열의 끝값을 더 작게 교체하여
            # 뒤의 확장 가능성을 키운다
            tails[i] = x
    # tails의 길이가 곧 LIS의 길이
    return len(tails)

def main():
    # 입력
    N = int(input().strip())
    A = list(map(int, input().split()))
    # 계산 및 출력
    print(lis_length(A))

if __name__ == '__main__':
    main()
