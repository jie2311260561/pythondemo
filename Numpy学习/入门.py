import numpy as np 

# a = np.arange(15).reshape(3,5)

# print(a)
# print(a.shape) #数组的尺寸
# print(a.ndim) #数组的轴数
# print(a.dtype) #一个对象的类型
# print(a.dtype.name) # 也是类型
# print(a.itemsize) #每个元素的大小 以字节为单位
# print(a.size) # 元素总数

# print(type(a)) #查看当前变量的类型 系统类型
# b = np.array([6,7,8])
# print(b)
# print(type(b))
#a = np.array(1,2,3,4)
# a = np.array([2,3,4]) #必须以一个列表作为参数
# print(a.dtype)   #int32

# b=np.array([(1.5,2,3),(4,5,6)])
# print(b)
# print(b.dtype) #float64

#类型也可以指定
# c= np.array([[1,2],[3,4]],dtype = complex)
# print(c)

#但是其大小是已知的。因此，NumPy提供了几个函数来创建具有初始占位符内容的数组
# 该函数zeros创建一个充满零的数组
# a = np.zeros((3, 4))
# print(a)
# print(a.dtype) # float64 默认情况下

# a = np.zeros((2,3,4),dtype = np.int32) #全是0
# print(a)
# print(a.dtype)

# a = np.empty((2,3))  #内容是随机的 但也有可能是全0
# print(a)
# print(a.dtype)

# print(np.arange(10,30,5))
# print(np.arange(0,2,0.3)) #返回小数序列

# 当arange用浮点参数使用时，它通常是不可能预测得到的元件的数量，由于有限浮点精度。因此，通常最好使用将linspace所需元素数量而不是步骤数量作为参数的函数：
# 返回均匀间隔的数字
# print(np.linspace(0,2,9))
# 然后将一维数组打印为行，将二维打印为矩阵，将三维打印为矩阵列表。

# 如果数组太大而无法打印，NumPy会自动跳过数组的中心部分，仅打印角点：
# print(np.arange(10000))
# 强制打印 
# import sys
# np.set_printoptions(threshold = sys.maxsize) # 更改打印选项
# print(np.arange(10000))

#基本操作
# 数组上的算数运算符一样适用于np
# 可以使用@ 或者dot 方法执行矩阵乘积
# += *= 修改当前数组 而不是创建新数组

# 当使用不同类型的数组进行操作时，结果数组的类型对应于更通用或更精确的数组（这种行为称为向上转换）
# 如'int64'->'float64'

#沿着数组指定操作
# b=np.arange(12).reshape(3,4)
# print(b)
# print(b.sum(axis = 0)) #向下求和 column 逐行求和
# print(b.min(axis = 1)) # row
# print(b.cumsum(axis = -1 )) #row 逐列求和

# NumPy提供熟悉的数学函数，例如sin，cos和exp。在NumPy中，这些被称为“通用函数”（ufunc）。在NumPy中，这些函数在数组上逐元素操作，从而生成数组作为输出。
# all， any， apply_along_axis， argmax， argmin， argsort， average， bincount， ceil， clip， conj， corrcoef， 
# cov， cross， cumprod， cumsum， diff， dot， floor， inner， INV， lexsort， max， maximum， mean， median， min， 
# minimum， nonzero， outer， prod， re， round， sort， std， sum， trace， transpose， var， vdot， vectorize， where

#多维数组也可以切片 索引 循环
# 多维数组每个轴可以有一个索引。这些索引以元组给出，并用逗号分隔：

# def f(x,y):
#     return 10*x+y
# b = np.fromfunction(f,(5,4),dtype = int)
# print(b)
# print(b[2,3])
# print(b[0:5,1])
# #以一个轴进行迭代
# for row in b:
#     print(row)

# # 以元素做迭代
# for element in b.flat:
#     print(element)

# 数组的形状可以使用各种命令来更改。请注意，以下三个命令均返回修改后的数组，但不更改原始数组：
# a = np.floor(10*np.random.random((3,4)))
# print(a)
# print(a.ravel()) #一维
# print(a.reshape(6,2)) #指定维度
# print(a.T) #行列倒置 转职
# a.resize((2,6) ) # 修改数组本身 如果给定参数 -1 会自动计算其他尺寸
# print(a)

# # 数组可以沿着不通的轴叠在一起 
# a = np.floor(10*np.random.random((2,2)))
# b = np.floor(10*np.random.random((2,2)))
# print(a)
# print(b)
# print(np.vstack((a,b)))  # 行上相加
# print(np.hstack((a,b)))  # 列上相加

# 1D数组 折叠到 2D中
# from numpy import newaxis
# # np.column_stack((a,b)) 
# a = np.array([4.,2.])
# b = np.array([3.,8.])
# print(np.column_stack((a,b))) #合成二维
# print(np.hstack((a,b))) #不相同的才会合成
# print(a[:,newaxis] ) #转换成二维
# print(np.column_stack((a[:,newaxis],b[:,newaxis]))) #转换成二维后合成 二维
# print(a)

# 将一个数组拆分为几个较小的数组使用hsplit，
# a  = np.floor(10*np.random((2,12)))
# print(a)
# 完全没有复制
# a = np.arange(12)
# b = a   #参数不会传递 只是指向同一个列表  
# print(id(a))
# print(id(b)) #即id相同
# # 不同的数组对象可以共享相同的数据。该view方法创建一个查看相同数据的新数组对象。
# c = a.view()
# print(id(c))
# # 切片数组将返回其视图
# # s = a[ : , 1:3]
# # print(s[:])
# # 深度复制¶
# # 该copy方法对数组及其数据进行完整复制。
# d=a.copy()
# print(d)
# #一般cpoy 应用于原来的数组不在使用后调用 对其切片做深度拷贝

# palette = np.array( [ [0,0,0],                # black
#                        [255,0,0],              # red
#                        [0,255,0],              # green
#                        [0,0,255],              # blue
#                        [255,255,255] ] )       # white
# image = np.array( [ [ 0, 1, 2, 0 ], 
#                   [ 0, 3, 4, 0 ]  ] )                      
# print(palette[image])

# 我们还可以为多个维度提供索引。每个维度的索引数组必须具有相同的形状。

# 自然，我们可以将i和j放在一个序列中（例如一个列表），然后对该列表进行索引。
# 但是，我们不能通过将i其j放入数组来完成此操作，因为该数组将被解释为索引a的第一个维度。###
# 是否要使用Python的 +=构造，因为它可能无法满足您的期望
# a = np.arange(5)
# print(a)
# a[[0,0,2]]+=1
# print(a) 
# [0 1 2 3 4]
# [1 1 3 3 4]  第0个元素也仅递增一次