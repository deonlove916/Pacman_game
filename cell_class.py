import pygame
from settings import *
import random

class Cell:
    def __init__(self, x, y, grid):
        self. pos = (x,y)
        self.grid = grid
        self.revealed = random.choice((True, False))
        self.size = CELL_SIZE
    
    def update(self):
        pass

    def draw(self):
        if self.revealed:
            pygame.draw.rect(self.grid.game.screen, CELL_BG_COLOR, (self.grid.pos[0] + (self.pos[0]*self.size), self.grid.pos[1] + (self.pos[1]*self.size), self.size, self.size), 2)
        if not self.revealed:
            pygame.draw.rect(self.grid.game.screen, (0,0,0), (self.grid.pos[0] + (self.pos[0]*self.size), self.grid.pos[1] + (self.pos[1]*self.size), self.size, self.size))
