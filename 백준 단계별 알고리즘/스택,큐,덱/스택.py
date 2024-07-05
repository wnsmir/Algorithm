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
    
    def peek(self):
        if self.top is None:
            return
        return self.top.data
    
    def is_empty(self):
        return self.top is None

    def print_stack(self):
        current_node = self.top
        while current_node:
            print(current_node.data)
            current_node = current_node.next
