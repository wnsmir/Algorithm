from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)  # 큐의 끝에 요소 추가

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()  # 큐의 앞에서 요소 제거 및 반환
        else:
            raise IndexError("dequeue from an empty queue")

    def front(self):
        if not self.is_empty():
            return self.queue[0]  # 큐의 앞 요소 반환 (제거하지 않음)
        else:
            raise IndexError("front from an empty queue")

    def is_empty(self):
        return len(self.queue) == 0  # 큐가 비어 있는지 확인

    def size(self):
        return len(self.queue)  # 큐의 크기 반환

    def __str__(self):
        return str(self.queue)