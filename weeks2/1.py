import turtle
#from turtle import* 这样就不用turtle.
#import turtle as 别名  给库起个别名
turtle.colormode(0);
turtle.setup(650,350) #设置窗体的大小和位置，不指定位置，默认在正中心
turtle.penup() #起飞   pu
turtle.fd(-250) # 向前行进 走直线
turtle.pendown() #降落 pd
turtle.pensize(25) # 宽度 width
turtle.pencolor("purple")
turtle.seth(-40)   #改变行进方向 绝对度数 setheading
for i in range(4):
    turtle.circle(40,80) #根据半径r 绘制弧度 
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()