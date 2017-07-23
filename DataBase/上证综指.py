# coding=utf8
import matplotlib.pyplot as plt
import numpy as np

open,close=np.loadtxt('G:\\PythonCode\\DataBase\\000001.csv',delimiter=',',skiprows=1,usecols=(1,4),unpack=True)
change=close-open
print(change)
yesterday=change[:-1]
today=change[1:]
plt.scatter(yesterday,today,10,'r','<',alpha=0.5)
plt.show()