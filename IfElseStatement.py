import turtle

prasad_turtle = turtle.Turtle()
def square():

    prasad_turtle.forward(50)
    prasad_turtle.right(90)
    prasad_turtle.forward(50)
    prasad_turtle.right(90)
    prasad_turtle.forward(50)
    prasad_turtle.right(90)
    prasad_turtle.forward(50)



jyo_height=5.4
prasad_height=6.0
if prasad_height>jyo_height:
    square()
else:
    prasad_turtle.forward(200)

print("Enter any Key")
input()