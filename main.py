import pygame, sys, time
from sprite_sheet import Spritesheet
from settings import *

my_sprite_sheet = Spritesheet('CheckersSpriteSheet.png')

class Game():
    def __init__(self):
        # to make assigning pieces to specific coordinates 

        pygame.init()
        
        self.screen = pygame.display.set_mode((DISPLAY_W,DISPLAY_H))
        pygame.display.set_caption("checkers")
        self.clock = pygame.time.Clock()
        running = True



        def coordinates(self, x, y):
            x *= 32
            y *= 32
            calculated_coordinates = (x,y)
            return(calculated_coordinates)

        def create_board(self):
            pass


    def run(self):
        last_time = time.time()
        while True:

            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # updating game
            self.all_sprites.update(dt)
            self.player.player_constraint()

            self.display_surface.blit(self.background, (0, 0))
            # this is needed to draw sprite to screen frfr
            self.all_sprites.draw(self.display_surface)
            # update window
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
