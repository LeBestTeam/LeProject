import turtle
import math
class DragonCurve:
    def __init__(self, order: int, length: float):
        self.order = order
        self.length = length

    def draw_dragon(self, order, length, angle=90):
        if order == 0:
            turtle.forward(length)
        else:
            length /= math.sqrt(2)
            self.draw_dragon(order-1, length, angle)
            turtle.right(angle)
            self.draw_dragon(order-1, length, -angle)

    def draw(self):
        turtle.speed(0)
        turtle.bgcolor("white")
        turtle.pencolor("blue")

        # Починаємо малювання з центру
        turtle.penup()
        turtle.goto(-self.length / 2, 0)
        turtle.pendown()

        self.draw_dragon(self.order, self.length)

        turtle.done()

class App:
    def __init__(self):
        self.curves_class = {
            
            "DragonCurve": DragonCurve,
        }

    def create(self, name, *args, **kwargs):
        if name in self.curves_class:
            self.curves_class[name](*args).draw()
        else:
            raise ValueError("Wrong curve name")

app = App()

# Example of creating and drawing a Dragon Curve:
app.create("DragonCurve", 10, 200)
