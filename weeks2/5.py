#字符串编程

#字符串有几种表示方式 

'''
形成的就是字符串，没有变量就可以当作字符串来使用
索引和切片 [M:N]M开头 N结尾
            [M:N:K] 根据步长K切片 倒叙步长-1
            转义字符\反斜杠之后的字符被当作真正的字符来使用
            \b回退  \n 换行  \r回车

    字符串操作符 1、 +  2、 *  3、 in 子串  
    eval 字符串相加 
    函数字符串处理函数： len(x)  str(x)-->增加一个引号

    hex(x)         方法
    chr(u)  ord(x)获取   python 使用 Unicode  
'''
# for  i in range(12):
#     print(chr(9800+i))
'''
    str.lower() 返回字符串的副本（全部大写or小写）
    str.upper()

    str.split(sep = None)  返回一个列表 有 sep 分割的列表
    str.count(sub) 返回字符出现的次数
    str.replace(ole,new) old替换成new
    str.center(width,[······]) 扩充宽度 由 中间的填充
    str.strip(chars)  去掉左右的 列出的字符
    str.join(iter) 给除最后一个元素后 增加一个  增加 分割字符串
    
'''