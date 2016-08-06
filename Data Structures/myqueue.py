"""Implement a queue using a list. ."""

class MyQueue():

    def __init__(self):
        self.list = []
        self.size = 0

    def empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def front(self):
        return self.list[0]

    def back(self):
        return self.list[-1]

    def enqueue(self, item):
        self.list.append(item)
        self.size += 1

    def dequeue(self):
        self.size -= 1
        return self.list.pop(0)

    def print_(self):
        for d in self.list:
            print(d.data, sep=',')
