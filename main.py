import pygame
from sprite_sheet import Spritesheet

pygame.init()
DISPLAY_W, DISPLAY_H = 320, 340
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
white_square = my_sprite_sheet.parse_sprite('white_square.png')
black_square = my_sprite_sheet.parse_sprite('black_square.png')
red_square = my_sprite_sheet.parse_sprite('red_square.png')
selector_TL = my_sprite_sheet.parse_sprite('selector_TL.png')
selector_TM = my_sprite_sheet.parse_sprite('selector_TM.png')
selector_TR = my_sprite_sheet.parse_sprite('selector_TR.png')
selector_LM = my_sprite_sheet.parse_sprite('selector_LM.png')
selector_RM = my_sprite_sheet.parse_sprite('selector_RM.png')
selector_BL = my_sprite_sheet.parse_sprite('selector_BL.png')
selector_BM = my_sprite_sheet.parse_sprite('selector_BM.png')
selector_BR = my_sprite_sheet.parse_sprite('selector_BR.png')
white_to_play = my_sprite_sheet.parse_sprite('white_to_play.png')
black_to_play = my_sprite_sheet.parse_sprite('black_to_play.png')

while running:

    screen.fill((75,150,100))

    # game code;
    screen.blit(white_square, (32, 0))
    screen.blit(black_square, (0, 0))
    screen.blit(white_puck, (0, 0))
    screen.blit(black_puck, (32, 0))
    screen.blit(red_square, (32*2, 0))

    screen.blit(white_square, (32*3, 0))
    screen.blit(black_square, (32*4, 0))
    screen.blit(white_square, (32*5, 0))
    screen.blit(black_square, (32*3, 32))
    screen.blit(white_square, (32*4, 32))
    screen.blit(black_square, (32*5, 32))
    screen.blit(white_square, (32*3, 32*2))
    screen.blit(black_square, (32*4, 32*2))
    screen.blit(white_square, (32*5, 32*2))

    screen.blit(black_puck, (32*4, 32))

    screen.blit(selector_TL, (32*3, 0))
    screen.blit(selector_TM, (32*4, 0))
    screen.blit(selector_TR, (32*5, 0))
    screen.blit(selector_LM, (32*3, 32))
    screen.blit(selector_RM, (32*5, 32))
    screen.blit(selector_BL, (32*3, 32*2))
    screen.blit(selector_BM, (32*4, 32*2))
    screen.blit(selector_BR, (32*5, 32*2))


    screen.blit(white_to_play, (32*1, 32*4))
    screen.blit(black_to_play, (32*1, 32*6))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    pygame.display.flip()
    clock.tick()
pygame.quit()