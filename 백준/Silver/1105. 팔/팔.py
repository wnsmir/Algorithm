L, R = input().split()

if len(L) != len(R):
    print(0)

else:
    count = 0
    for left, right in zip(L, R):
        if left == right:
            if left == '8' and right == '8':
                count += 1
        else: 
            break
    print(count)