import pygame

#classe du projectile

class Projectile():
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image_arrow = pygame.image.load("assets/arrow.jpg")
        self.rect = self.image_arrow.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
