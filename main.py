
import pygame
from constants import PIECES, ROWS, COLS, SQUARE_SIZE, WIDTH, HEIGHT, MODE
from constants import GREEN, RED
from game import Game
from algorithm import minimax


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
    if PIECES != 6 and PIECES != 13 and PIECES != 19:
        raise ValueError("Number of pieces can be 6, 13 or 19")

    if ROWS != COLS or WIDTH != HEIGHT:
        raise ValueError("The board must be square.")

    game_is_on = True
    clock = pygame.time.Clock()
    game = Game(screen)

    while game_is_on:
        clock.tick(FPS)

        if MODE == 'COMPvsPLAYER':
            if game.turn == GREEN:
                value, new_board = minimax(game.get_board(), 4, float('-inf'), float('inf'), GREEN, game)
                game.ai_move(new_board)

        if MODE == "COMPvsCOMP":
            if game.turn == GREEN:
                value, new_board = minimax(game.get_board(), 4, float('-inf'), float('inf'), GREEN, game)
                game.ai_move(new_board)

            elif game.turn == RED:
                value, new_board = minimax(game.get_board(), 4, float('-inf'), float('inf'), RED, game)
                game.ai_move(new_board)

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
