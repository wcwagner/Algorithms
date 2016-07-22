class ListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, data):
        if self.next is None:
            self.next = ListNode(data)
        else:
            self.next.append(data)

    def insert_after(self, data):
        if self.next is None:
            self.next = ListNode(data)
        else:
            memo = self.next
            self.next = ListNode(data)
            self.next.next = memo

    def remove_next(self):
        if self.next is None:
            return
        else:
            self.next = self.next.next

    def __getitem__(self, index):
        if index == 0:
            return self.data
        elif self.next is None:
            raise IndexError()
        else:
            return self.next[index - 1]
