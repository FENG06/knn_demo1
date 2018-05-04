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
