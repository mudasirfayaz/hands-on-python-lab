import turtle as t
import random

# Enable RGB colors
t.colormode(255)


def draw_dot_grid(rows, cols, dot_size, spacing):
    """Draw a dot painting grid with customizable parameters."""
    color_list = [
        (198, 13, 32),
        (248, 236, 25),
        (40, 76, 188),
        (39, 216, 69),
        (238, 227, 5),
        (227, 159, 49),
        (29, 40, 154),
        (212, 76, 15),
        (17, 153, 17),
        (241, 36, 161),
        (195, 16, 12),
        (223, 21, 120),
        (68, 10, 31),
        (61, 15, 8),
        (223, 141, 206),
        (11, 97, 62),
    ]

    # Set up turtle
    tom = t.Turtle()
    tom.speed(0)
    tom.penup()
    tom.hideturtle()

    # Center the grid
    start_x = -spacing * cols // 2
    start_y = -spacing * rows // 2
    tom.goto(start_x, start_y)

    for i in range(rows):
        for j in range(cols):
            tom.dot(dot_size, random.choice(color_list))
            tom.forward(spacing)
        tom.goto(start_x, start_y + (i + 1) * spacing)


# Example usage
draw_dot_grid(rows=10, cols=10, dot_size=25, spacing=50)

t.done()
