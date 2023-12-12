import pygame
from constants import SQUARE_SIZE, ROWS, COLS, BROWN, WHITE, RED, GREEN
from piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.green_left = 19
        self.create_board()

    def draw_squares(self, screen):
        """
        Drawing brown squares on board
        """
        screen.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(screen, BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        """
        create self.board which consists lists of rows,
        inside of each of list of rows there're pieces or empty square (0)
        """
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if row < 5 and col > 10:
                    if row == 0:
                        self.board[row].append(Piece(row, col, GREEN))
                    elif col >= 10 + row:
                        self.board[row].append(Piece(row, col, GREEN))
                    else:
                        self.board[row].append(0)
                elif col < 5 and row > 10:
                    if col == 0:
                        self.board[row].append(Piece(row, col, RED))
                    elif row >= 10 + col:
                        self.board[row].append(Piece(row, col, RED))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, screen):
        self.draw_squares(screen)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(screen)

