from collections import deque


class Stack:
    def __init__(self):
        self.items = deque()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def swapping_elements(item1, item2):
    queue = Stack()
    queue.push(item1)
    queue.push(item2)
    item1 = queue.pop()
    item2 = queue.pop()

    print(item1, item2)


swapping_elements(1, 2)
