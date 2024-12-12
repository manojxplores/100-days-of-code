import random
import turtle as t
colors_list = [(253, 251, 247), (253, 248, 252), (235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49)]

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()

y = -200
for dot_count in range(10):
    tim.setpos(-200, y)
    for j in range(10):
        tim.dot(20, random.choice(colors_list))
        tim.forward(50)
    y += 50

screen = t.Screen()
screen.exitonclick()
