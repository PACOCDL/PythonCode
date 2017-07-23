#coding=utf8
import matplotlib.pyplot as plt
import numpy as np

N=5
y=[20,10,30,25,14]
index=np.arange(N)
# p1=plt.bar(left=index,height=y,color='red',width=0.6)
pl=plt.barh(left=0,bottom=index,width=y)
plt.show()