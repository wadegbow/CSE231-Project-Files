
import turtle

import proj06lib

def main():
    
    turtle.speed(100)   # draw fast
    
    # set up: so drawing happens roughly centered
    height = 16*6
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(200)
    turtle.setheading(0)
    turtle.pendown()

    # Draw a row of three flags in landscape orientation
    proj06lib.draw_flag('Denmark',height,'landscape')
    # move so second flag is next to the first
    turtle.penup()
    turtle.forward(140)
    turtle.pendown()
    # draw second flag
    proj06lib.draw_flag('Sweden',height,'LandScape')  # checking that you handle mixed case
    turtle.penup()
    turtle.forward(140)
    turtle.pendown()
    proj06lib.draw_flag('Faroe Islands',height,'LANDSCAPE')

    # Reposition turtle for drawing of second row of three flags
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(190)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()

    # Draw second row of three flags in portrait orientation
    proj06lib.draw_flag('Norway',height,'portrait')
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    proj06lib.draw_flag('Iceland',height,'Portrait')  # checking that you handle mixed case
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    proj06lib.draw_flag('Finland',height,'PoRtRaIt')

main()

