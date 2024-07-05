a = input()
b = ['']
for i in range(len(a)):
    if a[i] == a[-(i+1)]:
        b[0] = 1
    else:
        b[0] = 0
        break
print(b[0])