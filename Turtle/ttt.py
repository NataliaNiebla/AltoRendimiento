import turtle
pantalla = turtle.getscreen()
t= turtle.Turtle()
t.speed(3)

def dibujar_tablero():
    t.penup() #sube
    t.goto(360,100) #mueve a 2
    t.right(180) #giro
    t.pendown() #baja
    t.forward(720) #marca
    
    t.penup()
    t.goto(360,-100) #mueve a 2
    t.pendown() #baja
    t.forward(720) #marca
    
    t.penup()
    t.goto(120,-300)
    t.right(90)
    t.pendown() #baja
    t.forward(600) #marca
    
    t.penup()
    t.goto(-120,-300)
    t.pendown() #baja
    t.forward(600) #marca
    
#CIRCULOS
def circulo_1():
    t.penup()
    t.home()
    t.goto(-250,120)
    t.pendown()
    t.circle(90)

def circulo_2():
    t.penup()
    t.home()
    t.goto(0,120)
    t.pendown()
    t.circle(90)
    
def circulo_3():
    t.penup()
    t.home()
    t.goto(250,120)
    t.pendown()
    t.circle(90)
    
def circulo_4():
    t.penup()
    t.home()
    t.goto(-250,-90)
    t.pendown()
    t.circle(90)
    
def circulo_5():
    t.penup()
    t.home()
    t.goto(0,-90)
    t.pendown()
    t.circle(90)
    
def circulo_6():
    t.penup()
    t.home()
    t.goto(250,-90)
    t.pendown()
    t.circle(90)
    
def circulo_7():
    t.penup()
    t.home()
    t.goto(-250,-300)
    t.pendown()
    t.circle(90)

def circulo_8():
    t.penup()
    t.home()
    t.goto(0,-300)
    t.pendown()
    t.circle(90)
    
def circulo_9():
    t.penup()
    t.home()
    t.goto(250,-300)
    t.pendown()
    t.circle(90)
    
dibujar_tablero()
"""
circulo_1()
circulo_2()
circulo_4()
circulo_5()
circulo_8()
circulo_3()
circulo_6()
circulo_9()
circulo_7()
"""

turtle.done()


