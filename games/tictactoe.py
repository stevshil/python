'''
tic tac toe
'''

import sys

class Board:
    '''
    tictactoe Board class
    '''

    def __init__(self,grid_rows,start_item):
        self.grid=[]
        self.piece=start_item
        y_pos=0
        while y_pos < grid_rows:
            self.grid.append([' ' for _ in range(grid_rows)])
            y_pos=y_pos+1

    def move(self,grid_row,grid_col):
        '''
        Users move
        '''

        self.grid[grid_row][grid_col]=self.piece
        if self.piece == 'X':
            self.piece='O'
        else:
            self.piece='X'

    def show(self):
        '''
        Show current grid
        '''
        sys.stdout.write('\033[2J')

        backrow='\033[0;0f'
        sys.stdout.write(backrow*3)

        for _,this_row in enumerate(self.grid):
            sys.stdout.write('|')
            for _,this_col in enumerate(this_row):
                sys.stdout.write(this_col+'|')
            sys.stdout.write('\n')
            sys.stdout.flush()

    def checkrows(self,win_rows):
        '''
        Check if winning line
        '''

        # Check rows
        for row in range(win_rows):
            win=0
            for col in range(win_rows):
                if self.grid[row][col] == 'X':
                    win=win+1
                if self.grid[row][col] == 'Y':
                    win=win-1
            if win == win_rows:
                winner='Win X Row'
                break
            if win == -win_rows:
                winner='Win Y Row'
                break
            winner=None

        return winner

    def checkcols(self,win_rows):
        '''
        Check winning column
        '''
        # Check columns
        for col in range(win_rows):
            win=0
            for row in range(win_rows):
                if self.grid[row][col] == 'X':
                    win=win+1
                if self.grid[row][col] == 'Y':
                    win=win-1
            if win == win_rows:
                winner='Win X Col'
                break
            if win == -win_rows:
                winner='Win Y Col'
                break
            winner=None

        return winner

    def checkdiag(self,win_rows):
        '''
        Check for winning diagonal
        '''
        counter=0
        win1=0
        win2=0
        counter=0
        # Top left to bottom right
        while counter < win_rows:
            if counter == 0:
                x=win_rows-1
            else:
                x=x-1

            if self.grid[counter][counter] == 'X':
                win1=win1+1
            if self.grid[counter][counter] == 'Y':
                win1=win1-1
            if self.grid[counter][x] == 'X':
                win2=win2+1
            if self.grid[counter][x] == 'Y':
                win2=win2-1
            counter=counter+1

        if win1 == win_rows:
            winner = 'Win X Col'
        elif win1 == -win_rows:
            winner = 'Win Y Col'
        elif win2 == win_rows:
            winner = 'Win X Col'
        elif win2 == -win_rows:
            winner = 'Win Y Col'
        else:
            winner = None

        return winner

if __name__ == "__main__":
    GRID_ROWS=3
    mygrid=Board(GRID_ROWS,'X')
    mygrid.show()
    mygrid.move(1,1)
    mygrid.show()
    mygrid.move(0,0)
    mygrid.show()
    mygrid.move(1,2)
    mygrid.move(0,1)
    mygrid.move(1,0)
    mygrid.show()
    print(mygrid.checkrows(GRID_ROWS))
    print(mygrid.checkcols(GRID_ROWS))
    print(mygrid.checkdiag(GRID_ROWS))
