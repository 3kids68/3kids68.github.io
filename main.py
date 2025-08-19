# Tank Battle Game
# by Jules

import pygame

def main():
    """Main game function"""
    pygame.init()

    # Screen dimensions
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Tank Battle")

    # Tank properties
    tank_width = 40
    tank_height = 40
    tank_x = (screen_width - tank_width) / 2
    tank_y = (screen_height - tank_height) / 2
    tank_speed = 5
    tank_color = (255, 255, 0)  # Yellow

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Key presses for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            tank_y -= tank_speed
        if keys[pygame.K_s]:
            tank_y += tank_speed
        if keys[pygame.K_a]:
            tank_x -= tank_speed
        if keys[pygame.K_d]:
            tank_x += tank_speed

        # Drawing
        screen.fill((0, 0, 0))  # Black background

        # Draw player tank
        pygame.draw.rect(screen, tank_color, (tank_x, tank_y, tank_width, tank_height))

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
