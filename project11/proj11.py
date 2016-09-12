# Project 11
# Classes and functions that aid in playing tic tac toe.

import turtle

class Tic_tac_toe(object):
    
    def __init__( self ):
        """
        Initializes the game grid and keeps track if the grid has beend drawn.
        """

        self.__grid = list(range(1,10))
        self.__drawnGrid = 0


    def draw( self ):
        """
        Draws the game grid and marks.
        """

        if self.__drawnGrid == 0:
            draw_grid().draw()

        self.__drawnGrid = 1

        column = 0
        row = 0
        i = 0
        for mark in self.__grid:
            if row == 0:
                turtle.goto(-60+60*column, 60)
            elif row == 1:
                turtle.goto(-60+60*column, 0)
            elif row == 2:
                turtle.goto(-60+60*column, -60)

            if isinstance(mark, str):
                if mark.lower() == 'x':   
                    drawX(i)
                elif mark.lower() == 'o':
                    drawO(i)

            column += 1

            if column == 3:
                column = 0
                row += 1

            i+=1

        turtle.goto(-60, 60)


    def set_mark( self, mark, index ):
        """
        Sets the mark at whatever index is provided.
        """

        try:
            int(self.__grid[index-1])

            if mark.lower() == 'x' or mark.lower() == 'o': 
                self.__grid[index-1] = mark

            return 1

        except ValueError:
            return 0


    def get_grid( self ):
        """
        Returns the game grid.
        """

        return self.__grid


    def determine_winner ( self ):
        """
        Using win functions to determine the winner of the game.
        """

        if self.columnWin() != None:
            return self.columnWin()

        elif self.diagonalWin() != None:
            return self.diagonalWin()

        elif self.rowWin() != None:
            return self.rowWin()

        else:
            return None


    def columnWin( self ):
        """
        Checks for win using columns.
        """

        for x in list(range(0,3)):
            firstVal = self.__grid[x]
            secondVal = self.__grid[x+3]
            thirdVal = self.__grid[x+6]

            compiledVal = str(firstVal) + str(secondVal) + str(thirdVal)

            if compiledVal.lower() == 'xxx':
                return 'X'

            elif compiledVal.lower() == 'ooo':
                return 'O'

        return None


    def diagonalWin( self ):
        """
        Checks for wins using the diagonals.
        """

        centerVal = self.__grid[4]

        diag1 = str(centerVal).lower() + str(self.__grid[0]).lower() \
        + str(self.__grid[8]).lower()
        diag2 = str(centerVal).lower() + str(self.__grid[2]).lower() \
        + str(self.__grid[6]).lower()

        if isinstance(centerVal, int):
            return None

        elif diag1 == 'xxx' or diag2 == 'xxx':
            return 'X'

        elif diag1 == 'ooo' or diag2 == 'ooo':
            return 'O'

        else:
            return None


    def rowWin( self ):
        """
        Checks for wins with rows.
        """

        for x in [0,3,6]:
            firstVal = self.__grid[x]
            secondVal = self.__grid[x+1]
            thirdVal = self.__grid[x+2]

            compiledVal = str(firstVal) + str(secondVal) + str(thirdVal)

            if compiledVal.lower() == 'xxx':
                return 'X'

            elif compiledVal.lower() == 'ooo':
                return 'O'  
        
        return None


    def checkColumns( self ):
        """
        Checks for win using columns.
        """

        for x in list(range(0,3)):
            firstVal = self.__grid[x]
            secondVal = self.__grid[x+3]
            thirdVal = self.__grid[x+6]

            compiledVal = str(firstVal) + str(secondVal) + str(thirdVal)

            if 'xx' in compiledVal.lower():
                return ('X', compiledVal)

            elif 'oo' in compiledVal.lower():
                return ('O', compiledVal)

            elif compiledVal.lower() == 'x4x' or \
                compiledVal.lower() == 'x5x' or \
                compiledVal.lower() == 'x6x':

                return ('X', compiledVal)                

        return None


    def checkDiagonals( self ):
        """
        Checks for wins using the diagonals.
        """

        centerVal = self.__grid[4]

        diag1 = str(centerVal).lower() + str(self.__grid[0]).lower() \
        + str(self.__grid[8]).lower()
        diag2 = str(centerVal).lower() + str(self.__grid[2]).lower() \
        + str(self.__grid[6]).lower()

        if isinstance(centerVal, int):
            return None

        elif 'xx' in diag1: 
            return ('X', diag1)

        elif 'xx' in diag2:
            return ('X', diag2)

        elif 'oo' in diag1:
            return ('O', diag1)

        elif 'oo' in diag2:
            return ('O', diag2)

        else:
            return None


    def checkRows( self ):
        """
        Checks for wins with rows.
        """

        for x in [0,3,6]:
            firstVal = self.__grid[x]
            secondVal = self.__grid[x+1]
            thirdVal = self.__grid[x+2]

            compiledVal = str(firstVal) + str(secondVal) + str(thirdVal)

            if 'xx' in compiledVal.lower():

                return ('X', compiledVal)

            elif 'oo' in compiledVal.lower():

                return ('O', compiledVal)  

            elif compiledVal.lower() == 'x2x' or \
                compiledVal.lower() == 'x5x' or \
                compiledVal.lower() == 'x8x':

                return ('X', compiledVal)
        
        return None              


    def full_board( self ):
        """
        Checks for a full game board.
        """

        for x in self.__grid:
            if isinstance(x, int):
                return False
            else:
                continue

        return True



