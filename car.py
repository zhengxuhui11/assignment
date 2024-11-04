import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Car Drawing")

t = turtle.Turtle()
t.speed(2)


t.penup()
t.goto(-100, -50)
t.pendown()


t.color("blue")
t.begin_fill()
t.forward(200)    
t.left(90)
t.forward(50)     
t.left(90)
t.forward(200)    
t.left(90)
t.forward(50)     
t.end_fill()


t.penup()
t.goto(-80, 0)
t.pendown()
t.color("red")
t.begin_fill()
t.setheading(45)
t.forward(70.71)
t.setheading(0)
t.forward(80)
t.setheading(-45)
t.forward(70.71)
t.setheading(180)
t.forward(140)
t.end_fill()

t.penup()
t.goto(-50, -50)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(20)      
t.end_fill()

t.penup()
t.goto(50, -50)
t.pendown()
t.begin_fill()
t.circle(20)      
t.end_fill()

t.hideturtle()
turtle.done()