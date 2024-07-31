N = int(input())

num = 666
count = 0
i = 665

while count < N:
    i += 1
    if str(num) in str(i):
        count += 1

print(i)