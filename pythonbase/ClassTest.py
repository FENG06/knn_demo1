class Test:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):  # 只读，无法删除或修改
        return self.__value


t = Test(3)
print(t.value)

# t.value = 5

t.v = 5  # 动态增加新成员
print(t.v)

del t.v  # 动态删除成员
# del t.value  # 试图删除对象属性，失败

# print(t.v)


print('----将属性设置为可读、可修改，但不允许删除--------')


class Test:
    def __init__(self, value):
        self.__value = value

    def __get__(self):
        return self.__value

    def __set__(self, v):
        self.__value = v

    value = property(__get__, __set__)


t = Test(3)  # 允许读取属性值
print(t.value)

t.value = 5  # 允许修改属性值
print(t.value)

# del t.value  # 试图删除属性，失败
