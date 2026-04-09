import pygame
import sys
from constants import *
from maze import Maze
from pacman import Pacman
from ghost import Ghost

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pacman")
    clock = pygame.time.Clock()

    maze = Maze()
    pacman = Pacman(15, 9)
    ghosts = [
        Ghost(9, 9, RED),
        Ghost(9, 8, PINK),
        Ghost(9, 10, CYAN),
        Ghost(8, 9, ORANGE)
    ]

    score = 0
    font = pygame.font.SysFont("Arial", 24)
    game_over = False
    win = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    pacman.next_direction = UP
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    pacman.next_direction = DOWN
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    pacman.next_direction = LEFT
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    pacman.next_direction = RIGHT

        if not game_over and not win:
            pacman.update(maze)
            
            cx, cy = int(pacman.x), int(pacman.y)
            r, c = cy // CELL_SIZE, cx // CELL_SIZE
            points = maze.eat_dot(r, c)
            if points > 0:
                score += points
                
            if maze.dots_left <= 0:
                win = True

            for g in ghosts:
                g.update(maze, pacman)
                if g.check_collision(pacman):
                    game_over = True

        screen.fill(BLACK)
        
        maze.draw(screen)
        pacman.draw(screen)
        for g in ghosts:
            g.draw(screen)
        
        score_surface = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surface, (10, SCREEN_HEIGHT - 40))
        
        if game_over:
            go_surface = font.render("GAME OVER", True, RED)
            screen.blit(go_surface, (SCREEN_WIDTH//2 - 60, SCREEN_HEIGHT//2))
        elif win:
            win_surface = font.render("YOU WIN!", True, YELLOW)
            screen.blit(win_surface, (SCREEN_WIDTH//2 - 40, SCREEN_HEIGHT//2))
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
