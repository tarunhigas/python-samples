import turtle
import math

def spirograph(R=120, r=55, d=65, color="purple"):
    t = turtle.Turtle()
    t.speed(5)  # 1=slowest, 10=fastest
    t.color(color)
    t.hideturtle()
    turtle.bgcolor("white")
    turtle.tracer(1)  # update every step so you can watch it draw

    gcd_val = math.gcd(int(R), int(r))
    steps = 360 * (r // gcd_val)

    t.penup()
    for angle in range(0, steps):
        theta = math.radians(angle)
        x = (R - r) * math.cos(theta) + d * math.cos((R - r) / r * theta)
        y = (R - r) * math.sin(theta) - d * math.sin((R - r) / r * theta)
        t.goto(x, y)
        t.pendown()

    turtle.update()
    turtle.done()

spirograph(R=120, r=55, d=65)