class drawX(object):
    """
    Draws an X at the position of the cursor.
    """

    def __init__( self, spot ):
        #print('Printing X in spot', spot+1)

        # draw the x with turtle
        # reposition the pen
        turtle.left(45)
        turtle.backward(14)
        turtle.pendown()
        turtle.forward(28)
        turtle.right(45)
        turtle.penup()
        turtle.backward(20)
        turtle.right(45)
        turtle.pendown()
        turtle.forward(28)
        turtle.penup()
        turtle.backward(20)
        turtle.left(45)



class drawO(object):
    """
    Draws a circle at the position of the cursor.
    """

    def __init__( self, spot ):
        #print('Printing O in spot', spot+1)

        # draw the circle with turtle
        # reset pen position
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.pendown()
        turtle.circle(10)
        turtle.penup()
        turtle.left(90)
        turtle.forward(10)
        turtle.right(90)




class draw_grid(object):
    """
    This class will draw a grid.
    """

    def draw( self ):
        turtle.penup()
        turtle.forward(90)
        turtle.right(90)
        turtle.forward(30)
        turtle.pendown()

        # draw horizontal rectangle
        for x in list(range(0,4)):
            turtle.right(90)
            if x%2 == 0:
                turtle.forward(180)
            else:
                turtle.forward(60)

        turtle.right(90)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(60)

        # draw vertical rectangle
        for x in list(range(0,4)):
            turtle.right(90)
            if x%2 != 0:
                turtle.forward(180)
            else:
                turtle.forward(60)

        turtle.pencolor('white')
        turtle.right(90)
        turtle.forward(120)

        # erase the outside edges
        for x in list(range(0,4)):
            turtle.right(90)
            turtle.forward(180)

        # reset the pen
        turtle.pencolor('black')
        turtle.penup()
        turtle.right(180)
        turtle.goto(-60,60)



def computer_play( game ):
    """
    This function plays for the computer.
    Plays defensively using checkColumns, checkDiagonals and checkRows.
    """

    grid = game.get_grid()

    diag = game.checkDiagonals()
    row = game.checkRows()
    column = game.checkColumns()

    if isinstance(diag, tuple):
        
        for x in diag[1]:
            try:
                x = int(x)
                print(x)
                if isinstance(x, int):
                    if game.set_mark('O', x):
                        return

            except ValueError:
                continue

    elif isinstance(row, tuple):

        for x in row[1]:
            try:
                x = int(x)
                if isinstance(x, int):
                    if game.set_mark('O', x):
                        return

            except ValueError:
                continue

    elif isinstance(column, tuple):

        for x in column[1]:
            try:
                x = int(x)
                if isinstance(x, int):
                    if game.set_mark('O', x):
                        return

            except ValueError:
                continue                

    for x in list(range(1,10)):
        if game.set_mark('O', x):
            return
        else:
            continue


