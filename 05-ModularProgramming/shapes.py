#05.09, 05.12

def drawSquare(x,y,n):
    import turtle
       
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
        
    for x in range(5):
        turtle.forward(n)
        turtle.right(90)
    turtle.setheading(0)
    
    
def drawCircle(x, y, r):
    import turtle
    
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    
    turtle.circle(r)
    

def drawTriangle(x, y, m):
    import turtle
    
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    
    for x in range(3):
        turtle.forward(m)
        turtle.right(120)
 
 
def drawStar():
    import turtle
    
    for x in range(5):
        turtle.forward(100)
        turtle.right(144)
        turtle.forward(100)
        turtle.left(72)
        
        
def drawBlackSquare(x, y, m):
    import turtle
       
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    
    turtle.fillcolor('black')
    turtle.begin_fill()
    for x in range(4):
        turtle.forward(m)
        turtle.right(90)
    turtle.end_fill()
     