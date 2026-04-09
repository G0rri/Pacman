import pygame
import sys
from constants import *
from maze import Maze
from pacman import Pacman
from ghost import Ghost
<<<<<<< HEAD
from levels import LEVEL_1, LEVEL_2

def find_spawn(maze, preferred_row_pct=0.5, preferred_col_pct=0.5):
    target_r = int(maze.rows * preferred_row_pct)
    target_c = int(maze.cols * preferred_col_pct)
    
    # search outwards from target
    for rad in range(max(maze.rows, maze.cols)):
        for r in range(max(0, target_r - rad), min(maze.rows, target_r + rad + 1)):
            for c in range(max(0, target_c - rad), min(maze.cols, target_c + rad + 1)):
                if not maze.is_wall(r, c):
                    return r, c
    return 1, 1

def main():
    pygame.init()
    pygame.display.set_caption("Pacman")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)

    levels = [LEVEL_1, LEVEL_2]
    current_level_idx = 0
    score = 0
    
    while current_level_idx < len(levels):
        level_data = levels[current_level_idx]
        maze = Maze(level_data)
        
        screen_width = maze.width
        screen_height = maze.height + 50
        screen = pygame.display.set_mode((screen_width, screen_height))
        
        pr, pc = find_spawn(maze, 0.75, 0.5)
        pacman = Pacman(pr, pc)
        
        gr, gc = find_spawn(maze, 0.4, 0.5)
        ghosts = [
            Ghost(gr, gc, RED),
            Ghost(gr, gc, PINK),
            Ghost(gr, gc, CYAN),
            Ghost(gr, gc, ORANGE)
        ]

        # Wait a bit before starting
        pygame.time.wait(1000)

        running_level = True
        game_over = False
        win_level = False

        while running_level:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        pacman.next_direction = UP
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        pacman.next_direction = DOWN
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        pacman.next_direction = LEFT
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        pacman.next_direction = RIGHT

            if not game_over and not win_level:
                pacman.update(maze)
                
                cx, cy = int(pacman.x), int(pacman.y)
                r, c = cy // CELL_SIZE, cx // CELL_SIZE
                points = maze.eat_dot(r, c)
                if points > 0:
                    score += points
                    
                if maze.dots_left <= 0:
                    win_level = True

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
            screen.blit(score_surface, (10, maze.height + 10))
            
            if game_over:
                go_surface = font.render("GAME OVER", True, RED)
                screen.blit(go_surface, (screen_width//2 - 60, screen_height//2))
            elif win_level:
                msg = "LEVEL COMPLETE" if current_level_idx < len(levels) - 1 else "YOU WIN!"
                win_surface = font.render(msg, True, YELLOW)
                screen.blit(win_surface, (screen_width//2 - 80, screen_height//2))
            
            pygame.display.flip()
            clock.tick(FPS)
            
            if game_over:
                pygame.time.wait(2000)
                pygame.quit()
                sys.exit()
            elif win_level:
                pygame.time.wait(2000)
                current_level_idx += 1
                running_level = False
=======

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
>>>>>>> e1f9903d7d85c8135338c00bf9c061eff053ba0b

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
