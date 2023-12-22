from piece import Piece
from constants import GREEN


def test_create_piece():
    piece = Piece(0, 15, GREEN)
    assert piece.row == 0
    assert piece.col == 15
    assert piece.color == GREEN


def test_calc_pos():
    piece = Piece(0, 15, GREEN)
    assert piece.x == 775
    assert piece.y == 25
