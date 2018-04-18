# Õ»µÄÊ¹ÓÃ
class Stack:
    def __init__(self, size=10):
        self._content = []
        self._size = size

    def empty(self):
        self._content = []

    def isEmpty(self):
        if not self._content:
            return True
        else:
            return False

    def setSize(self, size):
        self._size = size

    def isFull(self):
        if len(self._content) == self._size:
            return True
        else:
            return False

    def push(self, v):
        if len(self._content) < self._size:
            self._content.insert(0, v)
        else:
            print('Stack Full!')

    def pop(self):
        if len(self._content) > 0:
            v = self._content[0]
            del self._content[0]
            return v
        else:
            print('Stack is empty!')

    def show(self):
        print(self._content)
