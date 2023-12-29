from constants import GREEN, RED
from game import Game
import pygame


def test_change_turn():
    screen = pygame.display.set_mode((800, 800))
    game = Game(screen)
    game.turn = RED
    game.change_turn()
    assert game.turn == GREEN