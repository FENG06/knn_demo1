# f = open('sample.txt', 'a+')
# s = '文本文件的读取方法\n文本文件的写入方法\n'
# f.write(s)
# f.close()
#
# # 更合适的方法
# s = '文本文件的读取方法\n文本文件的写入方法\n'
# with open('sample.txt', 'a+') as f:
#     f.write(s)


fp = open('sample.txt', 'r')
print(fp.read(5))
print(fp.read(7))
print(fp.seek(7))  # 把文件指针移动到新的位置
print(fp.read(2))

# pickle模块
import pickle

f = open('sample_pickle.dat', 'wb')
n = 7
i = 13000000
a = 99.056
s = '中国人民123abc'
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tu = (-5, 10, 8)
coll = {4, 5, 6}
dic = {'a': 'apple', 'b': 'banana', 'g': 'grape', 'o': 'orange'}
try:
    pickle.dump(n, f)  # 表示后面将要写入的数据个数
    pickle.dump(i, f)  # 把整数i转换成自节串，并写入文件
    pickle.dump(a, f)
    pickle.dump(s, f)
    pickle.dump(lst, f)
    pickle.dump(tu, f)
    pickle.dump(coll, f)
    pickle.dump(dic, f)
except:
    print('写文件异常！')
finally:
    f.close()

# 读取写入的二进制文件
f = open('sample_pickle.dat', 'rb')
n = pickle.load(f)
i = 0
while i < n:
    x = pickle.load(f)
    print(x)
    i = i + 1
f.close()

print('---------------分割---------')

# struct 模块
import struct

n = 1300000000
x = 96.45
b = True
s = 'al@中国'
sn = struct.pack('if?', n, x, b)  # 把整数n，浮点数x，布尔对象b依次转换为字符串
print(sn)
f = open('sample_struct.dat', 'wb')
f.write(sn)  # 写入字符串
# f.write(s)  # 字符串可以直接写入
f.close()

f = open('sample_struct.dat', 'rb')
sn = f.read(9)
tu = struct.unpack('if?', sn)
print(tu)
n = tu[0]
x = tu[1]
bl = tu[2]
print('n=', n)
print('x=', x)
print('bl=', bl)
s = f.read(9)
f.close()
print('s=', s)
