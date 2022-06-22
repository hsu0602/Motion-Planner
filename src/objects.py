import pygame
from transform import AffineTransform

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, size, pos, color, vertices, config, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos

        x = config[0]
        y = config[1]
        theta = config[2]

        for i in range(len(vertices)) :
            pygame.draw.polygon(self.image, color, AffineTransform(vertices[i], (4.0,4.0), theta, (False, True), (4*x + width/12, -4*y + height - height/12)))

    def update(self):
        return 0    # no need to update


class Robot(pygame.sprite.Sprite):
    def __init__(self, size, pos, color, vertices, config, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos

        x = config[0]
        y = config[1]
        theta = config[2]

        for i in range(len(vertices)) :
            pygame.draw.polygon(self.image, color, AffineTransform(vertices[i], (4.0,4.0), theta, (False, True), (4*x + width/12, -4*y + height - height/12)))

    def update(self):
        return 0 # todo


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def update(self):

        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        
        return action
        