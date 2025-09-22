import turtle
import random

# Setup
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
#how big each line is
dis = 20

# Ask user for number of mirrored rotations
ref = int(input("Enter number of mirrored rotations: "))
# Uses a tuple to gain the coordinates and an array for all the mirrored and rotated lines
positions = [(0, 0)] * (ref * 2)

# Main loop, adds a line on to the previous line
for _ in range(100):
 # random direction for all the new lines
    dire = random.randint(-360, 360)

    for i in range(ref):
     # what rotates the orignal line
     #float() allows for more precise rotations
        angle_offset = float(360) / ref * fi

        # Original line
        t.penup()
        t.goto(positions[i * 2])
        t.pendown()
        heading = dire + angle_offset
        t.setheading(heading)
        t.forward(dis)
        positions[i * 2] = (t.xcor(), t.ycor())

        # Mirrored line
        t.penup()
        t.goto(positions[i * 2 + 1])
        t.pendown()
     #negative direction so its mirrored
        heading = -dire + angle_offset
        t.setheading(heading)
        t.forward(dis)
     # saves the position for the endpoint of the line created
        positions[i * 2 + 1] = (t.xcor(), t.ycor())

    # Return to first position
    t.penup()
    t.goto(positions[0])
    t.pendown()

