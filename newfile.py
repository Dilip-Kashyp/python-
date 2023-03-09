import turtle
turtle.Screen().bgcolor('gray')
t=turtle.Turtle()
t.speed(0)
t.hideturtle()

for i in range(1200):
    t.color('pink')
    t.circle(i)
    t.color('yellow')
    t.circle(i*0.8)
    t.right(3)
    t.forward(3)
