import types
# from __builtin__ import long
from numpy import long


class MyArray:
    "All the elements in this array must be numbers"
    __value = []
    __size = 0

    def __IsNumber(self, n):
        if type(n) != int and type(n) != float \
                and type(n) != complex and type(n) != long:
            return False
        return True

    def __init__(self, *args):
        for arg in args:
            if not self.__IsNumber(arg):
                print("All the elements must be numbers")
                return
        self.__value = []
        for arg in args:
            self.__value.append(arg)
        self.__size = len(args)

    def __add__(self, n):
        if not self.__IsNumber(n):
            print('+operating with', type(n), 'and type is not supported')
            return
        b = MyArray()
        for v in self.__value:
            b.__value.append(v + n)
            return b

    def __len__(self):
        return len(self.__value)
