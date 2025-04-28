a, b, c, d, e, f = map(int, input().split())
range = range(-999, 1000)
for x in range:
    for y in range:
        if a*x + b*y == c and d*x + e*y == f:
            print(x,y)