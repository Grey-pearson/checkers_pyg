import pygame, sys, time
from sprite_sheet import Spritesheet
# from settings import *

DISPLAY_W, DISPLAY_H = 320, 384
RED = (100,40,46)


class Game():
    def __init__(self):
        # to make assigning pieces to specific coordinates 

        pygame.init()
        
        self.screen = pygame.display.set_mode((DISPLAY_W,DISPLAY_H))
        pygame.display.set_caption("checkers")
        self.screen.fill(RED)
        self.clock = pygame.time.Clock()
        # self.my_sprite_sheet = Spritesheet('CheckersSpriteSheet.png')
        my_sprite_sheet = Spritesheet('CheckersSpriteSheet.png')

        # you can string frames in this list format to get animnations stored in one variable
        # white_puck = [my_sprite_sheet.parse_sprite('white_puck.png')]  
        # 'pucks'
        self.white_puck = my_sprite_sheet.parse_sprite('white_puck.png') 
        self.black_puck = my_sprite_sheet.parse_sprite('black_puck.png')
        # squares
        self.white_square = my_sprite_sheet.parse_sprite('white_square.png')
        self.black_square = my_sprite_sheet.parse_sprite('black_square.png')
        self.red_square = my_sprite_sheet.parse_sprite('red_square.png')
        # selector
        self.selector_TL = my_sprite_sheet.parse_sprite('selector_TL.png')
        self.selector_TM = my_sprite_sheet.parse_sprite('selector_TM.png')
        self.selector_TR = my_sprite_sheet.parse_sprite('selector_TR.png')
        self.selector_LM = my_sprite_sheet.parse_sprite('selector_LM.png')
        self.selector_RM = my_sprite_sheet.parse_sprite('selector_RM.png')
        self.selector_BL = my_sprite_sheet.parse_sprite('selector_BL.png')
        self.selector_BM = my_sprite_sheet.parse_sprite('selector_BM.png')
        self.selector_BR = my_sprite_sheet.parse_sprite('selector_BR.png')
        # text
        self.white_to_play = my_sprite_sheet.parse_sprite('white_to_play.png')
        self.black_to_play = my_sprite_sheet.parse_sprite('black_to_play.png')

        self.create_board()

    def coordinates(self, x, y):
        x *= 32
        y *= 32
        calculated_coordinates = (x,y)
        return(calculated_coordinates)

    def outline(self,x,y,w,h):
        self.screen.blit(self.selector_TL, self.coordinates(x,y))
        self.screen.blit(self.selector_TR, self.coordinates(x,y))
        self.screen.blit(self.selector_TL, self.coordinates(x,y))
        self.screen.blit(self.selector_TL, self.coordinates(x,y))

    def create_board(self):
        self.screen.blit(self.white_square, self.coordinates(1,2))
        self.outline(0,1,1,1)
        for col in range(8):
            for row in range(8):
                # if (row+1) % 2 == 1 and (col+1) % 2 == 1 or (row+1) % 2 == 0 and (col+1) % 2 == 0:
                if row % 2 == 0 and col % 2 == 0 or row % 2 == 1 and col % 2 == 1:
                    self.screen.blit(self.black_square, self.coordinates(row+1,col+2))


    def run(self):
        last_time = time.time()
        while True:

            # delta time
            # dt = time.time() - last_time
            last_time = time.time()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # updating game
            # self.all_sprites.update(dt)
            # self.player.player_constraint()

            # self.display_surface.blit(self.background, (0, 0))
            # this is needed to draw sprite to screen frfr
            # self.all_sprites.draw(self.display_surface)
            # update window
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()