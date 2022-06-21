import pygame

class Robot(pygame.sprite.Sprite):
    def __init__(self, size, pos, color, vertices):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        
        pygame.draw.polygon(self.image, color, vertices)

    def update(self):
        self.rect.x += 1
        self.rect.y += 1



class Obstacle(pygame.sprite.Sprite):
    def __init__(self, size, pos, color, vertices):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size, pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.center = pos

        pygame.draw.polygon(self.image, color, vertices)

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += 2
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= 2
        if key_pressed[pygame.K_UP]:
            self.rect.y -= 2
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += 2      
    