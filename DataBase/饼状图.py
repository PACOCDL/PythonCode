# coding=utf8
import matplotlib.pyplot as plt
import numpy as np

lables = 'a', 'b', 'c', 'd'
fracs = [15, 30, 45, 10]

explod=[0.1,0.1,0.2,0.08]

plt.axes(aspect=1)
plt.pie(x=fracs,labels=lables,autopct='%.0f%%',explode=explod,shadow=True)
plt.show()