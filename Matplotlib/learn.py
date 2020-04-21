import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib

zhfont1 = matplotlib.font_manager.FontProperties(fname="D:\\learn Java\\pyday\\2\\SimHei.ttf")

x= np.arange(1,11)
y=2*x+5
plt.title("杰的第一个函数线",fontproperties=zhfont1)

plt.xlabel("x轴",fontproperties=zhfont1)
plt.ylabel("y轴",fontproperties=zhfont1)
plt.plot(x,y,"_b")
plt.show()

# # fname 为 你下载的字体库路径，注意 SimHei.ttf 字体的路径
# zhfont1 = matplotlib.font_manager.FontProperties(fname="D:\\learn Java\\pyday\\2\\SimHei.ttf") 
 
# x = np.arange(1,11) 
# y =  2  * x +  5 
# plt.title("菜鸟教程 - 测试", fontproperties=zhfont1) 
 
# # fontproperties 设置中文显示，fontsize 设置字体大小
# plt.xlabel("x 轴", fontproperties=zhfont1)
# plt.ylabel("y 轴", fontproperties=zhfont1)
# plt.plot(x,y) 
# plt.show()