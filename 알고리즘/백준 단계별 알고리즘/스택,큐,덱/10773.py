class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            node = Node(data)
            node.next = self.top
            self.top = node
    
    def pop(self):
        if self.top is None:
            return
        data = self.top.data
        self.top = self.top.next
        return data

stack = Stack()
K = int(input())
for _ in range(K):
    a = int(input())
    if a == 0:
        stack.pop()
    else:
        stack.push(a)
sum = 0
while stack.top:
    sum += stack.pop()

print(sum)