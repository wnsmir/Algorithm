sets = set()
N = int(input())
nums = input().split()

for i in range(N):
    sets.add(int(nums[i]))
M = int(input())
nums = input().split()
print(nums)
for i in range(M):
    if int(nums[i]) in sets:
        print(1)
    else:
        print(0)