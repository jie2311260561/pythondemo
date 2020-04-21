'''
分形几何中  
    科赫雪花 
'''
import turtle
def koch(size,n):
    if n == 0 :
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)

def main():
    turtle.setup(800,400)
    turtle.penup()
    turtle.goto(-300,100)
    turtle.pendown()
    turtle.pensize(4)
    turtle.pencolor("blue")
    lever = 3
    koch(400,lever)
    turtle.right(120)
    koch(400,lever)
    turtle.right(120)
    koch(400,lever)
    turtle.hideturtle()
    turtle.done()
main()
