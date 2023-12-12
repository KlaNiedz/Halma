import pygame
from constants import SQUARE_SIZE, ROWS, COLS, BROWN, WHITE, RED, GREEN


class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.green_left = 19

    def draw_squares(self, screen):
        """
        Drawing brown squares on board
        """
        screen.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(screen, BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

