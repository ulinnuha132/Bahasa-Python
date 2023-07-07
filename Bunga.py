import turtle

t = turtle.Turtle()
s = turtle.Screen()

s.bgcolor('black')
t.pencolor('white')
t.speed(100)
col = ('yellow', 'green', 'red', 'blue')

for n in range(10):
    for x in range(8):
        t.speed(x+10)
        for i in range(2):
            t.pensize(2)
            t.circle(80+n*20, 90)
            t.lt(90)
        t.lt(45)
    t.pencolor(col[n%4])
s.exitonclick()