# coding=utf8
import matplotlib.pyplot as plt
import numpy as np

index=np.arange(4)
sales_BJ=[52,55,63,46]
sales_SH=[44,66,55,41]

bar_width=0.3

plt.bar(index,sales_BJ,bar_width,color='b')
plt.bar(index,sales_SH,bar_width,color='r',bottom=sales_BJ)
plt.show()