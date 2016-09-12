# Project 6
# Program draws Scandinavian flags using three functions;
# draw_flag, draw_rectangle and draw_cross

import turtle

def draw_flag(name, width, orientation):
    name = name.lower() # convert country name to lowercase
    orientation = orientation.lower() # convert orientation to lower
    # flag_config is a dictionary containing all of the settings
    # for each flag, this makes adding new flags or editing current flags
    # a manageable task
    flag_config = {'denmark':
                       {
                        'rectangle': {'color':'#C60C30'},
                        'cross': {0:{'color':'#FFFFFF', 'style':'singleton'}}
                        },
                   'norway':
                       {
                       'rectangle': {'color':'#ED2939'},
                       'cross': {0:{'color':'#FFFFFF', 'style':'thick'},
                                 1:{'color':'#002664', 'style':'thin'}}
                       },
                    'sweden':
                       {
                        'rectangle': {'color':'#006AA7'},
                        'cross': {0:{'color':'#FECC00', 'style':'singleton'}}
                        },
                    'finland':
                       {
                        'rectangle': {'color':'#FFFFFF'},
                        'cross': {0:{'color':'#003580', 'style':'singleton'}}
                        },
                    'iceland':
                       {
                        'rectangle': {'color':'#003897'},
                        'cross': {0:{'color':'#FFFFFF', 'style':'thick'},
                                  1:{'color':'#D72828', 'style':'thin'}}
                        },
                    'faroe islands':
                       {
                        'rectangle': {'color':'#FFFFFF'},
                        'cross': {0:{'color':'#0065BD', 'style':'thick'},
                                  1:{'color':'#ED2939', 'style':'thin'}}
                        }
                   }

    # error checking
    # width must be greater than 0
    if width > 0:
        rec_width = width
        rec_length = width*1.321428571
    else:
        print('Width must be greater than 0.')
        return None
    # country name has to be one of the 6 scandinavian countries
    if name not in flag_config:
        print('Invalid country entered.')
        return None
    # orientation must be either portrait or landscape
    if orientation != 'portrait' and orientation != 'landscape':
        print('Invalid orientation entered.')
        return None

    # set the color to the preset in flag_config
    color_rectangle = flag_config[name]['rectangle']['color']

    # set the turtle's colormode to 255 (RGB)
    turtle.colormode(255)

    # check orientation, rotate if portrait
    if orientation == 'portrait':
        turtle.right(90)

    # call draw_rectangle
    draw_rectangle(rec_length, rec_width, color_rectangle)

    # use a for loop to call draw_cross so flags with
    # multiple crosses will run the draw_cross function multiple times
    for val in flag_config[name]['cross'].values():
        draw_cross(rec_length, rec_width, val['color'], val['style'])

    # check orientation, rotate back if portrait
    if orientation == 'portrait':
        turtle.left(90)

# draw_rectangle is run by draw_flag
# it will draw a rectangle when given a length, width and color
# draw_rectangle does not error check on it's own, draw_flag
# handles that, so we assume all values are valid
def draw_rectangle(length, width, color):
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.end_fill()

# draw_cross is run by draw_flag
# it will draw a cross when given a length, width, color and style
# draw_cross does not error check on it's own, draw_flag
# handles that, so we assume all values are valid
def draw_cross(length, width, color, style):
    style = style.lower() # covert style to lowercase

    # check the style and calculate ratios
    if style == 'thick':
        cross_width = length * .18181818
        cross_padding = 0
    elif style == 'thin':
        cross_width = length * .090909091
        cross_padding = cross_width/2
    elif style == 'singleton':
        cross_width = length * .108108108
        cross_padding = cross_width/2

    turtle.penup()
    turtle.forward((length/2)-(cross_width+cross_padding))
    turtle.color(color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(cross_width)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(cross_width)
    turtle.right(90)
    turtle.forward(width)
    turtle.end_fill()
    
    turtle.penup()
    turtle.left(90)
    turtle.forward((length/2)-(cross_width+cross_padding))
    turtle.left(90)
    turtle.forward((width/2)-(cross_width/2))

    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(cross_width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(cross_width)
    turtle.end_fill()
    turtle.penup()
    turtle.forward((width/2)-(cross_width/2))
    turtle.right(90)
