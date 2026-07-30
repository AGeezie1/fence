import pygame
import sys
import json

# --- Settings ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
L_SPEED = 5
R_SPEED = 5
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("fence")
clock = pygame.time.Clock()


# info
# player size is (60,90)

with open("fencing.json", "r") as f:
    JSON = json.load(f)

# ----------------- initialize images --------------
l_fencer_base = pygame.image.load(JSON["player1"]["left_fencer"])
l_fencer_parry = pygame.image.load(JSON['player1']['left_fencer_parry'])

r_fencer_base = pygame.image.load(JSON['player2']['right_fencer'])
r_fencer_parry = pygame.image.load(JSON['player2']['right_fencer_parry'])





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

#player_test = pygame.Rect(50,270,60,90)

ignore_this_line = pygame.Rect(20,320,4,75) #to cover up an extra line on the strip

box, line_positions = lines(0, 300, 800, 300, 14)
strip, line_positions2 = lines(20, 320, 760, 75, 6)


l_fencer_rect = l_fencer_base.get_rect()
l_fencer_rect.x = 60
l_fencer_rect.y = 270

r_fencer_rect = r_fencer_base.get_rect()
r_fencer_rect.x = 700
r_fencer_rect.y = 270

r_fencer_current = r_fencer_base
l_fencer_current = l_fencer_base
# --- Main Loop ---
running = True
while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_LEFT:
    keys = pygame.key.get_pressed()

    # --- map drawing ---
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
    #------------------------------

    #just to see the player rect for now
    #pygame.draw.rect(screen, (255,0,255), r_fencer_rect)

    screen.blit(l_fencer_current,(l_fencer_rect))
    screen.blit(r_fencer_current,(r_fencer_rect))

    if keys[pygame.K_a] and l_fencer_rect.x > 10 :
        l_fencer_rect.x -= L_SPEED
    if keys[pygame.K_d] and l_fencer_rect.x < r_fencer_rect.x - 15:
        l_fencer_rect.x += L_SPEED

    if keys[pygame.K_LEFT] and r_fencer_rect.x > l_fencer_rect.x + 15:
        r_fencer_rect.x -= R_SPEED
    if keys[pygame.K_RIGHT] and r_fencer_rect.x < 730:
        r_fencer_rect.x += R_SPEED
    

    #slow when blocking
    if keys[pygame.K_s]:
        l_fencer_current = l_fencer_parry
        L_SPEED = 2.5
    #regulate
    if keys[pygame.K_s] == False:
        l_fencer_current = l_fencer_base
        L_SPEED = 5

    if keys[pygame.K_DOWN]:
        r_fencer_current = r_fencer_parry
        R_SPEED = 2.5

    if keys[pygame.K_DOWN] == False:
        r_fencer_current = r_fencer_base
        R_SPEED = 5



    

    pygame.display.flip()  # update the screen
    clock.tick(FPS)        

pygame.quit()
sys.exit()
