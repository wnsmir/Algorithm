def sign(x):
    if x > 0: return 1
    elif x < 0: return -1
    else: return 0

def build(arr, tree, node, start, end):
    if start == end:
        tree[node] = sign(arr[start])
    else:
        mid = (start + end) // 2
        build(arr, tree, node*2, start, mid)
        build(arr, tree, node*2+1, mid+1, end)
        tree[node] = tree[node*2] * tree[node*2+1]

def update(tree, node, start, end, idx, val):
    if start == end:
        tree[node] = sign(val)
    else:
        mid = (start + end) // 2
        if idx <= mid:
            update(tree, node*2, start, mid, idx, val)
        else:
            update(tree, node*2+1, mid+1, end, idx, val)
        tree[node] = tree[node*2] * tree[node*2+1]

def query(tree, node, start, end, l, r):
    if r < start or end < l:
        return 1
    if l <= start and end <= r:
        return tree[node]
    mid = (start + end) // 2
    left = query(tree, node*2, start, mid, l, r)
    right = query(tree, node*2+1, mid+1, end, l, r)
    return left * right


# =====================
# 여러 테스트 케이스 처리 (sys 없이)
# =====================
while True:
    try:
        line = input().strip()
        if not line:
            continue
        N, K = map(int, line.split())
        number = list(map(int, input().split()))

        tree = [1] * (4*N)
        build(number, tree, 1, 0, N-1)

        result = []
        for _ in range(K):
            order, I, V = input().split()
            I, V = int(I), int(V)

            if order == "C":
                update(tree, 1, 0, N-1, I-1, V)
            else:
                res = query(tree, 1, 0, N-1, I-1, V-1)
                if res > 0: result.append("+")
                elif res < 0: result.append("-")
                else: result.append("0")

        print("".join(result))

    except EOFError:
        break