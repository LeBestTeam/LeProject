import turtle
import math

class ArchimedeanSpiral:
    def __init__(self, a: float, b: float, turns: int):
        self.a = a
        self.b = b
        self.turns = turns

    def draw(self):
        turtle.speed(0)
        turtle.bgcolor("white")
        turtle.pencolor("blue")

        # Зберігаємо всі точки спіралі
        points = []
        for i in range(self.turns * 360):
            angle = math.radians(i * 0.1)
            x = (self.a + self.b * angle) * math.cos(angle)
            y = (self.a + self.b * angle) * math.sin(angle)
            points.append((x, y))

        # Переміщаємося до початкової точки без малювання
        turtle.penup()
        turtle.goto(points[0])
        turtle.pendown()

        # Малюємо спіраль
        for point in points:
            turtle.goto(point)

        turtle.done()

class App:
    def __init__(self):
        self.curves_class = {
            "ArchimedeanSpiral": ArchimedeanSpiral,
        }

    def create(self, name, *args, **kwargs):
        if name in self.curves_class:
            self.curves_class[name](*args).draw()
        else:
            raise ValueError("Wrong curve name")

app = App()

# Example of creating and drawing an Archimedean Spiral:
app.create("ArchimedeanSpiral", 0.1, 0.1, 10)
