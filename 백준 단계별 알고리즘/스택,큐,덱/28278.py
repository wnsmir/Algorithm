class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0  # 스택의 크기를 추적하기 위한 변수

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            print(-1)  # 스택이 비어 있는 경우 -1 출력
        else:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            print(data)  # 스택의 맨 위 정수를 출력

    def peek(self):
        if self.top is None:
            print(-1)  # 스택이 비어 있는 경우 -1 출력
        else:
            print(self.top.data)  # 스택의 맨 위 정수를 출력

    def is_empty(self):
        if self.top is None:
            print(1)  # 스택이 비어 있는 경우 1 출력
        else:
            print(0)  # 스택이 비어 있지 않은 경우 0 출력

    def count_stack(self):
        print(self.size)  # 스택의 크기 출력

# 명령 처리 프로그램
import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
stack = Stack()

for i in range(1, N + 1):
    command = data[i]
    if command.startswith('1'):
        _, num = command.split()
        stack.push(int(num))
    elif command == '2':
        stack.pop()
    elif command == '3':
        stack.count_stack()
    elif command == '4':
        stack.is_empty()
    elif command == '5':
        stack.peek()