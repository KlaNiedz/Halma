from board import Board
from constants import RED, GREEN, ROWS, COLS, PIECES
from piece import Piece


def test_create_board_object():
    board_object = Board()
    assert board_object.red_left == 6
    assert board_object.green_left == 6
    assert board_object.winner_green == 0
    assert board_object.winner_red == 0

# board_object.board[0][0] = Piece(11, 11, BUTTON_WHEELUP)
    # assert repr(board_object.board[0][11]) == '(0, 204, 0)'


def test_create_board_table():
    board_obj = Board()
    piece = board_obj.board[0][COLS-1]
    assert isinstance(piece, Piece)


def test_check_winner_green():
    board_object = Board()
    board_object.green_left = 0
    assert board_object.check_winner() == GREEN


def test_check_winner_red():
    board_object = Board()
    board_object.red_left = 0
    assert board_object.check_winner() == RED


def test_check_winner():
    halma_board = Board()
    for row in range(ROWS):
        for col in range(COLS):
            PIECES == 6
            max_piec_in_row = PIECES//2
            if col >= COLS - max_piec_in_row and row < max_piec_in_row:
                if col >= COLS - max_piec_in_row + row:
                    halma_board.board[row][col] = Piece(row, col, RED)
    halma_board.check_winner()
    assert halma_board.red_left == 0


def test_get_moves():
    # WIDTH, HEIGHT = 800, 800
    # ROWS, COLS = 10, 10
    # SQUARE_SIZE = WIDTH//COLS
    # # 3 possible amount of pieces: 6, 13, 19
    # PIECES = 6
    board_obj = Board()
    result = board_obj._left(2, 0, -1, GREEN, 0, skipped=[])
    assert result == {(0, 2): []}
