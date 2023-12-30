from board import Board
from constants import RED, GREEN, ROWS, COLS, PIECES
from piece import Piece


def test_create_board_object():
    # PIECES = 6
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
    assert halma_board.winner_red == 6
    assert halma_board.check_winner() == "RED WON"


def test_get_moves():
    # WIDTH, HEIGHT = 800, 800
    # ROWS, COLS = 10, 10
    # SQUARE_SIZE = WIDTH//COLS
    # # 3 possible amount of pieces: 6, 13, 19
    # PIECES = 6
    board_obj = Board()
    result = board_obj._left(2, 0, -1, GREEN, 0, skipped=[])
    assert result == {(0, 2): []}


def test_calculate_distance():
    board = Board()
    piece = Piece(0, 5, GREEN)
    desination_zone = [(4, 0), (4, 1)]
    assert board.calculate_distance(piece, desination_zone) == 8


def test_move():
    board = Board()
    piece = Piece(1, 0, GREEN)
    board.move(piece, 2, 0)
    assert piece.row == 2
    assert piece.col == 0
    assert piece.x == 50
    assert piece.y == 250


def test_get_piece():
    board = Board()
    piece = Piece(0, 6, GREEN)
    assert board.get_piece(0, 6).color == piece.color
    assert board.get_piece(0, 6).row == piece.row
    assert board.get_piece(0, 6).col == piece.col


def test_get_options_of_move():
    board = Board()
    piece = Piece(6, 1, RED)
    assert board.get_options_of_move(piece) == {(5, 2): [], (5, 1): [], (6, 2): []}

