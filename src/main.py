# filepath: moving-circle-py/moving-circle-py/src/main.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, CIRCLE_COLOR, OBSTACLE_COLOR, CIRCLE_RADIUS, OBSTACLE_WIDTH, OBSTACLE_HEIGHT, FPS
from entities.circle import Circle
from entities.obstacle import Obstacle
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Moving Circle Demo")
    clock = pygame.time.Clock()

    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.create_circle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, CIRCLE_RADIUS)
    # automatic velocity (pixels per second)
    game.circle.vx = 160.0
    game.circle.vy = 120.0

    # stationary obstacles
    game.add_obstacle(150, 120, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
    game.add_obstacle(400, 300, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)
    game.add_obstacle(600, 100, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)

    running = True
    while running:
        dt_ms = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # NO manual input: update physics with dt in seconds
        game.update(dt=dt_ms / 1000.0)

        # Draw
        screen.fill(BACKGROUND_COLOR)

        # Draw semi-transparent expanded obstacle areas (expanded by circle radius)
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        r = int(game.circle.radius)
        expanded_color = (255, 255, 0, 128)  # yellow, 50% transparent
        for ob in game.obstacles:
            infl_rect = pygame.Rect(int(ob.x - r), int(ob.y - r), int(ob.width + 2 * r), int(ob.height + 2 * r))
            pygame.draw.rect(overlay, expanded_color, infl_rect)
        screen.blit(overlay, (0, 0))

        # draw obstacles on top (opaque)
        for ob in game.obstacles:
            pygame.draw.rect(screen, OBSTACLE_COLOR, pygame.Rect(int(ob.x), int(ob.y), int(ob.width), int(ob.height)))

        # draw moving circle and its core dot
        pygame.draw.circle(screen, CIRCLE_COLOR, (int(game.circle.x), int(game.circle.y)), int(game.circle.radius))
        core_dot_color = (0, 0, 0)
        pygame.draw.circle(screen, core_dot_color, (int(game.circle.x), int(game.circle.y)), max(2, int(game.circle.radius * 0.12)))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()