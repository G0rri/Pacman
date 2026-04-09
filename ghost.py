import pygame
import random
from constants import *

class Ghost:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.x = col * CELL_SIZE + CELL_SIZE // 2
        self.y = row * CELL_SIZE + CELL_SIZE // 2
        self.color = color
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.speed = 3
        self.radius = CELL_SIZE // 2 - 2
        
    def update(self, maze, pacman):
        # Simple random AI
        cx = self.col * CELL_SIZE + CELL_SIZE // 2
        cy = self.row * CELL_SIZE + CELL_SIZE // 2
        
        if abs(self.x - cx) < self.speed and abs(self.y - cy) < self.speed:
            self.x = cx
            self.y = cy
            
            # Find available directions
            available = []
            for d in [UP, DOWN, LEFT, RIGHT]:
                if not maze.is_wall(self.row + d[1], self.col + d[0]):
                    available.append(d)
            
            # Avoid reversing direction if possible
            if self.direction != STOP:
                reverse = (-self.direction[0], -self.direction[1])
                if reverse in available and len(available) > 1:
                    available.remove(reverse)
            
            if available:
                self.direction = random.choice(available)
            else:
                self.direction = STOP
                
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
        
        # Wrapping
        if self.x < 0:
            self.x = maze.width
        elif self.x > maze.width:
            self.x = 0
            
        self.row = int(self.y // CELL_SIZE)
        self.col = int(self.x // CELL_SIZE)
        
    def check_collision(self, pacman):
        dist = ((self.x - pacman.x)**2 + (self.y - pacman.y)**2)**0.5
        return dist < (self.radius + pacman.radius)

    def draw(self, screen):
        # Simple circle for ghost
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        # Eyes
        pygame.draw.circle(screen, WHITE, (int(self.x) - 4, int(self.y) - 4), 3)
        pygame.draw.circle(screen, WHITE, (int(self.x) + 4, int(self.y) - 4), 3)
        pygame.draw.circle(screen, BLACK, (int(self.x) - 4 + self.direction[0], int(self.y) - 4 + self.direction[1]), 1)
        pygame.draw.circle(screen, BLACK, (int(self.x) + 4 + self.direction[0], int(self.y) - 4 + self.direction[1]), 1)
