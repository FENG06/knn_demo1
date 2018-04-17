import time

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
