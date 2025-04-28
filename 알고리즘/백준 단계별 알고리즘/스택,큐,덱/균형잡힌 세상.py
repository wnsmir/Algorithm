import sys

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
            return None
        data = self.top.data
        self.top = self.top.next
        return data
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None

import sys

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
            return None
        data = self.top.data
        self.top = self.top.next
        return data
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    def is_empty(self):
        return self.top is None

def main():
    input_text = sys.stdin.read().strip().splitlines()
    results = []

    for line in input_text:
        line = line.rstrip()
        if line.strip() == "":
            results.append("yes")
            continue
        
        stack = Stack()
        balanced = True

        for char in line:
            if char in "([":  # 여는 괄호를 만나면 스택에 푸시
                stack.push(char)
            elif char in ")]":  # 닫는 괄호를 만나면 스택에서 팝하고 매칭 검사
                top = stack.pop()
                if (char == ")" and top != "(") or (char == "]" and top != "["):
                    balanced = False
                    break
        
        if balanced and stack.is_empty():
            results.append("yes")
        else:
            results.append("no")

    for result in results:
        print(result)

if __name__ == "__main__":
    main()