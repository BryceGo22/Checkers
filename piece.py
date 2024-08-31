# piece.py

import pygame
from constants import RED, WHITE, SQUARE_SIZE, PIECE_RADIUS

class Piece: 
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        self.x = 0
        self.y = 0
        self.calc_position()

    def calc_position(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, screen):
        radius = PIECE_RADIUS - self.PADDING
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)
        if self.king:
            pygame.draw.circle(screen, (255, 215, 0), (self.x, self.y), radius // 2)

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()
