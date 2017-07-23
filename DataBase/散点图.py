#coding=utf8
import matplotlib.pyplot as plt
import numpy as np
N=1000
x=np.random.randn(N)

# y=np.random.randn(N)
y=-x+np.random.randn(N)*0.5
plt.scatter(x,y)
plt.show()