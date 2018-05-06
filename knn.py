import random
import operator
import datetime
import numpy as np
import pandas as  pd
import statsmodels.api as sm
import matplotlib
import matplotlib.pyplot as plt

# 100个正态分布的悲伤
grief_heigts = np.random.normal(50, 6, 100)
grief_weights = np.random.normal(5, 0.5, 100)

# 100个正态分布的痛苦
agony_heights = np.random.normal(30, 6, 100)
agony_weights = np.random.normal(4, 0.5, 100)

# 100个正态分布的绝望
despair_heights = np.random.normal(45, 6, 100)
despair_weights = np.random.normal(2.5, 0.5, 100)

# 设置图片大小
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 15
fig_size[1] = 10

# scatter参数（x,y(输入数据，相同长度的数组序列),s(标量或想入shape(n,)数组，可选),c(色彩或颜色序列),marker(MarkerStyle)）
# marker参数：'.' point; ','pixel像素; 'o',circle,圈; 'v' triangle_down 倒三角；‘^’ triangle_up 正三角；
# “<” triangle_left 左三角形；‘>’ triangle_right 右三角


plt.scatter(40, 2.7, c='m', marker='*', s=200, alpha=0.8)
plt.scatter(grief_heigts, grief_weights, c='g', marker='s', s=50, alpha=0.8)
plt.scatter(agony_heights, agony_weights, c='b', marker='^', s=50, alpha=0.8)
plt.scatter(despair_heights, despair_weights, c='y', s=50, alpha=0.8)
plt.axis((10, 70, 1, 7))
plt.xlabel('身高(cm)', size=15)
plt.ylabel('体重(kg)', size=15)


# plt.show()


class kdtree(object):
    # 创建kd树
    # point_list是一个list的pair，pair[0]是一tuple的特征，pair[1]是类别
    def __init__(self, point_list, depth=0, root=None):

        if len(point_list) > 0:

            # 轮换按照树深度选择坐标轴
            k = len(point_list[0][0])
            axis = depth % k

            # 选中位线，切
            point_list.sort(key=lambda x: x[0][axis])
            median = len(point_list) // 2

            self.axis = axis
            self.root = root
            self.size = len(point_list)

            # 造节点
            self.node = point_list[median]

            # 递归造右枝和左枝
            if len(point_list[:median]) > 0:
                self.left = kdtree(point_list[:median], depth + 1, self)
            else:
                self.left = None
            if len(point_list[:median]) > 0:
                self.right = kdtree(point_list[:median], depth + 1, self)
            else:
                self.right = None
        else:
            return None

    # 在树上加一点
    def insert(self, point):
        self.size += 1

        # 分析是左还是右，递归加在叶子上
        if point[0][self.axis] < self.node[0][self.axis]:
            if self.left is not None:
                self.left.insert(point)
            else:
                self.left = kdtree([point], self.axis + 1, self)
        else:
            if self.right is not None:
                self.right.insert(point)
            else:
                self.right = kdtree([point], self.axis + 1, self)

    # 输入一点
    #  按切分寻找叶子

    def find_leaf(self, point):
        if self.left is None and self.right is None:
            return self
        elif self.left is None:
            return self.right.find_leaf(point)
        elif self.right is None:
            return self.left.find_leaf(point)
        elif point[self.axis] < self.node[0][self.axis]:
            return self.left.find_leaf(point)
        else:
            return self.right.find_leaf(point)

    # 查找最近的k个点
    # 输入一点，一距离函数，一K。距离函数默认是L2
    def knearest(self, point, k=1, dist=lambda x, y: sum(map(lambda u, v: (u - v) ** 2, x, y))):
        # 往下戳到最底叶
        leaf = self.find_leaf(point)
        # 从叶子往上爬
        return leaf.k_down_up(point, k, dist, result=[], stop=self, visited=None)

    # 从下往上爬函数，stop是到哪里去，visited是从哪里来
    def k_down_up(self, point, k, dist, result=[], stop=None, visited=None):
        # 选最长距离
        if not result:
            max_dist = 0
        else:
            max_dist = max([x[1] for x in result])

        other_result = []
        # 如果离分界线的距离小于现有最大距离，或者数据点不够，就从另一半的数根开始寻找
        if (self.left == visited and self.node[0][self.axis] - point[self.axis] < max_dist and self.right is not None) \
                or (len(result) < k and self.left == visited and self.right is not None):
            other_result = self.right.knearest(point, k, dist)
        if (self.right == visited and point[self.axis] - self.node[0][self.axis] < max_dist and self.left is not None) \
                or (len(result) < k and self.right == visited and self.left is not None):
            other_result = self.left.knearest(point, k, dist)

            # 刨出来的点放在一起，选前K个
        result.append(self.node, dist(point, self.node[0]))
        result = sorted(result + other_result, key=lambda pair: pair[1])[:k]

        # 到停点就返回结果
        if self == stop:
            return result
        # 没有就带着现有结果接着往上爬
        else:
            return self.root.k_down_up(point, k, dist, result, stop, self)

    # 输入 特征、类别、k、距离函数
    # 返回这个点属于该类别的概率
    def kNN_prob(self, point, label, k, dist=lambda x, y: sum(map(lambda u, v: (u - v) ** 2, x, y))):
        nearests = self.knearest(point, k, dist)
        return float(len([pair for pair in nearests if pair[0][1] == label])) / float(len(nearests))

    # 输入 特征、k、距离函数
    # 返回该点概率最大的类别以及相对应的概率
    def kNN(self, point, k, dist=lambda x, y: sum(map(lambda u, v: (u - v) ** 2, x, y))):
        nearests = self.knearest(point, k, dist)
        statistics = {}
        for data in nearests:
            label = data[0][1]
            if label not in statistics:
                statistics[label] = 1
            else:
                statistics[label] += 1
        max_label = max(statistics.iteritems(), key=operator.itemgetter(1))[0]
        return max_label, float(statistics[max_label]) / float(len(nearests))
