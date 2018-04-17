import time
import os

a_list = ['a', 'b', 'mpilgram', 'z', 'example']
a_list1 = list((3, 5, 7, 8, 11))
print(a_list1)
print(list(range(1, 10, 2)))
print(list('hello world'))

a_list = a_list + [7]
print(a_list)

a_list.append(9)
print(a_list)

result = []
start = time.time()

print("---------分割-------------")


#
# for i in range(10000):
#     result = result + [i]
#
# print(len(result), ',', time.time() - start)
#
# result = []
# start = time.time()
#
# for i in range(10000):
#     result.append(i)
#
# print(len(result), ',', time.time() - start)
#
# a = [1, 2, 3]
# id(a)
#
# a = [1, 2]
# print(id(a))


def Insert():
    a = []
    for i in range(10000):
        a.insert(0, i)


def Append():
    a = []
    for i in range(10000):
        a.append(i)


start = time.time()
for i in range(10):
    Insert()

print('Insert:', time.time() - start)

start = time.time()
for i in range(10):
    Append()

print('Append:', time.time() - start)

a_list = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in a_list:
    if i == 1:
        a_list.remove(i)

a_list = [1, 1, 1, 1, 1]

print("---------------分割-----------------")

# aList = [1, 2, 3]
# bList = [4, 5, 6]
# cList = zip(aList, bList)
# print(list(cList))
# for i in enumerate(cList):
#     print(i)
#
# for index, ch in enumerate('SDIBT'):
#     print((index, ch), end=',')
#


aList = [x * x for x in range(10)]
print(aList)

aList = []
for x in range(10):
    aList.append(x * x)
print(aList)

freshfruit = [' banana', ' loganberry ', 'passion fruit ']
aList = [w.strip() for w in freshfruit]
print(aList)
#
# freshfruit = [' banana', ' loganberry ', 'passion fruit ']
# for i in freshfruit:
#     i = i.strip()
#     print(i)

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

print([filename for filename in os.listdir('.') if filename.endswith('.py')])

aList = [-1, -4, 6, 7.5, -2.3, 9, -11]
print([i for i in aList if i > 0])

print("---------------分割-----------------")

scores = {"Zhang San": 45, "Li Si": 78, "Wang Wu": 40, "Zhou Liu": 96, "Zhao Qi": 65, "Sun Ba": 90, "Zheng Jiu": 78,
          "Wu Shi": 99, "Dong Shiyi": 60}

highest = max(scores.values())
lowest = min(scores.values())
print("最高分:")
print(highest)
print("最低分")
print(lowest)

average = sum(scores.values()) * 1.0 / len(scores)
print("平均分")
print(average)

highestPerson = [name for name, score in scores.items() if score == highest]

print(highestPerson)

print([(x, y) for x in range(3) for y in range(3)])

print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print([[row[i] for row in matrix] for i in [0, 1, 2, 3]])

print(list(zip(*matrix)))

a = 3,
print(a)
print(tuple('abcdefg'))
print(aList)
print(tuple(aList))

x, y, z = 1, 2, 3
print(x, y, z)

v_tuple = (False, 3.5, 'exp')
x, y, z = v_tuple

# 序列解包，可以用于列表和字典。默认对字典“键”进行操作，对键-值操作时，需要items()方法，对值 操作，需要使用values()方法
a = [1, 2, 3]
b, c, d = a
s = {'a': 1, 'b': 2, 'c': 3}
b, c, d = s.items()
print("items()方法对键值对进行操作:", b, c, d)
b, c, d = s
print("默认方法对键进行操作:", b, c, d)
b, c, d = s.values()
print("values()方法对键进行操作:", b, c, d)

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
for k, v in zip(keys, values):
    print((k, v))

g = ((i + 2) ** 2 for i in range(10))
print(g)
tuple(g)
print(g)
g = ((i + 2) ** 2 for i in range(10))
print(list(g))
g = ((i + 2) ** 2 for i in range(10))
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# g = ((i + 2) ** 2 for i in range(10))
# for i in g:
#     print(i)

a = (1, 2, 3, 4, 5)
b = 'Hello world.'


def demo():
    a = 3
    b = [1, 2, 3]
    print('locals:', locals())
    print('globals', globals())


# demo()

a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}
print(a_dict)

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

dictionary = dict(zip(keys, values))

print(dictionary)

d = dict(name='Dong', age=37)
print(d)

adict = dict.fromkeys(['name', 'age', 'sex'])
print(adict)

aDict = {'name': 'Dong', 'sex': 'male', 'age': '37'}
print(aDict.get('address'))
print(aDict.get('address', 'SDIBT'))

aDict['score'] = aDict.get('score', [])
aDict['score'].append(98)
aDict['score'].append(97)
print(aDict)

aDict = {'name': 'Dong', 'sex': 'male', 'age': '37'}
for item in aDict.items():
    print(item)

for key in aDict.keys():
    print(key)
for key, value in aDict.items():
    print(key, value)

print(aDict.keys())
print(aDict.values())
