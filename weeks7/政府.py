'''
政府工作报告词云

生成所需的词云
'''
import jieba
import wordcloud
from scipy.misc import imread

mask = imread('fivestart.png') #北京是白色的五角星图片
f = open('新时代中国特色社会主义.txt','r',encoding= 'utf-8')
t =f.read()
f.close()
ls =jieba.lcut(t)
txt = ' '.join(ls)
#生成词云
#生成
w =wordcloud.wordcloud(font_path ='msyh.ttc',width =1000, height = 700 , background_color = 'write',max_words =15)

w.generate(txt)