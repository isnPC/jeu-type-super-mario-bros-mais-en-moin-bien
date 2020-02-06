import pygame
pygame.init()

class player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 5
        self.image = pygame.image.load('projet term/hero.png')
        self.rect = self.image.get_rect()

pygame.display.set_caption("projet terminal")
screen = pygame.display.set_mode((400,600))

background = pygame.image.load('projet term/backgroundpluspetit.png')

player = player()

running = True
while running:

    screen.blit(background,(-10,-198 ))

    screen.blit(player.image,player.rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
