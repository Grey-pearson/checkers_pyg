import pygame
import sprite_sheet as Spritesheet

pygame.init()
DISPLAY_W, DISPLAY_H = 480, 400
screen = pygame.display.set_mode((DISPLAY_W,DISPLAY_H))
pygame.display.set_caption("checkers")
clock = pygame.time.Clock()
running = True

my_sprite_sheet = Spritesheet('CheckersSpriteSheet.png')
white_puck = [my_sprite_sheet.parse_sprite('white_puck.png')]



# sprite_sheet_image = pygame.image.load('CheckersSpriteSheet.png').convert_alpha()
# 22 blocks long
# 16 blocks tall


while running:

    screen.fill((75,150,100))

    # game code;
    screen.blit(white_puck[0], (0, DISPLAY_H - 128))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    pygame.display.flip()
    clock.tick()
pygame.quit()