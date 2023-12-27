import pygame
from constants import SQUARE_SIZE, WIDTH, HEIGHT
from game import Game

pygame.init()

FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Halma game")


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
    game = Game(screen)

    while game_is_on:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())
            game_is_on = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


if __name__ == "__main__":
    main()
