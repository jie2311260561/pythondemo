#map eval 函数将每个元素都去掉

ls = [[],[],[]]
f = open(fname,'w')
for item in ls:
    f.write(','.join(item)+'\n')
    f.close()