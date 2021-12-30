import turtle

# full screen 
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0)

# background color
screen.bgcolor("black")

def crcks(postionX,PstionY,color,type):
    c = turtle.Turtle()
    c.goto(postionX,PstionY)
    c.speed(0)

    for x in range(12):
        c.color(color)
        c.width(5)
        c.penup()
        c.forward(5)
        c.pendown()
        for i in range(13):
            
            c.forward(i-i+1)
            c.penup()
            c.backward(i+20+type)
            c.pendown()
            c.left(30)
        c.hideturtle()


def stars(postionX,PstionY,color,size):
    star = turtle.Turtle()
    star.goto(postionX,PstionY)
    star.speed(0)
    star.pendown()
    star.width(3)
    # fire work head
    star.color(color)
    star.fillcolor(color)
    star.begin_fill()
    for i in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()
    star.penup()
    star.hideturtle()



def friework(postionX,PstionY,color,rotation):
    b = turtle.Turtle()
    b.goto(postionX,PstionY)
    b.speed(0)
    b.pendown()
    b.width(2)
    # fire work head
    b.color('white')
    b.fillcolor(color)
    b.begin_fill()
    b.setheading(0)
    b.left(30)          #chagene 60
    b.forward(50)
    b.right(60+60)
    b.forward(50)
    b.setheading(170)   #change 200
    b.circle(-68,43)
    b.end_fill()
    # fier work body
    b.penup()
    b.backward(10)
    b.setheading(0)
    b.setheading(240)     #change 270
    b.pendown()
    b.forward(100)
    b.setheading(330)         #change 0 360-30
    b.forward(32)
    b.left(90)
    b.forward(100)
    b.backward(5)
    b.color(color)
    b.fillcolor(color)
    b.begin_fill()
    b.setheading(190)    #change 220
    b.circle(-65,30)
    b.setheading(240)   #change 220
    b.forward(15)
    b.setheading(340)  #change 10
    b.circle(65,30)
    b.setheading(60)  #change 90
    b.end_fill()
    b.forward(15)

    b.backward(30)
    b.color(color)
    b.fillcolor(color)
    b.begin_fill()
    b.setheading(190)    #change 220
    b.circle(-65,30)
    b.setheading(240)   #change 220
    b.forward(15)
    b.setheading(340)  #change 10
    b.circle(65,30)
    b.setheading(60)  #change 90
    b.end_fill()
    b.forward(15)

    b.backward(30)
    b.color(color)
    b.fillcolor(color)
    b.begin_fill()
    b.setheading(190)    #change 220
    b.circle(-65,30)
    b.setheading(240)   #change 220
    b.forward(15)
    b.setheading(340)  #change 10
    b.circle(65,30)
    b.setheading(60)  #change 90
    b.end_fill()
    b.forward(15)

    b.color('white')
    b.forward(15+15+30)
    b.backward(95)
    b.setheading(150) 
    b.forward(12)
    b.setheading(240)
    b.forward(300)
    b.setheading(150)
    b.forward(8)
    b.right(90)
    b.forward(300)
    b.penup()
    b.hideturtle()

stars(-700,-200,'blue',10)
stars(-700,-130,'red',10)
stars(-630,-140,'blue',10)

friework(-650,-200,'blue',20)
friework(-540,-240,'green',20)
friework(-570,-180,'red',20)

crcks(-250,250,"#E5E4E2",15)#withe
crcks(350,260,'#FF6700',15) #red F70D1A
crcks(50,300,"#8EEBEC",15)#bule 52D017

def fier(postionX,PstionY,speed):
    value=False
    a = turtle.Turtle()
    for x in range(12):
            a.goto(postionX,PstionY)
            a.speed(speed)
            a.width(3)

            if value:
                a.color('red')
                a.penup()
                a.forward(10)
                a.pendown()
                a.forward(70)
                a.right(30)
                value=False
            else:
                a.color('blue')
                a.penup()
                a.forward(10)
                a.pendown()
                a.forward(50)
                a.right(30)
                value=True
    a.hideturtle()


# fier(0,0,0)
# fier(-400, 200,0)
# fier(500, 200,0)


happy=turtle.Turtle()
date=turtle.Turtle()


# pen color
happy.color("white")
happy.width(3)
happy.speed(10)

# -------------H 
# H postion set 
happy.hideturtle()           #make the turtle invisible
happy.penup()                #don't draw when turtle moves
happy.goto(-400, 200)       #move the turtle to a location
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
happy.goto(-310, 0)       #move the turtle to a location
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

happy.penup()        
happy.backward(100)
happy.right(90)
happy.forward(100)
happy.right(90)
happy.forward(10)
happy.left(90)
happy.pendown()
happy.fillcolor('black')
happy.begin_fill()
happy.setheading(60)  
happy.circle(20,steps=3)
happy.end_fill()

happy.penup()        #don't draw when turtle moves
happy.setheading(180)
happy.goto(-70,0)
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


# ##------------P


# #-----------P
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
#Y

