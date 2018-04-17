import sys

# from importlib import reload
#
# reload(sys)
# sys.setdefaultencoding('uft8')
import math
import random


# coding=gbk


class KdNode(object):
    def __init__(self, dom_elt, spilt, left, right):
        self.dom_elt = dom_elt
        self.spilt = spilt
        self.left = left
        self.right = right


class KdTree(object):
    def __init__(self, data):
        k = len(data[0])

        def CreatNode(spilt, data_set):
            if not data_set:
                return None
            data_set.sort(key=lambda x: x[spilt])
            spilt_pos = len(data_set) // 2
            median = data_set[spilt_pos]
            spilt_next = (spilt + 1) % k

            return KdNode(median, spilt,
                          CreatNode(spilt_next, data_set[:spilt_pos]),
                          CreatNode(spilt_next, data_set[spilt_pos + 1:]))

        self.root = CreatNode(0, data)


def preorder(root):
    print(root.dom_elt)
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)


if __name__ == "__main__":
    data = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]
    kd = KdTree(data)
    preorder(kd.root)
    print('1' * 5)
    print([1, 2, 3] * 5)
    print(3 * 'a')
    print([1, 2, 3] + [4, 5, 6])
    print(map(math.sin, [1, 2, 3] + [4, 5, 6]))
    print(ord('a'))
    print(chr(67))
    print(str(1234))
    a = [random.randint(1, 100) for i in range(10)]
    print(a)
    print(max(a), min(a), sum(a))
    print(sum(a) / len(a))

    # x = [1, 2, 3, 4, 5, 6]
    y = 3
    z = y
    print(y)

    # del y
    # print(y)

    # z = input("Please input")

    x = input('请输入一个三位数：')
    a = int(x) // 100
    b = int(x) // 10 % 10
    c = int(x) % 10
    print(a, b, c)

    s = input('x,y,z=')
    x, y, z = s.split(',')
    if x > y:
        x, y = y, x
    if x > z:
        x, z = z, x
    if y > z:
        y, z = z, y
    print(x, y, z)
