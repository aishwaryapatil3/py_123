# draw a square
import turtle

wn = turtle.Screen()
kurzweil = turtle.Turtle()

for i in range(4):
    kurzweil.forward(100)
    kurzweil.left(360/4)

wn.exitonclick()