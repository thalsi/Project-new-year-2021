import turtle

# full screen 
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

# background color
screen.bgcolor("black")

happy=turtle.Turtle()
# pen color
happy.color("white")
happy.width(3)


# H 
# H postion set 
happy.hideturtle()           #make the turtle invisible
happy.penup()                #don't draw when turtle moves
happy.goto(-600, 100)       #move the turtle to a location
happy.showturtle()           #make the turtle visible
happy.pendown()              #draw when the turtle moves
happy.goto(-550, 100)  
## H postion set 

happy.heading()  
happy.right(90)  
happy.heading()  
happy.forward(100)
## H

turtle.done()
