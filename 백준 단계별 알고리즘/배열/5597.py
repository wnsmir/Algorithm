a = []
x = []
for i in range(28):
    b = int(input())
    a.append(b)

for i in range(30):
    if i+1 in a:
        pass
    else:
        x.append(i+1)

for i in x:
    print(i)