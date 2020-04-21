# coding=utf-8

# 创建一个空列表numbers
numbers = []

# str用来存储输入的数字字符串，lst1是将输入的字符串用空格分割，存储为列表
str = input()
lst1 = str.split(' ')

# 将输入的数字字符串转换为整型并赋值给numbers列表
for i in range(len(lst1)):
   numbers.append(int(lst1.pop()))

# 请在此添加代码，对输入的列表中的数值元素进行累加求和
########## Begin ##########
def add(*number):
    for num in range(number):
        d += num


d = add(numbers)
########## End ##########

print(d)








