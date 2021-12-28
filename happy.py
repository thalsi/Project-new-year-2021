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



# -------------H 
# H postion set 
happy.hideturtle()           #make the turtle invisible
happy.penup()                #don't draw when turtle moves
happy.goto(-400, 100)       #move the turtle to a location
happy.showturtle()           #make the turtle visible
happy.pendown()              #draw when the turtle moves
## H postion set 
# fill color
happy.fillcolor("red")
happy.begin_fill()

happy.forward(50)
happy.right(90)  
happy.forward(200)
happy.right(90)
happy.forward(50)
happy.right(90)
happy.forward(74)
happy.left(90)
happy.forward(50)
happy.left(90)
happy.forward(75)
happy.right(90)
happy.forward(50)
happy.right(90)
happy.forward(200)
happy.right(90)
happy.forward(50)
happy.right(90)
happy.forward(75)
happy.left(90)
happy.forward(50)
happy.left(90)
happy.forward(75)

##red color end
happy.end_fill()

happy.right(90)
happy.forward(50)
happy.right(90)  
happy.forward(200)
## --------H

# fill color
happy.fillcolor("red")
happy.begin_fill()
# --------------A 
# A postion set 
happy.hideturtle()           #make the turtle invisible
happy.penup()                #don't draw when turtle moves
happy.goto(-310, -100)       #move the turtle to a location
happy.showturtle()           #make the turtle visible
happy.pendown()              #draw when the turtle moves
## A postion set 

happy.right(200)
happy.forward(215)
happy.right(70)
happy.forward(50)
happy.right(70)
happy.forward(215)
happy.left(250)
happy.forward(50)
happy.right(65)
happy.forward(50)
happy.left(65)
happy.forward(50)
happy.left(65)
happy.forward(50)
happy.right(65)
happy.forward(51)
##red color end
happy.end_fill()

happy.penup()        #don't draw when turtle moves
happy.backward(230)
happy.pendown()      #draw when the turtle moves
##-----------------A 

#-----------P
happy.fillcolor("red")
happy.begin_fill()

happy.right(90)
happy.forward(200)
happy.right(90)
happy.forward(100)
happy.circle(-60,180)
happy.forward(50)
happy.left(90)
happy.forward(84)
happy.right(90)
happy.forward(50)
happy.end_fill()
happy.backward(50)
happy.right(90)
happy.forward(84)

happy.penup()        #don't draw when turtle moves
happy.forward(35)
happy.pendown()      #draw when the turtle moves

happy.fillcolor("black")
happy.begin_fill()

happy.forward(45)
happy.right(90)
happy.forward(50)
happy.circle(-22,180)
happy.forward(50)
happy.end_fill()

happy.penup()        #don't draw when turtle moves
happy.left(90)
happy.forward(35+84)
happy.right(90)
happy.backward(150)
happy.pendown()      #draw when the turtle moves


##------------P


#-----------P
happy.fillcolor("red")
happy.begin_fill()

happy.right(90)
happy.forward(200)
happy.right(90)
happy.forward(100)
happy.circle(-60,180)
happy.forward(50)
happy.left(90)
happy.forward(84)
happy.right(90)
happy.forward(50)
happy.end_fill()
happy.backward(50)
happy.right(90)
happy.forward(84)

happy.penup()        #don't draw when turtle moves
happy.forward(35)
happy.pendown()      #draw when the turtle moves

happy.fillcolor("black")
happy.begin_fill()

happy.forward(45)
happy.right(90)
happy.forward(50)
happy.circle(-22,180)
happy.forward(50)
happy.end_fill()

happy.penup()        #don't draw when turtle moves
happy.left(90)
happy.forward(35+84)
happy.right(90)
happy.backward(180)
happy.pendown()      #draw when the turtle moves


##------------P
happy.fillcolor("red")
happy.begin_fill()
#Y
happy.right(90)
happy.forward(84)
happy.left(35)
happy.forward(150)
happy.right(125)
happy.forward(55)
happy.right(52)
happy.forward(100)
happy.left(110)
happy.forward(100)
happy.right(58)
happy.forward(55)
happy.right(120)
happy.forward(150)
happy.left(30)
happy.forward(84)
happy.right(90)
happy.forward(60)
happy.end_fill()
##Y

turtle.done()
