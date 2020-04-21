import random

#random.seed(10) #初始化的种子 不调用使用时间作为种子

#随机数的产生与种子有关


print(random.random())

print(random.randint(10,100))

print(random.randrange(10,100,10))
a=random.choice([1,2,3,4,5,6,7,8])
print(a)
s=[1,2,3,4,5,6,8,9]
random.shuffle(s)
print(s)