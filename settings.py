import pygame, sys, time
from sprite_sheet import Spritesheet
from settings import *

my_sprite_sheet = Spritesheet('CheckersSpriteSheet.png')

DISPLAY_W, DISPLAY_H = 320, 340

# you can string frames in this list format to get animnations stored in one variable
# white_puck = [my_sprite_sheet.parse_sprite('white_puck.png')]  
# 'pucks'
white_puck = my_sprite_sheet.parse_sprite('white_puck.png') 
black_puck = my_sprite_sheet.parse_sprite('black_puck.png')
# squares
white_square = my_sprite_sheet.parse_sprite('white_square.png')
black_square = my_sprite_sheet.parse_sprite('black_square.png')
red_square = my_sprite_sheet.parse_sprite('red_square.png')
# selector
selector_TL = my_sprite_sheet.parse_sprite('selector_TL.png')
selector_TM = my_sprite_sheet.parse_sprite('selector_TM.png')
selector_TR = my_sprite_sheet.parse_sprite('selector_TR.png')
selector_LM = my_sprite_sheet.parse_sprite('selector_LM.png')
selector_RM = my_sprite_sheet.parse_sprite('selector_RM.png')
selector_BL = my_sprite_sheet.parse_sprite('selector_BL.png')
selector_BM = my_sprite_sheet.parse_sprite('selector_BM.png')
selector_BR = my_sprite_sheet.parse_sprite('selector_BR.png')
# text
white_to_play = my_sprite_sheet.parse_sprite('white_to_play.png')
black_to_play = my_sprite_sheet.parse_sprite('black_to_play.png')