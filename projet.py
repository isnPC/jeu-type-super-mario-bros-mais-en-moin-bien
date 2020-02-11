import pygame
pygame.init()

class Game() :
    def __init__(self):
        self.player = player()
        self.pressed = {}


class player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 10
        self.hauteurdesaut = 25
        self.image = pygame.image.load('projet term/hero.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 558

    def move_right(self):
        self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity
    def move_saut(self):
        self.rect.y += self.hauteurdesaut
        pygame.time.delay(400)
        self.rect.y -= self.hauteurdesaut
        pygame.display.update()


pygame.display.set_caption("projet terminal")

screen = pygame.display.set_mode((400,600))

background = pygame.image.load('projet term/backgroundpluspetit.png')

game = Game()

player = player()

running = True
while running:

    screen.blit(background,(-10,-198 ))

    screen.blit(game.player.image,game.player.rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.player.move_right()
            elif event.key == pygame.K_LEFT:
                game.player.move_left()
            elif event.key == pygame.K_SPACE:
                game.player.move_saut()

