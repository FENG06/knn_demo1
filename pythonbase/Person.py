from typing import ByteString

import types


class Person(object):
    def __init__(self, name='', age=20, sex='man'):
        self.__sex = sex
        self.__age = age
        self.__name = name
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        print(type(name))
        if type(name) != str:
            print('name must be string')
            return

    def setAge(self, age):
        if type(age) != int:
            print('age must be int')
            return

    def setSex(self, sex):
        if sex != 'man' and sex != 'woman':
            print('sex must be "man" or "woman"')
            return

    def show(self):
        print(self.__name)
        print(self.__age)
        print(self.__sex)


class Teacher(Person):
    def __init__(self, name='', age=30, sex='man', department='Computer'):
        super(Teacher, self).__init__(name, age, sex)
        # Person.__init__(self, name, age, sex)
        self.__department = department
        self.setDepartment(department)

    def setDepartment(self, department):
        if type(department) != str:
            print('department must be a string')
            return

    def show(self):
        super(Teacher, self).show()
        print(self.__department)


if __name__ == '__main__':
    zhangsan = Person('Zhang San', 19, 'man')
    zhangsan.show()
    lisi = Teacher('Li Si', 32, 'man', 'Math')
    lisi.show()
    #
