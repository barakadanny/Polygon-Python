from turtle import Turtle, Screen
timmy_the_turtle = Turtle()


def draw_polygon(sides, length, color):
    timmy_the_turtle.color(color)
    for _ in range(sides):
        timmy_the_turtle.forward(length)
        timmy_the_turtle.right(360/sides)


# Triangle
draw_polygon(3, 70, "red")

# Square
draw_polygon(4, 70, "orange")

# Pentagon
draw_polygon(5, 70, "black")

# Hexagon
draw_polygon(6, 70, "pink")

# Heptagon
draw_polygon(7, 70, "green")

# Octagon
draw_polygon(8, 70, "blue")

# Nonagon
draw_polygon(9, 70, "brown")

# Decagon
draw_polygon(10, 70, "purple")


screen = Screen()
screen.exitonclick()
