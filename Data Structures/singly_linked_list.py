class Node(object):
    """
    Implements node structure to be used in singly linked list.
    """
    def __init__(self, data, next_ =None):
        self.data = data
        self.next_ = next_


    def __str__(self):
        return str(self.data)

class SinglyLinkedList(object):
    """
    This is a very rudimentary class, created for the sole purpose of solving the chapter 8
    alogirthms in Elements of Programming Interviews.
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def print_list(self):
        n = self.head
        while n is not None:
            print str(n.data),
            n = n.next_

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            curr_node = self.head
            while curr_node.next_ is not None:
                curr_node = curr_node.next_
            curr_node.next_ = Node(data)
        self.size += 1
        return

