"""This program uses the Turtle package to create a unique drawing each time it is run. The drawing includes a dirt bottom, assortment of different size trees that fill the middle of the drawing, and muticolor birds that fill the top of the painting. For consistency, length is always a horizontal, and width is always vertical."""

__author__ = "730477982"

import math
from turtle import Turtle, colormode, done 
from random import randint
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    todd: Turtle = Turtle()
    todd.speed(100)
    todd.hideturtle()

    draw_dirt(todd, -650, -250)

    count_1: int = 0
    while count_1 < 50:
        """Loops to draw 50 tress of different size, using the draw_tree fucntion."""
        draw_tree(todd, randint(-600, 600), randint(-250, 200), randint(2, 10))
        count_1 += 1
    
    count_2: int = 0
    while count_2 < 10:
        """Loops to draw 10 different color, and size, birds using the draw_bird function."""
        draw_bird(todd, randint(-600, 600), randint(200, 320), randint(1, 3))
        count_2 += 1
    done()


def draw_tree(todd: Turtle, x: float, y: float, multiplier: float) -> None:
    """Draws one tree, given the Turtle, x and y coordinates, and a multiplier. The random mutiplier given to the function is what allows the tree to be a random size each time."""
    todd.penup()
    todd.goto(x, y)
    todd.setheading(0.0)
    todd.pendown()

    trunk_length: float = 3 * multiplier
    trunk_width: float = 4 * multiplier
    
    """Draws a tree trunk."""
    todd.color(79, 41, 1)
    draw_rectangle(todd, x, y, trunk_length, trunk_width)

    """Pythagorean theorem used to creat lines that connect to top of the tree"""
    todd.color(43, 194, 14)
    tree_height: float = pythagorean_theorem(trunk_width + trunk_length / 2, trunk_width * 2)
    todd.setheading(0.0)
    todd.begin_fill()

    """Draws the top of tree. The specific degrees of turning are for a "3, 4, 5 triangle"."""
    todd.forward(trunk_width + trunk_length)
    todd.left(126.9)
    todd.forward(tree_height)
    todd.left(106.4)
    todd.forward(tree_height)
    todd.left(126.9)
    todd.forward(trunk_width * 2 + trunk_length)
    todd.end_fill()


def draw_bird(todd: Turtle, x: float, y: float, multiplier: float) -> None:
    """Draws a bird, given a Turtle, x and y coordinates and a multiplier. Again, the multiplier allows for different sizes of birds."""
    todd.penup()
    todd.goto(x, y)
    todd.setheading(0.0)
    todd.pendown()

    """Makes a random color, 7 is used because that made desirable sized birds."""
    todd.color(randint(0, 255), randint(0, 255), randint(0, 255))
    length: float = 7 * multiplier
    width: float = 7 / 3 * multiplier
     
    """Draws the bird."""
    todd.forward(length)
    todd.right(90)
    todd.forward(width)
    todd.left(90)
    todd.forward(length / 2)
    todd.right(90)
    todd.forward(width)
    todd.left(90)
    todd.forward(length / 2)
    todd.left(90)
    todd.forward(width)
    todd.right(90)
    todd.forward(length / 2)
    todd.left(90)
    todd.forward(width)
    todd.right(90)
    todd.forward(length)


def draw_dirt(todd: Turtle, x: float, y: float) -> None:
    """Given a turtle, x and y coordinates, draws dirt at the bottom of screen."""
    todd.penup()
    todd.goto(x, y)
    todd.setheading(0.0)
    todd.pendown()

    """Draws the dirt."""
    todd.color(109, 56, 0)
    draw_rectangle(todd, x, y, 1300, 300)


def draw_rectangle(todd: Turtle, x: float, y: float, length: float, width: float) -> None:
    """Given a Turtle, x and y coordinates, length and width, draws a rectangle."""
    todd.penup()
    todd.goto(x, y)
    todd.setheading(0.0)
    todd.pendown()

    count: int = 0
    todd.begin_fill()
    while count < 2:
        """Loops to draw the rectangle."""
        todd.forward(length)
        todd.right(90)
        todd.forward(width)
        todd.right(90)
        count += 1
    
    todd.end_fill()


def pythagorean_theorem(a: float, b: float) -> float:
    """Given side a and b, executes the pythagorean theorem and returns side c."""
    side_c: float = (math.sqrt(a ** 2 + b ** 2))
    return side_c


if __name__ == "__main__":
    main()