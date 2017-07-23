# coding=utf8
import numpy as np


class Perceptron(object):
    """
        eta:学习率
        n_iter 权重向量的训练次数
        w_:神经元的权重向量
        errors_: 用于记录错误次数
    """

    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
        pass

    """
       输入训练数据，培训神经元，x输入向量样本，y对应样本分类
       x:shape[n_samples，n_features]
    """

    def fit(self, x, y):
        self.w_ = np.zero(1 + x.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(x, y):
                update = self.eta * (target - self.predict(xi))

                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
                self.errors_.append(errors)
                pass
        pass

    def net_input(self, x):
        return np.dot(x.self.w_[1:]) + self.w_[0]
        pass

    def predict(self, x):
        return np.where(self.net_input(x) >= 0.0, 1, -1)

        pass


file = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

import pandas as pd

df = pd.read_csv(file, header=None)
df.head(10)

import matplotlib.pyplot as plt
import numpy as np

y = df.loc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)

x = df.iloc[0:100, [0, 2]].values
print x

plt.scatter(x[:50, 0], x[:50, 1], color='red', marker='o', lable='setosa')
plt.scatter(x[50:100, 0], x[50:100, 1], color='blue', marker='x', lable='versicolor')
plt.xlabel("花瓣的长度")
plt.ylabel("花径的长度")
plt.legend(loc='upper left')
plt.show()

from matplotlib.colors import ListedColormap


def plot_decision_regions(x, y, classifier, resolution='0.02'):
    marker = ('s', 'x', 'o', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    x1_min, x1_max = x[:, 0].min() - 1, x[:, 0].max()
    x2_min, x2_max = x[:, 1].min() - 1, x[:, 1].max()
