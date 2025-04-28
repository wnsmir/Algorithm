import sys
input = sys.stdin.readline

N = int(input())
from collections import deque

que = deque()

def push(X):
    que.append(X)

def pop():
    if len(que) == 0:
        print(-1)
    else:
        print(que.popleft())

def size():
    print(len(que))

def empty():
    if len(que) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(que) == 0:
        print(-1)
    else:
        print(que[0])

def back():
    if len(que) == 0:
        print(-1)
    else:
        print(que[-1])

for i in range(N):
    inputs = input().split()
    func = inputs[0]
    X = int(inputs[1]) if len(inputs) > 1 else None

    if func == "push":
        push(X)

    elif func == "pop":
        pop()

    elif func == "size":
        size()

    elif func == "empty":
        empty()

    elif func == "front":
        front()
        
    elif func == "back":
        back()