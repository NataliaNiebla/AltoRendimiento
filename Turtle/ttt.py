import turtle
pantalla = turtle.getscreen()
t= turtle.Turtle()
t.speed(6)

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
def circulo(circ_marca):
    coordenadas = {
        "1": [-250,120],
        "2":[0,120],
        "3":[250,120],
        "4":[-250,-90],
        "5":[0,-90],
        "6":[250,-90],
        "7":[-250,-300],
        "8":[0,-300],
        "9": [250,-300]
    }
    
    t.penup()
    t.goto(coordenadas[str(circ_marca)][0],coordenadas[str(circ_marca)][1])
    t.pendown()
    t.circle(90)
    
#EQUIS
def equis(equis_marca):
    coordenadas = {
        "1": [-250,210],
        "2":[0,210],
        "3":[250,210],
        "4":[-250,0],
        "5":[0,0],
        "6":[250,0],
        "7":[-250,-210],
        "8":[0,-210],
        "9": [250,-210]
    }
    
    t.penup()
    t.goto(coordenadas[str(equis_marca)][0]-90,coordenadas[str(equis_marca)][1]+90)
    t.pendown()
    t.goto(coordenadas[str(equis_marca)][0]+90,coordenadas[str(equis_marca)][1]-90)
    t.penup()
    t.goto(coordenadas[str(equis_marca)][0]+90,coordenadas[str(equis_marca)][1]+90)
    t.pendown()
    t.goto(coordenadas[str(equis_marca)][0]-90,coordenadas[str(equis_marca)][1]-90)


dibujar_tablero()
circ_marca=int(input("o: "))
circulo(circ_marca)
equis_marca=int(input("x: "))
equis(equis_marca)

turtle.done()


