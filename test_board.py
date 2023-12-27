from board import Board
from constants import SQUARE_SIZE, ROWS, COLS, BROWN, WHITE, RED, GREEN
from piece import Piece


def test_tuple():
    ta = Piece(0, 0, GREEN)
    tb = Piece(0, 0, GREEN)
    assert ta == tb

def test_create_board_object():
    board_object = Board()
    assert board_object.red_left == 6
    assert board_object.green_left == 6
    assert board_object.winner_green == 0
    assert board_object.winner_red == 0

# board_object.board[0][0] = Piece(11, 11, BUTTON_WHEELUP)
    # assert repr(board_object.board[0][11]) == '(0, 204, 0)'

def test_create_board_table():
    board_object = Board()
    assert board_object.board[0] == ['empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', 'empty', "piece", "piece", "piece", "piece", "piece"]


def test_check_winner_green():
    board_object = Board()
    board_object.winner_green = 19
    assert board_object.check_winner() == GREEN


def test_check_winner_red():
    board_object = Board()
    board_object.winner_red = 19
    assert board_object.check_winner() == RED


def test_check_winner():
    board_object = Board()
    for row in range(ROWS):
        for col in range(COLS):
            if row < 5 and col > 10:
                if row == 0:
                    board_object.board[row].append(Piece(row, col, RED))
                elif col >= 10 + row:
                    board_object.board[row].append(Piece(row, col, RED))
    board_object.check_winner()
    assert board_object.winner_red == 19

def test_get_moves():
    WIDTH, HEIGHT = 800, 800
    ROWS, COLS = 10, 10
    SQUARE_SIZE = WIDTH//COLS
    # 3 possible amount of pieces: 6, 13, 19
    PIECES = 6
    board_o = Board()
    result = board_o._left(2, 0, -1, GREEN, 0, skipped=[])
    assert result == {(0, 2): []}
