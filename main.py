# main.py

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SQUARE_SIZE
from game import Game

FPS = 60

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Checkers')
    clock = pygame.time.Clock()
  
    game = Game()

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE
                game.select(row, col)

        game.update(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