#pen home postion set
happy.penup()        #don't draw when turtle moves
happy.setheading(0)
happy.goto(0,0)
happy.pendown()      #draw when the turtle moves
##pen home postion set


# ------------------------------------------ new year ---------------------------------------------

happy.color("white")
happy.width(15)


#pen home postion set
happy.penup()        #don't draw when turtle moves
happy.setheading(0)
happy.goto(-400,-250)
happy.showturtle()           #make the turtle visible
happy.pendown()      #draw when the turtle moves
##pen home postion set

#N
happy.left(90)
happy.forward(50)
happy.setheading(315)
happy.forward(70)
happy.setheading(90)
happy.forward(50)
happy.backward(50)

happy.penup()
happy.setheading(0)
happy.forward(50)
happy.pendown()

#E
happy.color("red")
happy.forward(50)
happy.backward(50)
happy.left(90)
happy.forward(25)
happy.right(90)
happy.forward(25)
happy.backward(25)
happy.left(90)
happy.forward(25)
happy.right(90)
happy.forward(50)
happy.backward(50)
happy.right(90)
happy.forward(50)
happy.left(90)
happy.forward(50)

happy.penup()
happy.setheading(0)
happy.forward(50)
happy.pendown()

#W
happy.color("blue")
happy.left(90)
happy.forward(50)
happy.backward(50)
happy.right(45)
happy.forward(35)
happy.right(90)
happy.forward(35)
happy.setheading(0)
happy.left(90)
happy.forward(50)
happy.backward(50)

happy.penup()
happy.setheading(0)
happy.forward(100+25)
happy.pendown()

#Y
happy.color("red")
happy.left(90)
happy.forward(25)
happy.left(135)
happy.setheading(0)
happy.setheading(45)
happy.forward(35)
happy.backward(35)
happy.setheading(0)
happy.setheading(135)
happy.forward(35)
happy.backward(35)
happy.setheading(0)
happy.right(90)
happy.forward(25)

happy.penup()
happy.setheading(0)
happy.forward(50+10)
happy.pendown()

#E
happy.color("Gold")
happy.forward(50)
happy.backward(50)
happy.left(90)
happy.forward(25)
happy.right(90)
happy.forward(25)
happy.backward(25)
happy.left(90)
happy.forward(25)
happy.right(90)
happy.forward(50)
happy.backward(50)
happy.right(90)
happy.forward(50)
happy.left(90)
happy.forward(50)

happy.penup()
happy.setheading(0)
happy.forward(40)
happy.pendown()

#A
happy.color("green")
happy.setheading(60)
happy.forward(60)
happy.setheading(0)
happy.setheading(60+60+60+60+60)
happy.forward(60)
happy.backward(30)
happy.setheading(180)
happy.forward(33)
happy.backward(33)
happy.setheading(0)
happy.setheading(60+60+60+60+60)
happy.forward(33)
happy.setheading(0)

happy.penup()
happy.setheading(0)
happy.forward(40)
happy.pendown()


#R
happy.color("red")
happy.setheading(90)
happy.forward(50)
happy.right(90)
happy.forward(37.5)
happy.circle(-12.5,180)
happy.forward(37.5)
happy.setheading(0)
happy.right(35)
happy.forward(50)




# 2022

#pen home postion set
date.penup()        #don't draw when turtle moves
date.setheading(0)
date.goto(-200,-125)
date.showturtle()           #make the turtle visible
date.pendown()      #draw when the turtle moves
##pen home postion set
date.color("white")
date.width(25)

#2
date.color("yellow")
date.forward(50)
date.backward(50)
date.left(40)
date.forward(60)
date.circle(20,145)
date.forward(10)
date.circle(20,90)

date.penup()        #don't draw when turtle moves
date.setheading(0)
date.goto(-200,-125)
date.forward(50+40+25) #2 one is letter sape
date.showturtle()           #make the turtle visible
date.pendown()      #draw when the turtle moves


# 0
date.circle(25,90)
date.forward(25)
date.circle(25,180)
date.forward(25)
date.circle(25,90)


date.penup()        #don't draw when turtle moves
date.setheading(0)
date.forward(40+25) #2 one is letter sape
date.showturtle()           #make the turtle visible
date.pendown()      #draw when the turtle moves

#2
date.color("yellow")
date.forward(50)
date.backward(50)
date.left(40)
date.forward(60)
date.circle(20,145)
date.forward(10)
date.circle(20,90)

date.penup()        #don't draw when turtle moves
date.setheading(0)
date.goto(70,-125)
date.showturtle()           #make the turtle visible
date.pendown()      #draw when the turtle moves

#2
date.color("yellow")
date.forward(50)
date.backward(50)
date.left(40)
date.forward(60)
date.circle(20,145)
date.forward(10)
date.circle(20,90)

date.penup()        #don't draw when turtle moves
date.setheading(0)
date.forward(50+20+25) #2 one is letter sape
date.showturtle()           #make the turtle visible
date.pendown()      #draw when the turtle moves


date.hideturtle()

turtle.done()