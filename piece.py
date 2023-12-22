import pygame
from constants import GREY, SQUARE_SIZE


class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.final_position = False
        self.calculate_pos()

    def calculate_pos(self):
        """
        Calculate the x,y position of piece on board
        """
        self.x = SQUARE_SIZE*self.col + SQUARE_SIZE//2
        self.y = SQUARE_SIZE*self.row + SQUARE_SIZE//2

    def draw(self, screen):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(screen, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_pos()

    def __repr__(self):
        return str(self.color)
