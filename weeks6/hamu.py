def getText():
    txt = open("ku.txt","r",encoding='utf-8',errors='ignore').read()
    # txt = txt.lower() #将所有的英文字符变成小写
    # for ch 
    return txt
def calcu_sub_str_num(mom_str,sun_str):
    count = 0                                  #定义计数器初始值
    for i in range(len(mom_str)-1): #因为i的下标从0开始，所以len（mom_str）-1
        if mom_str[i:i+len(sun_str)] == sun_str:
            count+=1
    return count

num = calcu_sub_str_num(getText(),'可视化')
print(getText())
print(getText().count("u003Cp",0,len(getText())))

print("{}".format(num))
# print("\")