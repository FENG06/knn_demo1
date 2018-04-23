class A:
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('__private() method of A')

    def public(self):
        print('public() method of A')


class B(A):
    def __private(self):
        print('__private method of B')

    def public(self):
        print('public  method of B')


b = B
print('\n'.join(dir(b)))  # 查看对象b的成员


class C(A):
    def __init__(self):
        self.__private()
        self.public()

    def __private(self):
        print('__private method of C')

    def public(self):
        print('public method of C')


c = C
print(c)
print('\n'.join(dir(c)))
