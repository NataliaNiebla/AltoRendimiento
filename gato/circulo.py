import turtle

class TicTacToeCircle:
    def _init_(self, size):
        self.size = size // 3  # Tamaño ajustado al tamaño del tablero
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()

    def draw_circle(self, x, y):
        self.turtle.penup()
        self.turtle.goto(x, y - self.size // 2)
        self.turtle.pendown()
        self.turtle.circle(self.size // 2)
        
    def display(self):
        screen = turtle.Screen()
        screen.mainloop()

# Ejemplo de uso
if __name__ == "_main_":
    circle = TicTacToeCircle(300)
    circle.draw_circle(0, 0)
    circle.display()