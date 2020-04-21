import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'
radar_labels = np.array(['研究型(I)','艺术型(A)','社会型(S)','企业型(E)','常规型(C)','现实型(R)'])

date = np.array([[0.40,0.32, 0.35,0.30,0.30,0.88],
                [0.85, 0.35, 0.30, 0.40, 0.40, 0.30],
                [0.43, 0.89, 0.30, 0.28, 0.22, 0.30],
                [0.30, 0.25, 0.48, 0.85, 0.45, 0.40],
                [0.20, 0.38, 0.87, 0.45, 0.32, 0.28],
                [0.34, 0.31, 0.38, 0.40, 0.92, 0.28]])
date_labels = ('艺术家','实验员','工程师','推销员','社会工作者','计时员')
angles = np.linspace(0,2*np.pi,6,endpoint = False)
date = np.concatenate((date,[date[0]]))
angles = np.concatenate((angles,[angles[0]]))
fig = plt.figure(facecolor='write')
plt.subplot(111,polar =True)
plt.plot(angles,date,'o-',linewidth = 1,alpha =0.2)
plt.fill(angles,date,alpha = 0.25)
plt.thetargrids(angles*180/np.pi,radar_labels,frac = 1.2)
plt.figtext(0.52,0.95,'霍兰德人格分析',ha='center',size = 20)
legend = plt.legend(date_labels,loc = (0.94,0.80),labelspacing = 0.1)
plt.setp(legend.get_texts(),fontsize = 'large')
plt.grid(True)
plt.savefig('holland_radar.jpg')
plt.show()