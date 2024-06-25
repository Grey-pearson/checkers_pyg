import pygame
import sprite_sheet as Spritesheet

pygame.init()

screen = pygame.display.set_mode((480,400))
pygame.display.set_caption("checkers")
clock = pygame.time.Clock()
running = True

my_sprite_sheet = Spritesheet('CheckersSpriteSheet.png')
white_puck = [my_sprite_sheet.parse]

# sprite_sheet_image = pygame.image.load('CheckersSpriteSheet.png').convert_alpha()
# 22 blocks long
# 16 blocks tall


while running:

    screen.fill((75,150,100))

    # game code;

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    pygame.display.flip()
    clock.tick()
pygame.quit()