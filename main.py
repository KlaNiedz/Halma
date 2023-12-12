import pygame
from constants import WIDTH, HEIGHT

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Halma game")
FPS = 60


def main():
    clock = pygame.time.Clock()
    game_is_on = True

    while game_is_on:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_on = False

    pygame.quit()