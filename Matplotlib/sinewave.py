# title   subplot 用法


import numpy as np 
import matplotlib.pyplot as plt 
#计算正弦波的x y 的坐标
x=np.arange(0,3*np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)
#建立一个subplot网络 高位2 宽为1
plt.subplot(2,1,1)
#绘制第一个图像
plt.plot(x,y_sin)
plt.title('sine wave ')
#使用matplolib来绘制点
#绘制第二个图像
plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('cosine wave')

plt.show()
