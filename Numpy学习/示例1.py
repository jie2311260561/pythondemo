#生成布尔索引
import numpy as np 
import matplotlib.pyplot as plt 

# def mandelbrot(h,w,maxit = 20):
#     y,x = np.ogrid[-1.4:1.4:h*1j,-2:0.8:w*1j]
#     c = x*y*1j
#     z = c
#     divtime = maxit + np.zeros(z.shape,dtype = int)

#     for i in range(maxit):
#         z= z**2 + c
#         diverge = z*np.conj(z) > 2**2
#         div_now = diverge & (divtime == maxit)
#         divtime[div_now] = i
#         z[diverge] = 2

#     return divtime
# def mandelbrot( h,w, maxit=20 ):
#     """Returns an image of the Mandelbrot fractal of size (h,w)."""
#     y,x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
#     c = x+y*1j
#     z = c
#     divtime = maxit + np.zeros(z.shape, dtype=int)

#     for i in range(maxit):
#         z = z**2 + c
#         diverge = z*np.conj(z) > 2**2            # who is diverging
#         div_now = diverge & (divtime==maxit)  # who is diverging now
#         divtime[div_now] = i                  # note when
#         z[diverge] = 2                        # avoid diverging too much

#     return divtime
# plt.imshow(mandelbrot(400,400))
# plt.show()



#布尔索引数组切片
# a = np.arange(12).reshape(3,4)
# print(a)

# b1 =np.array([False,True,True])

# b2 = np.array([True,False,True,False])

# print(a[b1,:])
# print(a[:,b2])



# # 该ix_函数可用于组合不同的向量，以便获得每个n片段的结果
# a = np.array([2,3,4,5])
# b = np.array([8,5,4])
# c = np.array([5,4,6,8,3])
# ax,bx,cx = np.ix_(a,b,c) ########多余
# result = ax+bx*cx
# print(result)
# print(result[3,2,4])
# print(a[3]+b[2]*c[4])
# #使用广播规则 避免创建一个数组
# def ufunc_reduce(ufct, *vectors):
#     vs = np.ix_(*vectors)
#     r = ufct.identity
#     for v in vs:
#        r = ufct(r,v)
#     return r
# print(ufunc_reduce(np.add,a,b,c))



# 自动整形  数组的尺寸
# a = np.arange(30)
# a.shape = 2,-1,3# -1 means "whatever is needed"
# print(a.shape)

# print(a)



# 向量堆叠
# column_stack，dstack，hstack和vstack，视维在堆叠是必须要做
# x = np.arange(0,10,2)
# y = np.arange(5)

# m =np.vstack([x,y])

# print(m)



# histogram应用于数组的NumPy 函数返回一对向量：数组的直方图和bin的向量。当心： matplotlib还具有建立直方图的功能（
# hist在Matlab中称为），该功能不同于NumPy中的直方图。主要区别是pylab.hist自动绘制直方图，而 numpy.histogram仅生成数据。
import matplotlib.pyplot as plt
mu,sigma = 2,0.5
v = np.random.normal(mu,sigma,10000)

# plt.hist(v,bins=50,density=1)
# plt.show()
# Compute the histogram with numpy and then plot it
(n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
plt.plot(.5*(bins[1:]+bins[:-1]), n)
plt.show()