import numpy as np

x=np.loadtxt('G:\\PythonCode\\DataBase\\000001.csv',delimiter=',',skiprows=1,usecols=(2,3),unpack=False)
# print(x)
c=np.arange(11)
print(c)
print(c[-1])
print(c[5:])
print(c[::2])

c=np.random.randint(1,100,10)
print(c)

print(np.min(c))

print(c.min())
print(np.sort(c))