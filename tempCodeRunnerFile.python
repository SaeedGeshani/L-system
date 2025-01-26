import turtle

def koch_curve(t, iterations, length):
    if iterations == 0:
        t.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, iterations - 1, length / 3)
            t.left(angle)

def main():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-150, 90)
    t.pendown()
    for i in range(3):
        koch_curve(t, 4, 300)
        t.right(120)
    turtle.done()

main()