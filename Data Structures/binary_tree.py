"""Implement a simple binary tree"""

class Node():
    def __init__(self, val):
        self.data = val
        self.l = None
        self.r = None

class BT():
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_(val, self.root)

    def insert_(self, val, node):
        if val < node.data:
            if node.l is not None:
                self.insert_(val, node.l)
            else:
                node.l = Node(val)
        else:
            if node.r is not None:
                self.insert_(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if self.root is not None:
            return self.find_(val, self.root)
        return None

    def find_(self, val, node):
        if node.data == val:
            return node
        elif val < node.data and node.l is not None:
            return self.find_(val, node.l)
        elif val > node.data and node.r is not None:
            return self.find_(val, node.r)

    def deleteVal(self, val):
        n = self.find(val)
        del n

    def postOrder(self):
        if self.root is not None:
            self.postOrder_(self.root)

    def postOrder_(self, node):
        if node is None:
            return
        self.postOrder_(node.l)
        self.postOrder_(node.r)
        print(str(node.data))

    def inOrder(self):
        if self.root is not None:
            self.inOrder_(self.root)

    def inOrder_(self, node):
        if node is None:
            return
        self.inOrder_(node.l)
        print(str(node.data))
        self.inOrder_(node.r)

    def preOrder(self):
        if self.root is not None:
            self.preOrder_(self.root)

    def preOrder_(self, node):
        if node is None:
            return
        print(str(node.data))
        self.preOrder_(node.l)
        self.preOrder_(node.r)

bt = BT()
bt.insert(4)
bt.insert(2)
bt.insert(1)
bt.insert(3)
bt.insert(6)
bt.insert(5)
bt.insert(7)
bt.getRoot()
bt.postOrder()
bt.inOrder()
bt.preOrder()
