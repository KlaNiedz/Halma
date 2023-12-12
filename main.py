import pygame
from constants import WIDTH, HEIGHT
from board import Board

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Halma game")
FPS = 60


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
                pass
        board.draw_squares(screen)
        pygame.display.update()

    pygame.quit()


main()