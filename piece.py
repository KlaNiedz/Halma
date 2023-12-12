import pygame
from constants import RED, GREEN, SQUARE_SIZE


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calculate_pos

    def calculate_pos(self):
        """
        Calculate the x,y position of piece on board
        """
        self.x = SQUARE_SIZE*self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE//2

    def draw(self, screen):
        radius = SQUARE_SIZE//2
        pygame.draw.circle(screen, RED, (self.x, self.y), radius)
        pygame.draw.circle(screen, GREEN, (self.x, self.y), radius)

    