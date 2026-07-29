import pygame
import sys
import json

# --- Settings ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("fence")
clock = pygame.time.Clock()

with open("fencing.json", "r") as f:
    JSON = json.load(f)


print(JSON["name"])



def lines(x, y, width, height, count):
    base = pygame.Rect(x, y, width, height)

    line_list = []
    spacing = width / count

    for i in range(count):
        start_pos = (x + i * spacing, y)
        end_pos = (x + i * spacing, y + height)
        line_list.append((start_pos, end_pos))

    return base, line_list

box = pygame.Rect(0, 300, 800, 300)
strip = pygame.Rect(20, 320, 760, 75)

ignore_this_line = pygame.Rect(20,320,4,75) #to cover up an extra line on the strip

box, line_positions = lines(0, 300, 800, 300, 14)
strip, line_positions2 = lines(20, 320, 760, 75, 6)
# --- Main Loop ---
running = True
while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # --- Drawing ---
    screen.fill((162,124,91))

    #BASE
    pygame.draw.rect(screen, (92,64,51), box)

    #BASE LINES
    for start, end in line_positions:
        pygame.draw.line(screen, (102,74,61), start, end, 2)

    #STRIP
    pygame.draw.rect(screen, (255,255,255), strip) 
    #STRIP LINES
    
    for start, end in line_positions2:
        pygame.draw.line(screen, (225,225,225), start, end, 4)


    


    pygame.draw.rect(screen, (255,255,255), ignore_this_line)




    pygame.display.flip()  # update the screen
    clock.tick(FPS)        

pygame.quit()
sys.exit()
