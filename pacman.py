import pygame
import math
from constants import *

class Pacman:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * CELL_SIZE + CELL_SIZE // 2
        self.y = row * CELL_SIZE + CELL_SIZE // 2
        self.direction = STOP
        self.next_direction = STOP
        self.speed = 4
        self.radius = CELL_SIZE // 2 - 2
        
    def update(self, maze):
        # Allow turning when exactly aligned with the center of a grid cell
        cx = self.col * CELL_SIZE + CELL_SIZE // 2
        cy = self.row * CELL_SIZE + CELL_SIZE // 2
        
        # Reverse direction immediately if trying to go back
        if self.next_direction != STOP and self.direction != STOP:
            if (self.next_direction[0] == -self.direction[0] and self.next_direction[1] == -self.direction[1]):
                self.direction = self.next_direction
        
        # Check if we are near the center of the current cell
        if abs(self.x - cx) < self.speed and abs(self.y - cy) < self.speed:
            if self.next_direction != STOP:
                next_r = self.row + self.next_direction[1]
                next_c = self.col + self.next_direction[0]
                # Can we turn?
                if not maze.is_wall(next_r, next_c):
                    # Snap to center
                    self.x = cx
                    self.y = cy
                    self.direction = self.next_direction
            
            # Can we keep moving forward?
            next_r = self.row + self.direction[1]
            next_c = self.col + self.direction[0]
            if maze.is_wall(next_r, next_c):
                # Snap and stop
                self.x = cx
                self.y = cy
                self.direction = STOP
                
        # Move
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
        
        # Wrap around screen edges
        if self.x < 0:
            self.x = SCREEN_WIDTH
        elif self.x > SCREEN_WIDTH:
            self.x = 0
            
        # Update current row and col based on current coordinates
        self.row = int(self.y // CELL_SIZE)
        self.col = int(self.x // CELL_SIZE)
        
    def draw(self, screen):
        # Temporary drawing of Pacman
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)), self.radius)
