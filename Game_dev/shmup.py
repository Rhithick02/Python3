import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"
import pygame
import random

# Constants
HEIGHT = 720
WIDTH = 720
FPS = 30
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(ship, (56,38))
        self.image.set_colorkey(BLACK)
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = ((360,670))
        self.speed = 0
    def update(self):
        self.speed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed = -10
        if keystate[pygame.K_RIGHT]:
            self.speed = 10
        self.rect.x+= self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH-50:
            self.rect.x = WIDTH-50
    def shoot(self):
        bullet = Bullets(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        all_bullets.add(bullet)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(meteor, (50,42))
        self.image.set_colorkey(BLACK)
        # self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, BLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(0,WIDTH-20)
        self.rect.y = random.randrange(-100,-40)
        self.speed = random.randrange(4,12)
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT+10:
            self.rect.x = random.randrange(0,WIDTH-20)
            self.rect.y = random.randrange(-100,-40)
            self.speed = random.randrange(2,8)
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(laser, (8,30))
        self.image.set_colorkey(BLACK)
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.x = x
        self.speed = 8
    def update(self):
        self.rect.y-= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Setting up screen
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("----")
clock = pygame.time.Clock()

# Locations
img = os.path.dirname("/home/rhithick/Desktop/NITT/Code/Python3/Game_dev/images/")
background = pygame.image.load(os.path.join(img, "starfield.jpg")).convert()
background_rect = background.get_rect()
ship = pygame.image.load(os.path.join(img, "playerShip2_green.png")).convert()
meteor = pygame.image.load(os.path.join(img, "meteorBrown_big1.png")).convert()
laser = pygame.image.load(os.path.join(img, "laserRed01.png")).convert()

# Sprites
all_sprites = pygame.sprite.Group()
all_oponnents = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(0,8):
    enemy = Enemy()
    all_sprites.add(enemy)
    all_oponnents.add(enemy)

# Game loop
running = True
while running:
    clock.tick(FPS)
    # Exiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    all_sprites.update()
    hits = pygame.sprite.groupcollide(all_bullets, all_oponnents, True, True)
    for hit in hits:
        enemy = Enemy()
        all_sprites.add(enemy)
        all_oponnents.add(enemy)
    hits = pygame.sprite.spritecollide(player, all_oponnents, False, pygame.sprite.collide_circle)
    if hits:
        running = False
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()