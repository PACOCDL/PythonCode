# coding=utf8
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

x = np.linspace(-10, 10, 100)
y = x**2
plt.plot(x, y)
plt.show()