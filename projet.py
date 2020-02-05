import pygame
pygame.init()

pygame.display.set_caption("projet terminal")
screen = pygame.display.set_mode((400,600))

background = pygame.image.load('projet term/backgroundpluspetit.png')

running = True
while running:

    screen.blit(background,(-10,-198 ))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
