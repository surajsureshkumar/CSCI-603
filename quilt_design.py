"""
CSCI-603: Assignment 1
Author: Suraj Sureshkumar (ss7495@g.rit.edu)

This is a homework program that draws the quilt design along with
an own design for the third and final block whereas the design
for the first two blocks are pre-requisites.
"""

import turtle as t


def init():
    """
    Initialize for drawing.  (-200, -200) is in the lower left and
    (200, 200) is in the upper right.
    :pre: pos (0,0), heading (east), right
    :post: pos (0,0), heading (east), right
    :return: None
    """
    t.setup(1.0, 1.0)
    t.up()
    t.setheading(0)
    t.showturtle()
    t.title('quilt_design')
    t.speed(0)


def square_block_borders():
    """
    Drawing the outer and the inner square borders using the turtle functions
    :pre: pos relative, heading (east), right
    :post: pos relative, heading (east), right
    :return: None
    """
    t.pendown()
    for i in range(4):  # Loop to draw the outer square
        t.forward(200)
        t.left(90)
    t.penup()
    t.forward(20)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.pendown()
    for i in range(4):  # Loop to draw the inner square
        t.forward(160)
        t.left(90)
    t.forward(180)
    t.back(200)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.back(200)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.back(200)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.back(200)
    t.right(90)
    t.back(180)
    t.penup()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)


def block1_bigger_triangle():
    """
    Draws the bigger triangle design
    :pre: pos relative, heading (east), right
    :post: pos relative, heading (east), right
    :return: None
    """
    t.color('purple')  # Selecting the color
    t.begin_fill()  # Color fill beings for the triangle

    t.pendown()
    t.forward(50)
    t.left(135)
    t.forward(35)
    t.left(90)
    t.forward(35)

    t.end_fill()  # Color fill ends
    t.color('pink')  # Turtle pointer color is changed to pink for the smaller triangle


def block1_smaller_triangle():
    """
    Draws the smaller triangle design
    :pre: pos relative, heading (east), right
    :post: pos relative, heading (east), right
    :return: None
    """
    t.color('pink')  # Selecting the color
    t.begin_fill()  # Color fill beings for the triangle
    t.forward(25)
    t.right(90)
    t.forward(25)
    t.right(135)
    t.forward(35)
    t.right(135)

    t.end_fill()  # Color fill ends
    t.color('black')  # Turtle pointer color is changed to default


def block2_design():
    """
    This function block holds the code for block2 design
    :pre: pos relative, heading (east), right
    :post: pos relative, heading (east), right
    :return: None
    """

    # Lines 168-176 draws the triangle in color orange
    t.pendown()
    t.color('orange')
    t.begin_fill()
    t.forward(35)
    t.left(135)
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.back(25)
    t.end_fill()
    t.color('black')


def block3_design():
    """
    Draws the third design
    :pre: pos relative, heading (east), right
    :post: pos relative, heading (east), right
    :return: None
    """
    t.pendown()
    t.color('maroon')
    for i in range(70):
        t.circle(i, 45)
    t.penup()
    t.left(90)
    t.forward(70)
    t.pendown()


def main():
    """
    This is the main method which consists of all other methods used to generate a part of the design
    :pre: pos (0,0), heading (east), right
    :post: pos (0,0), heading (east), right
    :return: None
    """
    init()
    t.penup()
    t.back(350)
    t.pendown()
    square_block_borders()
    block1_bigger_triangle()
    t.right(135)
    block1_bigger_triangle()
    t.right(135)
    block1_bigger_triangle()
    t.right(135)
    block1_bigger_triangle()
    t.right(135)
    block1_smaller_triangle()
    t.left(90)
    block1_smaller_triangle()
    t.left(90)
    block1_smaller_triangle()
    t.left(90)
    block1_smaller_triangle()
    t.left(90)

    t.penup()
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(180)
    t.forward(250)
    t.pendown()

    square_block_borders()

    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(180)
    t.forward(85)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.forward(25)
    t.right(180)

    block2_design()
    t.right(45)
    t.penup()
    t.forward(17.5)
    t.right(180)
    t.pendown()

    block2_design()
    t.penup()
    t.right(45)
    t.forward(17.5)
    t.right(90)
    t.forward(35)
    t.right(180)
    t.pendown()

    block2_design()
    t.penup()
    t.right(45)
    t.forward(17.5)
    t.right(180)
    t.pendown()

    block2_design()
    t.penup()
    t.right(45)
    t.forward(17.5)
    t.right(90)
    t.forward(35)
    t.right(180)

    block2_design()
    t.right(45)
    t.forward(17.5)
    t.right(180)

    block2_design()
    t.penup()
    t.right(45)
    t.forward(17.5)
    t.right(90)
    t.forward(35)
    t.right(180)
    t.pendown()

    block2_design()
    t.right(45)
    t.forward(17.5)
    t.right(180)

    block2_design()
    t.penup()
    t.right(45)
    t.forward(17.5)
    t.forward(60)
    t.right(90)
    t.forward(100)
    t.right(180)

    t.forward(250)
    square_block_borders()
    block3_design()

    t.mainloop()


if __name__ == '__main__':
    main()
