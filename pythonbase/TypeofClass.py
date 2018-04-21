class Root:
    __total = 0

    def __init__(self, v):
        self.__value = v
        Root.__total += 1

    def show(self):
        print('self.__value:', self.__value)
        print('self.__total:', self.__total)

    @classmethod  # 类方法
    def classShowTotal(cls):
        print(cls.__total)

    @staticmethod  # 静态方法
    def staticShowTotal():
        print(Root.__total)


r = Root(3)
r.classShowTotal()  # 通过对象来调用类方法

r.staticShowTotal()  # 通过对象来调用静态方法

r.show()

rr = Root(3)
Root.classShowTotal()  # 通过类名调用类方法

Root.staticShowTotal()  # 通过类名调用静态方法

# Root.show()  # 通过类名直接调用实例方法，失败

# 可以通过下面的方法调用方法并访问实例成员
Root.show(r)
r.show()
