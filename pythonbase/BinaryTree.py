class BinaryTree:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._data = None

    def insertLeftChild(self, value):
        if self._left:
            print('_left child tree already exists')
        else:
            self._left = BinaryTree(value)
            return self._left

    def insertRightChild(self, value):
        if self._right:
            print('right child tree already exists.')
        else:
            self._right = BinaryTree(value)
            return self._right

    def show(self):
        print(self._data)

    def preOrder(self):
        print(self._data)
        if self._left:
            self._left.preOrder()
        if self._right:
            self._right.preOrder()

    def postOrder(self):
        if self._left:
            self._left.postOrder()
        if self._right:
            self._right.postOrder()

    def inOrder(self):
        if self._left:
            self._left.inOrder()
        print(self._data)
        if self._right:
            self._right.inOrder()


if __name__ == '__main__':
    print('Please use me as a module')
