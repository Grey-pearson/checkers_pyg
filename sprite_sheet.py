import pygame
import json

class Spritesheet:
    def __init__(self, filename):
        self.filename = filename
        self.sprite_sheet = pygame.image.load(filename).convert_alpha()
        self.meta_data = self.filename.replace('png', 'json')
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()
    
    def get_sprite(self, x, y, w, h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        return sprite

    def parse_sprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x, y, w, h = sprite['x'], sprite['y'], sprite['w'], sprite ['h']
        image = self.get_sprite(x, y, w, h)
        # scale it with meta data but idk how to do that yet
        image = pygame.transform.scale(image, ( w * sprite['scale'], h * sprite['scale']))
        return image