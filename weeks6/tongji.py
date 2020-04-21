def getNum():
    nums = []
    iNumStr =  input("请输入数字（回车结束）：")
    while iNumStr != '':
        nums.append(eval(iNumStr))
        iNumStr =  input("请输入数字（回车结束）：")

    return nums

def mean(numbers):
    s = 0.0
    for num in numbers:
        s= s + num
    return (s/len(numbers))

def dev(numbers , mean): #计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers) - 1) , 0.5)

def median(numbers): #计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1]+numbers[size//2])/2
    else:
        med = numbers[size//2] 
    return med

n = getNum()
m = mean(n)
print('平均数是：{}  中位数是{}  方差是{} '.format(m,median(n),dev(n,m)))