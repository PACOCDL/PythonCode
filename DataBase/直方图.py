# coding=utf8
import matplotlib.pyplot as plt
import numpy as np

# mu=100
# sigma=20
# x=mu+sigma*np.random.randn(2000)

# plt.hist(x,bins=100,color='red',normed=False)
# plt.show()
x=np.random.randn(1000)+2
y=np.random.randn(1000)+3

plt.hist2d(x,y,bins=50)
plt.show()
