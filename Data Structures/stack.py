
class Stack():
    def __init__(self):
        """Initialize an empty stack"""
        self.list = []

    def empty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

    def top(self):
        return self.list[-1]

    def push(self, item):
        self.list.append(item)

    def pop(self):
        self.list.pop()

    def size(self):
        return len(self.list)

    def __str__(self):
        return " ".join([str(val) for val in reversed(self.list)])

if __name__ == "__main__":
    print("Initializing stack")
    s = Stack()
    if s.empty():
        print("Stack is empty")
    for i in range(1,11):
        s.push(i)
    print(s)
    print("Popping")
    s.pop()
    print(s)
    print("Size", s.size())
