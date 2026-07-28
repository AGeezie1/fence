import pygame
import sys

# --- Settings ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Starter Template")
clock = pygame.time.Clock()

box = pygame.Rect(00, 300, 800, 300)

# --- Main Loop ---
running = True
while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # --- Drawing ---
    screen.fill((162,124,91))

    pygame.draw.rect(screen, (92,64,51), box)


    pygame.display.flip()  # update the screen
    clock.tick(FPS)        

pygame.quit()
sys.exit()
