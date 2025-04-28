a, b = map(int, input().split())
c = int(input())

if c > 60:
    if c%60 + b >= 60:
        if (a + 1 + c//60) >= 24:
            print(a + 1 + c//60 - 24, c%60 + b - 60, sep=" ")
        else:
            print(a + 1 + c//60, c%60 + b - 60, sep=" ")
    else:
        if (a + c//60) >= 24:
            print(a + c//60 - 24, c%60 + b, sep=" ")
        else:
            print(a + c//60, c%60 + b, sep=" ")
else:
    if c + b >= 60:
        if (a + 1) >= 24:
            print(a + 1 - 24, c + b - 60,sep=" ")
        else:
            print(a + 1, c + b - 60,sep=" ")

    else:
        print(a, c + b, sep=" ")