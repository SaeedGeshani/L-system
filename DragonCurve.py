import turtle

def dragon_curve(t, iterations, length, sign):
    if iterations == 0:
        t.forward(length)
    else:
        t.left(45 * sign)
        dragon_curve(t, iterations - 1, length / (2**0.5), 1)
        t.right(90 * sign)
        dragon_curve(t, iterations - 1, length / (2**0.5), -1)
        t.left(45 * sign)

def main():
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    dragon_curve(t, 10, 200, 1)
    turtle.done()

main()