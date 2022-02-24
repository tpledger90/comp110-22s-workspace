from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.speed(1)
leo.color(109, 56, 0)


i: int = 0
while (i < 4):
    leo.goto(0, 325)
    leo.forward(300)
    leo.left(90)
    i = i + 1
done()