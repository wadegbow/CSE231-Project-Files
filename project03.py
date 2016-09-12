# Project 03
# The following program will output a latin square when the user
# provides an order and a starting value. It will provide errors
# if the order is greater than 9 or less than 1 and if the starting
# value falls outside of the order.

# latin square function, takes topleft and order values as input
# prints square as output
def latin_square(topleft, order):
    # create a list of the first line
    l = list(range(topleft, order+1)) + list(range(1, topleft))
    # get the length for use in our for loops
    x = len(l)

    # create another list to dump our values
    tmp = []

    # the first loop is for generating each "line"
    # it goes from zero and stops one short of the length of l
    # the second loop uses a descending range so that
    # when using the index i-j each value is shifted one left
    # for each preceding line after 0
    for i in range(x):
        for j in range(x,0,-1):
            tmp.append(l[i-j])
        # after each "line" a pipe is appended to make formatting easier
        tmp.append('|')

    # add whitespace
    print()

    # loop through each value in the tmp list
    for k in tmp:
        # if the value is equal to a pipe, add a linebreak
        if k == '|':
            print()
        # otherwise just print the value and a space
        else:
            print(k, end = ' ')

# take user input for the order of the latin square
order = int(input("Enter the order: "))

# prompt user for the starting number
topleft = int(input("Enter the starting number: "))

# check to make sure the order value is less than 10
# and greater than 0
if order < 1 or order > 9:
    print("Invalid value for order.")
    print("Value must be between 1 and 9")
    print("\n-- Program Halted --")

# check that the starting number falls in the range 1 to order
elif topleft < 1 or topleft > order:
    print("Invalid value for starting number.")
    print("Value must be between 1 and",order)
    print("\n-- Program Halted --")

# if both inputs pass our checks, run the latin_square function
else:
    latin_square(topleft, order)
