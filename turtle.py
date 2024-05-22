import turtle

class TicTacToeBoard:
    def _init_(self, size=200):
        self.size = size
        self.turtle = turtle.Turtle()

    def draw_board(self):
        self.turtle.penup()
        self.turtle.goto(-self.size // 2, self.size // 6)
        self.turtle.pendown()
        self.turtle.forward(self.size)
        
        self.turtle.penup()
        self.turtle.goto(-self.size // 2, -self.size // 6)
        self.turtle.pendown()
        self.turtle.forward(self.size)
        
        self.turtle.penup()
        self.turtle.goto(-self.size // 6, self.size // 2)
        self.turtle.right(90)
        self.turtle.pendown()
        self.turtle.forward(self.size)
        
        self.turtle.penup()
        self.turtle.goto(self.size // 6, self.size // 2)
        self.turtle.pendown()
        self.turtle.forward(self.size)

    def display(self):
        screen = turtle.Screen()
        self.draw_board()
        screen.mainloop()

# Uso de la clase para dibujar el tablero de gato
board = TicTacToeBoard(300)
board.display()