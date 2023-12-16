import pygame
from constants import SQUARE_SIZE, WIDTH, HEIGHT
from board import Board
from piece import Piece
from constants import RED


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Halma game")
FPS = 60

def get_pos_from_mouse(pos):
    """
    Calculate row and col from position of mouse cursor
    """
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col
    

def main():
    game_is_on = True
    clock = pygame.time.Clock()
    board = Board()
    

    while game_is_on:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 10, 0)    

        board.draw(screen)
        
        pygame.display.update()

    

    pygame.quit()


main()