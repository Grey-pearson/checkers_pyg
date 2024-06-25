import pygame
from sprite_sheet import Spritesheet

pygame.init()
DISPLAY_W, DISPLAY_H = 480, 400
screen = pygame.display.set_mode((DISPLAY_W,DISPLAY_H))
pygame.display.set_caption("checkers")
clock = pygame.time.Clock()
running = True

my_sprite_sheet = Spritesheet('CheckersSpriteSheet.png')

# you can string frames in this list format to get animnations stored in one variable
# white_puck = [my_sprite_sheet.parse_sprite('white_puck.png')]  

# you can do one not in a list for single imgs tho
white_puck = my_sprite_sheet.parse_sprite('white_puck.png') 
black_puck = my_sprite_sheet.parse_sprite('black_puck.png')

while running:

    screen.fill((75,150,100))

    # game code;
    screen.blit(white_puck, (0, DISPLAY_H - 128))
    screen.blit(black_puck, (50, DISPLAY_H - 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    pygame.display.flip()
    clock.tick()
pygame.quit()