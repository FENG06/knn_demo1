import heapq
import os
import queue
import random
import time
from collections import deque

import myQueue
import Stack
import types

# a_list = ['a', 'b', 'mpilgram', 'z', 'example']
# a_list1 = list((3, 5, 7, 8, 11))
# print(a_list1)
# print(list(range(1, 10, 2)))
# print(list('hello world'))
#
# a_list = a_list + [7]
# print(a_list)
#
# a_list.append(9)
# print(a_list)
#
# result = []
# start = time.time()
#
# print("---------分割-------------")
#
#
# #
# # for i in range(10000):
# #     result = result + [i]
# #
# # print(len(result), ',', time.time() - start)
# #
# # result = []
# # start = time.time()
# #
# # for i in range(10000):
# #     result.append(i)
# #
# # print(len(result), ',', time.time() - start)
# #
# # a = [1, 2, 3]
# # id(a)
# #
# # a = [1, 2]
# # print(id(a))
#
#
# def Insert():
#     a = []
#     for i in range(10000):
#         a.insert(0, i)
#
#
# def Append():
#     a = []
#     for i in range(10000):
#         a.append(i)
#
#
# start = time.time()
# for i in range(10):
#     Insert()
#
# print('Insert:', time.time() - start)
#
# start = time.time()
# for i in range(10):
#     Append()
#
# print('Append:', time.time() - start)
#
# a_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# for i in a_list:
#     if i == 1:
#         a_list.remove(i)
#
# a_list = [1, 1, 1, 1, 1]
#
# print("---------------分割-----------------")
#
# # aList = [1, 2, 3]
# # bList = [4, 5, 6]
# # cList = zip(aList, bList)
# # print(list(cList))
# # for i in enumerate(cList):
# #     print(i)
# #
# # for index, ch in enumerate('SDIBT'):
# #     print((index, ch), end=',')
# #
#
#
# aList = [x * x for x in range(10)]
# print(aList)
#
# aList = []
# for x in range(10):
#     aList.append(x * x)
# print(aList)
#
# freshfruit = [' banana', ' loganberry ', 'passion fruit ']
# aList = [w.strip() for w in freshfruit]
# print(aList)
# #
# # freshfruit = [' banana', ' loganberry ', 'passion fruit ']
# # for i in freshfruit:
# #     i = i.strip()
# #     print(i)
#
# vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([num for elem in vec for num in elem])
#
# print([filename for filename in os.listdir('.') if filename.endswith('.py')])
#
# aList = [-1, -4, 6, 7.5, -2.3, 9, -11]
# print([i for i in aList if i > 0])
#
# print("---------------分割-----------------")
#
# scores = {"Zhang San": 45, "Li Si": 78, "Wang Wu": 40, "Zhou Liu": 96, "Zhao Qi": 65, "Sun Ba": 90, "Zheng Jiu": 78,
#           "Wu Shi": 99, "Dong Shiyi": 60}
#
# highest = max(scores.values())
# lowest = min(scores.values())
# print("最高分:")
# print(highest)
# print("最低分")
# print(lowest)
#
# average = sum(scores.values()) * 1.0 / len(scores)
# print("平均分")
# print(average)
#
# highestPerson = [name for name, score in scores.items() if score == highest]
#
# print(highestPerson)
#
# print([(x, y) for x in range(3) for y in range(3)])
#
# print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
#
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print([[row[i] for row in matrix] for i in [0, 1, 2, 3]])
#
# print(list(zip(*matrix)))
#
# a = 3,
# print(a)
# print(tuple('abcdefg'))
# print(aList)
# print(tuple(aList))
#
# x, y, z = 1, 2, 3
# print(x, y, z)
#
# v_tuple = (False, 3.5, 'exp')
# x, y, z = v_tuple
#
# # 序列解包，可以用于列表和字典。默认对字典“键”进行操作，对键-值操作时，需要items()方法，对值 操作，需要使用values()方法
# a = [1, 2, 3]
# b, c, d = a
# s = {'a': 1, 'b': 2, 'c': 3}
# b, c, d = s.items()
# print("items()方法对键值对进行操作:", b, c, d)
# b, c, d = s
# print("默认方法对键进行操作:", b, c, d)
# b, c, d = s.values()
# print("values()方法对键进行操作:", b, c, d)
#
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3, 4]
# for k, v in zip(keys, values):
#     print((k, v))
#
# g = ((i + 2) ** 2 for i in range(10))
# print(g)
# tuple(g)
# print(g)
# g = ((i + 2) ** 2 for i in range(10))
# print(list(g))
# g = ((i + 2) ** 2 for i in range(10))
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# # g = ((i + 2) ** 2 for i in range(10))
# # for i in g:
# #     print(i)
#
# a = (1, 2, 3, 4, 5)
# b = 'Hello world.'
#
#
# def demo():
#     a = 3
#     b = [1, 2, 3]
#     print('locals:', locals())
#     print('globals', globals())
#
#
# # demo()
#
# a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
# print(a_dict)
#
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3, 4]
#
# dictionary = dict(zip(keys, values))
#
# print(dictionary)
#
# d = dict(name='Dong', age=37)
# print(d)
#
# adict = dict.fromkeys(['name', 'age', 'sex'])
# print(adict)
#
# aDict = {'name': 'Dong', 'sex': 'male', 'age': '37'}
# print(aDict.get('address'))
# print(aDict.get('address', 'SDIBT'))
#
# aDict['score'] = aDict.get('score', [])
# aDict['score'].append(98)
# aDict['score'].append(97)
# print(aDict)
#
# aDict = {'name': 'Dong', 'sex': 'male', 'age': '37'}
# for item in aDict.items():
#     print(item)
#
# for key in aDict.keys():
#     print(key)
# for key, value in aDict.items():
#     print(key, value)
#
# print(aDict.keys())
# print(aDict.values())
#
# aDict['age'] = 38
# print(aDict)
#
# aDict['address'] = 'SDIBT'
# print(aDict)
#
# print(aDict.items())
# aDict.update({'a': 'a', 'b': 'b'})
# print(aDict)
#
# a = {3, 5}
#
# a.add(7)
# print(a)
#
# a_set = set(range(8, 14))
# print(a_set)
#
# data = range(10)
# print(list(data))
#
# print(random.choice(data))
# print(random.choice(data))
# # random.shuffle(data)
# # print(data)
#
# heap = []  # 建堆
# for n in data:
#     heapq.heappush(heap, n)
# print(heap)
#
# heapq.heappush(heap, 0.5)
# print(heap)
#
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
# print(heapq.heappop(heap))
#
# print("------------分割---------------")
#
# myheap = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 10, 333]
# print(myheap)
# print(heapq.heapreplace(myheap, 6))
# print(myheap)
#
# print("--------Queue模块的使用方法-----------")
# # q = Queue.Queue()
# # q.put(0)
# # q.put(1)
# # q.put(2)
# #
# # print(q.queue)
#
# q = queue.Queue()
# q.put(0)
# q.put(1)
# q.put(2)
# print(q.queue)
# print(q.get())
# print(q.queue)
#
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.append("Graham")
# print(queue.popleft())
# print(queue.popleft())
# print(queue)
#
# q = myQueue.myQueue()
# q.get()
# q.put(5)
# q.show()
# q.put(7)
# q.put('a')
# q.show()
# q.get()
# q.get()
# q.get()
# q.get()
#
# print("----------栈的使用--------------")
# myStack = []
# myStack.append(3)
# myStack.append(5)
# myStack.append(7)
# print(myStack)
# print(myStack.pop())
# print(myStack.pop())
# print(myStack.pop())
# # print(myStack.pop())
#
# s = Stack.Stack()
# s.push(3)
# s.show()
# s.push(5)
# s.show()
# s.push(7)
# s.show()
# s.pop()
# s.show()
#
# print('----------------二叉树的使用------------')
#
# # import BinaryTree
#
# # root = BinaryTree.BinaryTree('root')
#
#
# print('-----------运算符与条件表达式------------')
#
#
# def Join(chList, sep=None):
#     return (sep or ',').join(chList)
#
#
# chTest = ['1', '2', '3', '4', '5']
# print(Join(chTest))
# print(Join(chTest, ':'))
# print(Join(chTest, " "))
#
# print('----------------选择结构的使用------------')
#
# # endFlag = 'yes'
# # s = 0
# #
# # while endFlag.lower() == 'yes':
# #     x1 = eval(input("请输入一个正整数："))
# #     print(type(x1))
# #     if type(x1) == int and 0 <= x1 <= 100:
# #         s = s + x1
# #     else:
# #         print('不是数字或不符合要求')
# #     endFlag = input('继续输入?(yes or no):')
# # print('整数之和=', s)
#
#
# print('-------------循环结构的使用-------------')
#
# import time
# import math
#
# # start = time.time()
# # for i in range(10000000):
# #     math.sin(i)
# # print('Time Used:', time.time() - start)
# # loc_sin = math.sin
# # start = time.time()
# # for i in range(10000000):
# #     loc_sin(i)
# # print('Time Used:', time.time() - start)
# #
# # print('-----循环结构使用及导入方式的改进-------')
# # import time
# # from math import sin as sin
# #
# # start = time.time()
# # for i in range(10000000):
# #     sin(i)
# # print('Time Used:', time.time() - start)
# # loc_sin = sin
# # start = time.time()
# # for i in range(10000000):
# #     loc_sin(i)
# # print('Time Used:', time.time() - start)
# #
# # print('---------break 和 continue的使用----------')
#
# # i = 1
# # while i < 10:
# #     if i % 2 == 0:
# #         continue
# #     print(i)
#
# for i in range(10):
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#
# # import math
# #
# # n = eval(input('请输入一个整数：'))
# #
# # m = int(math.sqrt(n) + 1)
# #
# # for i in range(2, m):
# #     if n % i == 0:
# #         print('No!')
# #         break
# #     else:
# #         print('Yes!')
#
# print('----------字符串的使用---------')
#
# a = '1234'
# b = '1234'
# print(id(a) == id(b))
#
# a = '1234' * 50
# b = '1234' * 50
# print(id(a) == id(b))
#
# x = 1235
# so = "%o" % x
# print(so)
#
# sh = "%x" % x
# print(sh)
#
# print(chr(ord("3") + 1))
#
# print('%d,%c' % (65, 65))
#
# print('------------format()方法进行字符串格式化-----------')
# print("The number {0:,} in hex is: {0:#x},the number {1} in oct is {1:#o}".format(5555, 55))
# print("my name is {name},my age is {age},and my QQ is {qq}".format(name="Dong Fuguo", age=20, qq="12345678"))
#
# s = "apple,peach,banana,peach,pear"
# print(s.find("peach"))
# print(s.find("peach", 5))
# li = s.split(",")
# print(li)
# s = 'hello world \n\n My name is Dong'
# print(s.split())
#
# import string
# import _string
#
# table = s.maketrans("abcdef123", "uvwxyz@#$")
# s = "Python is a great programming language. I like it!"
# print(s.translate(table))
#
# # a = input(__import__('os').startfile(r'C:\windows\\notepad.exe'))
# # eval(a)
# # inputfile = open()
#
# print('--------函数的使用-------')
#
#
# def say(message, times=1):
#     print(((message + ' ') * times)[0:-1])
#
#
# print(say.__defaults__)
# say('hello')
# say('hello', 3)
#
#
# def demo(newitem, old_list=[]):
#     old_list.append(newitem)
#     return old_list
#
#
# print(demo('5', [1, 2, 3, 4]))
# print(demo('aaa', ['a', 'b']))
# print(demo('a'))
# print(demo('b'))
#
#
# def demo(newitem, old_list=None):
#     if old_list is None:
#         old_list = []
#     old_list.append(newitem)
#     return old_list
#
#
# print(demo('5', [1, 2, 3, 4]))
# print(demo('aaa', ['a', 'b']))
# print(demo('a'))
# print(demo('b'))
#
# print('-------关键参数：实参顺序可以和形参顺序不一致-----')
#
#
# def demo(a, b, c=5):
#     print(a, b, c)
#
#
# demo(3, 7)
# demo(3, 2)
# demo(c=1, a=2, b=5)
#
# print('---------可变长度参数：*p 接收任意多个实参将其放在一个元组中，**p接收显示赋值形式的多个实参将其放在字典中------------')
#
#
# def demo(*p):
#     print(p)
#
#
# demo(1, 2, 3)
# demo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
#
# def demo(**p):
#     for item in p.items():
#         print(item)
#
#
# demo(x=1, y=2, z=3)
#
# print('-----------参数传递的序列解包：在实参名称前加一个星号-------')
#
#
# def demo(a, b, c):
#     print(a + b + c)
#
#
# seq = [1, 2, 3]
# demo(*seq)
#
# dic = {1: 'a', 2: 'b', 3: 'c'}
#
# demo(*(dic.values()))
# demo(*(dic.items()))
#
# print('--------------变量作用域------------')
#
#
# def demo1():
#     global x1  # 声明或创建全局变量
#     x1 = 3  # 修改全局变量的值
#     y1 = 4  # 局部变量
#     print(id(x1))
#     print(x1, y1)
#
#
# x1 = 5
#
# print(id(x1))
# demo1()  # 本次调用修改全局变量x的值
# print(id(x1))
# print(x1)

# print(y1)  # 报错，y1未定义
print('--------------lambda表达式的使用----------')
# f = lambda x, y, z: x + y + z
# print(f(1, 2, 3))
# L = [(lambda x: x ** 2), (lambda x: x ** 3), (lambda x: x ** 4)]
# print(L[0](2), L[1](2), L[2](2), )
#
# L = [1, 2, 3, 4, 5]
# map((lambda x: x + 10), L)

data = list(range(20))
# print(data)
# random.shuffle(data)
# print(data)
# data.sort(key=lambda x: x)
# print(data)
print(data)

data.sort(key=lambda x: len(str(x)), reverse=True)

print(len(str(data)))

print(data)

print('---------高级话题-------')

seq = ['foo', 'x41', '?!', '***']


def func(x):
    return x.isalnum()


print(filter(func, seq))
