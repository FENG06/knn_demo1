class myQueue:
    def __init__(self, size=10):
        self._content = []
        self._size = size

    def setSize(self, size):
        self._size = size

    def put(self, v):
        if len(self._content) < self._size:
            self._content.append(v)
        else:
            print("The queue is full")

    def get(self):
        if self._content:
            return self._content.pop(0)
        else:
            print("The queue is empty")

    def show(self):
        if self._content:
            print(self._content)
        else:
            print("The queue is empty")

    def empty(self):
        self._content = []

    def isEmpty(self):
        if not self._content:
            return True
        else:
            return False

    def isFull(self):
        if len(self._content) == self._size:
            return True
        else:
            return False
