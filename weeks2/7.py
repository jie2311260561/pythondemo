import time
#strftime 设计输出格式
# #time()
# ctime  获取格式化和处理时间的方法
# gmtime


timeStr='2018-01-26 12:55:20'
time.strptime(timeStr) #使用一个字符串形成特定的时间

t=time.gmtime() # 时间格式化 
print(time.strftime("%Y-%m-%d %H:%M:%S",t))