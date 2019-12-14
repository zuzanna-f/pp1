def drawSquare(x,y,n):
    import turtle
       
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
        
    for x in range(5):
        turtle.forward(n)
        turtle.right(90)
    turtle.setheading(0)
        
    
  
drawSquare(0, 0, 50)
drawSquare(50, 0, 50)
drawSquare(100, 0, 50)
drawSquare(150, 0, 50)
            
drawSquare(0, 50, 50)
drawSquare(50, 50, 50)
drawSquare(100, 50, 50)
drawSquare(150, 50, 50)

drawSquare(0, 100, 50)
drawSquare(50, 100, 50)
drawSquare(100, 100, 50)
drawSquare(150, 100, 50)

drawSquare(0, 150, 50)
drawSquare(50, 150, 50)
drawSquare(100, 150, 50)
drawSquare(150, 150, 50)