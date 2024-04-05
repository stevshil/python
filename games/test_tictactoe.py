import pytest

from tictactoe import Board

@pytest.fixture
def my_grid():
    '''
    Define a grid for testing
    '''
    my_board=Board(3,'X')
    my_board.move(1,1)
    my_board.move(0,0)
    my_board.move(1,2)
    my_board.move(0,1)
    my_board.move(1,0)
    return my_board

def test_show(my_grid):
    assert my_grid.show() == None

def test_checkrows(my_grid):
    assert my_grid.checkrows(3) == 'Win X Row'

def test_checkcols(my_grid):
    assert my_grid.checkcols(3) == None

def test_checkdiag(my_grid):
    assert my_grid.checkdiag(3) == None

if __name__ == "__main__":
    pytest.main(["-v"])