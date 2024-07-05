a = int(input())
b = []
for i in range(a):
    b.append(int(input()))

for i in range(a):
    for j in range(1,i+1):
        if b[j-1]>b[j]:
            b[j-1],b[j] = b[j],b[j-1]
    

for i in b:
    print(i, end="")