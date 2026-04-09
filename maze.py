import pygame
from constants import *

# 1 = wall, 0 = dot, 2 = empty, 3 = power pellet

class Maze:
    def __init__(self, level_data):
        self.grid = [row[:] for row in level_data]
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.width = self.cols * CELL_SIZE
        self.height = self.rows * CELL_SIZE
        self.dots_left = sum(row.count(0) for row in self.grid) + sum(row.count(3) for row in self.grid)
        self.wall_color = BLUE
        self.dot_color = WHITE
        
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                val = self.grid[row][col]
                x = col * CELL_SIZE
                y = row * CELL_SIZE
                
                if val == 1:
                    pygame.draw.rect(screen, self.wall_color, (x, y, CELL_SIZE, CELL_SIZE), 2)
                    pygame.draw.rect(screen, self.wall_color, (x+4, y+4, CELL_SIZE-8, CELL_SIZE-8), 1)
                elif val == 0:
                    pygame.draw.circle(screen, self.dot_color, (x + CELL_SIZE//2, y + CELL_SIZE//2), 3)
                elif val == 3:
                    pygame.draw.circle(screen, self.dot_color, (x + CELL_SIZE//2, y + CELL_SIZE//2), 8)

    def is_wall(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col] == 1
        return True

    def eat_dot(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if self.grid[row][col] in (0, 3):
                val = self.grid[row][col]
                self.grid[row][col] = 2
                self.dots_left -= 1
                return 10 if val == 0 else 50
        return 0
