N, Q = map(int, input().split())
arr = list(map(int, input().split()))

size = 1
while size < N:
    size <<= 1

tree = [0] * (2 * size)
for i in range(N):
    tree[size + i] = arr[i]

for i in range(size - 1, 0, -1):
    tree[i] = tree[2 * i] + tree[2 * i + 1]

def range_query(l, r):
    l += size
    r += size
    s = 0
    while l <= r:
        if l & 1:
            s += tree[l]
            l += 1
        if not (r & 1):
            s += tree[r]
            r -= 1
        l //= 2
        r //= 2

    return s

def point_update(pos, val):
    i = size + pos
    tree[i] = val
    i //= 2
    while i:
        tree[i] = tree[2 * i] + tree[2 * i + 1]
        i //= 2

out = []
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    out.append(str(range_query(x - 1, y - 1)))
    point_update(a - 1, b)

print("\n".join(out))