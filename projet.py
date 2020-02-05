import pygame
pygame.init()

pygame.display.set_caption("projet terminal")
screen = pygame.display.set_mode((800,400))

background = pygame.image.load('projet term/castle.png')

running = True
while running:

    screen.blit(background,(0, 0))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
