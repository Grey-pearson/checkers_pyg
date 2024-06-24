import pygame
BLACK = (0, 0, 0)

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, frame, width, height, scale, color = BLACK):
        image = pygame.Surface((width,height)).convert_alpha()
        image.blit(self.sheet, (0,0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image
    def list_images(self, list_of_frames, size, scale):
        sprite_frames = []
        for index in range(len(list_of_frames)):
            temp_frame = self.get_image(list_of_frames[index], size, size, scale)
            sprite_frames.append(temp_frame)
        return sprite_frames



pygame.init()

screen = pygame.display.set_mode((480,400))
pygame.display.set_caption("checkers")
clock = pygame.time.Clock()
running = True

sprite_sheet_image = pygame.image.load('CheckersSpriteSheet.png').convert_alpha()
# 22 blocks long
# 16 blocks tall
sprite_sheet = SpriteSheet(sprite_sheet_image)

frame_indexs_needed = [2,3,4,10,15,16]

test = []

for i in range(320):
    test.append(i)

frames = sprite_sheet.list_images(test, 8, 1)

# print(frames)

while running:

    screen.fill((75,150,100))

    # screen.blit(frames[4], (0,0))
    y = 0
    x = 0

    for i in range(len(frames)):
        screen.blit(frames[i],(x,y))
        # print(f'{x} , {y}')
        x += 8
        if x >= 480:
            x = 0
            y += 8
        if y >= 400:
            y = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    pygame.display.flip()
    clock.tick()
pygame.quit()