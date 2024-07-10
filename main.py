import pygame, sys, time
from sprite_sheet import Spritesheet
# from settings import *

# imgs are avg all scaled by 4
# imgs are 8 px
# post scaled imgs are 32 px

DISPLAY_W, DISPLAY_H = 320, 384
RED = (80,30,36)
BLACK = (0,0,0,0)



class Game():
    def __init__(self):
        # to make assigning pieces to specific coordinates 

        pygame.init()
        
        self.screen = pygame.display.set_mode((DISPLAY_W,DISPLAY_H))
        pygame.display.set_caption("checkers")
        
        self.clock = pygame.time.Clock()
        # self.my_sprite_sheet = Spritesheet('CheckersSpriteSheet.png')
        my_sprite_sheet = Spritesheet('CheckersSpriteSheet.png')

        # you can string frames in this list format to get animnations stored in one variable
        # white_puck = [my_sprite_sheet.parse_sprite('white_puck.png')]  
        # 'pucks'
        # self.white_puck = my_sprite_sheet.parse_sprite('white_puck.png') 
        # self.black_puck = my_sprite_sheet.parse_sprite('black_puck.png')
        # squares
        self.white_square = my_sprite_sheet.parse_sprite('white_square.png')
        self.black_square = my_sprite_sheet.parse_sprite('black_square.png')
        self.red_square = my_sprite_sheet.parse_sprite('red_square.png')
        # selector
        self.selector_square = my_sprite_sheet.parse_sprite('selector.png')
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

        
        # self.selector = [self.selector_square.get_rect()]
        self.selector = self.selector_square.get_rect()
        self.plr_white = [self.white_puck.get_rect(), self.white_puck.get_rect()]
        self.plr_white[0].topleft = (self.coordinates(5,3,2))
        self.plr_white[1].topleft = (self.coordinates(3,2,1))
        # pygame.draw.rect(self.screen, BLACK, self.plr_white, 48)
        # self.screen.blit(self.white_puck, self.plr_white[0])
        # self.screen.blit(self.white_puck, self.plr_white[1])
        
    
    def hover(self):
        mouse_pos = pygame.mouse.get_pos()
        # print(mouse_pos)
        for i in range(len(self.plr_white)):
            if self.plr_white[i].collidepoint(mouse_pos):
                topleft = self.plr_white[i].topleft
                # print(topleft[0])
                self.selector.topleft = (topleft[0]-16, topleft[1]-16)
                self.screen.blit(self.selector_square, self.selector)
                # self.outline(topleft[0]/32,topleft[1]/32)
            # if self.plr_white[i].collidepoint(mouse_pos) == False:
                
            
    # easier grid placment meant for top left corner
    def coordinates(self, x, y, offset=0):
        x *= 32
        y *= 32
        calculated_coordinates = (x,y-offset)
        return(calculated_coordinates)

    def outline_board(self,x,y,w=2,h=2):
        self.screen.blit(self.selector_TL, self.coordinates(x,y))
        self.screen.blit(self.selector_TR, self.coordinates(x+w,y))
        self.screen.blit(self.selector_BL, self.coordinates(x,y+h))
        self.screen.blit(self.selector_BR, self.coordinates(x+w,y+h))

        for sides in range(1,w):
            for TopBottom in range(1,h):
                self.screen.blit(self.selector_TM, self.coordinates(x+TopBottom,y))
                self.screen.blit(self.selector_BM, self.coordinates(x+TopBottom,y+h))
                self.screen.blit(self.selector_LM, self.coordinates(x,y+sides))
                self.screen.blit(self.selector_RM, self.coordinates(x+w,y+sides))

    def create_board(self):
        self.screen.blit(self.white_square, self.coordinates(1,2))
        self.outline_board(0,1,9,9)
        for col in range(8):
            for row in range(8):
                # if (row+1) % 2 == 1 and (col+1) % 2 == 1 or (row+1) % 2 == 0 and (col+1) % 2 == 0:
                if row % 2 == 0 and col % 2 == 0 or row % 2 == 1 and col % 2 == 1:
                    self.screen.blit(self.black_square, self.coordinates(row+1,col+2))
        # to select one square
        # self.outline(2,4)


    def run(self):
        last_time = time.time()
        while True:

            last_time = time.time()
            self.screen.fill(RED)
            self.create_board()
            self.screen.blit(self.white_puck, self.plr_white[0])
            self.screen.blit(self.white_puck, self.plr_white[1])
            self.hover()
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


class Player():
    def __init__(self):
        #have to be able to use this in junction with Game
        pass
        create_pucks()
        
    def create_pucks(self):
        pass
        

if __name__ == "__main__":
    game = Game()
    game.run()