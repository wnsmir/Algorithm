m = int(input())

for _ in range(m):
    n = int(input())
    nums = []

    while len(nums) < n:
        nums += list(map(int, input().split()))

    new_num = []
    result = []

    for i in range(1, len(nums) + 1):
        new_num.append(nums[i - 1])
        if i % 2 != 0:  # 홀수 개일 때만 중앙값 출력
            new_num.sort()
            result.append(str(new_num[i // 2]))

    print(len(result))
    for i in range(len(result)):
        print(result[i], end=' ')
        if (i + 1) % 10 == 0:
            print()
    if len(result) % 10 != 0:
        print()