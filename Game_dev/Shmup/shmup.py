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

font_name = pygame.font.match_font('arial')
def draw_lives(surf, x, y):
    for i in range(player.lives):
        img_rect = ship_mini.get_rect()
        img_rect.center = (x + i*30, y)
        surf.blit(ship_mini, img_rect)
def draw_text(text, surf, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surf, text_rect)
def draw_shield(val, x, y, surf):
    if val > 100:
        val = 100
    if val < 0:
        val = 0
    outline = pygame.Rect(x, y, 100, 20)
    status = pygame.Rect(x, y, val, 20)
    if val >= 30:
        pygame.draw.rect(surf, GREEN, status)
    else:
        pygame.draw.rect(surf, RED, status)
    pygame.draw.rect(surf, WHITE, outline, 2)
def gameover():
    screen.blit(background, background_rect)
    draw_text("SHOOT 'EM UP", screen, 64, WIDTH / 2, 200)
    draw_text("Move left < | Move right >", screen, 30, WIDTH / 2, 400)
    draw_text("Space bar to shoot", screen, 30, WIDTH / 2, 500)
    draw_text("Press a key to start your space ride", screen, 30, WIDTH / 2, 600)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(ship, (56,38))
        self.image.set_colorkey(BLACK)
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.radius = 23
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.center = (360, 670)
        self.speed = 0
        self.buf = 10
        self.shield = 100
        self.lives = 3
        self.hidden = False
        self.p = False
    def update(self):
        if self.p and pygame.time.get_ticks() - self.ptime > 10000:
            self.hidden = False
            self.buf = 10
        if self.hidden and pygame.time.get_ticks() - self.hidden_time > 1000:
            self.hidden = False
            self.rect.center = (360, 670)
        self.speed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed = -self.buf
        if keystate[pygame.K_RIGHT]:
            self.speed = self.buf
        self.rect.x+= self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WIDTH-50:
            self.rect.x = WIDTH-50
    def shoot(self):
        shoot_sound.play()
        bullet = Bullets(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        all_bullets.add(bullet)
    def hide(self):
        self.hidden = True
        self.hidden_time = pygame.time.get_ticks()
        self.rect.center = (360, -10000)
    def pspeed(self):
        self.p = True
        self.ptime = pygame.time.get_ticks()
        self.buf = 16
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        num = random.randrange(0,4)
        self.image_org = meteor_img[num]#pygame.transform.scale(meteor, (50,42))
        self.image_org.set_colorkey(BLACK)
        self.image = self.image_org
        # self.image.fill(RED)
        self.rect = self.image_org.get_rect()
        self.radius = radius_lvl[num]
        # self.radius = 20
        # pygame.draw.circle(self.image, BLUE, self.rect.center, self.radius)
        self.rect.x = random.randrange(0,WIDTH-40)
        self.rect.y = random.randrange(-100,-40)
        self.speed = random.randrange(4,12)
        self.rot = 0
        self.rot_speed = random.randrange(-8,8)
        self.last_update = pygame.time.get_ticks()
        self.cur = pygame.time.get_ticks()
        self.const = 0
    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_org, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
    def update(self):
        self.rotate()
        self.rect.y += self.speed
        now = pygame.time.get_ticks()
        if now - self.cur >= 20000 and self.const <= 10:
                self.cur = now
                self.const += 2
        if self.rect.y > HEIGHT+10:
            self.rect.x = random.randrange(0,WIDTH-20)
            self.rect.y = random.randrange(-100,-40)
            self.speed = random.randrange(2+self.const,8+self.const)
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(laser, (8,30))
        self.image.set_colorkey(BLACK)
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.x = x
        self.speed = 10
    def update(self):
        self.rect.y-= self.speed
        if self.rect.bottom < 0:
            self.kill()
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.frame_rate = 50
        self.size = size
        self.frame = 0
        self.image = expl[size][self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.ti = pygame.time.get_ticks()
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.ti > self.frame:
            self.ti = now
            self.frame += 1
            if self.frame == len(expl):
                self.kill()
            else:
                center = self.rect.center
                self.image = expl[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
class Power_up(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['health', 'speed'])
        self.image = pup[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speed = 5
    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

# Setting up screen
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("SHMUP!")
clock = pygame.time.Clock()

# Graphics
img = os.path.dirname(os.path.realpath(__file__))
img = os.path.join(img, 'images')
background = pygame.image.load(os.path.join(img, "starfield.jpg")).convert()
background_rect = background.get_rect()
ship = pygame.image.load(os.path.join(img, "playerShip2_green.png")).convert()
ship_mini = pygame.transform.scale(ship, (30, 20))
ship_mini.set_colorkey(BLACK)
meteor_img = []
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 
                'meteorBrown_small1.png', 'meteorBrown_tiny1.png']
for imge in meteor_list:
    meteor_img.append(pygame.image.load(os.path.join(img, imge)).convert())
radius_lvl = [20, 16, 10, 5]
laser = pygame.image.load(os.path.join(img, "laserRed01.png")).convert()
expl = {}
expl['lg'] = []
expl['sm'] = []
for i in range(9):
    name = 'regularExplosion0'+str(i)+'.png'
    te_img = pygame.image.load(os.path.join(img, name)).convert()
    te_img.set_colorkey(BLACK)
    nw_img1 = pygame.transform.scale(te_img, (75, 75))
    nw_img2 = pygame.transform.scale(te_img, (32, 32))
    expl['lg'].append(nw_img1)
    expl['sm'].append(nw_img2)
pup = {}
pup['health'] = pygame.image.load(os.path.join(img, 'pill_green.png')).convert()
pup['speed'] = pygame.image.load(os.path.join(img, 'bolt_gold.png')).convert()
#Sound 
snd = os.path.dirname(os.path.realpath(__file__))
snd = os.path.join(snd, 'Sound_Effects')
shoot_sound = pygame.mixer.Sound(os.path.join(snd, "sfx_laser1.ogg"))
pygame.mixer.music.load(os.path.join(snd, "tgfcoder-FrozenJam-SeamlessLoop.ogg"))


# Sprites
all_sprites = pygame.sprite.Group()
all_oponnents = pygame.sprite.Group()
all_bullets = pygame.sprite.Group()
all_pups = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(0,8):
    enemy = Enemy()
    all_sprites.add(enemy)
    all_oponnents.add(enemy)
score = 0

pygame.mixer.music.play(loops = -1)
# Game loop
game_over = True
running = True
while running:
    clock.tick(FPS)
    if game_over:
        gameover()
        game_over = False
        all_sprites = pygame.sprite.Group()
        all_oponnents = pygame.sprite.Group()
        all_bullets = pygame.sprite.Group()
        all_pups = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(0,8):
            enemy = Enemy()
            all_sprites.add(enemy)
            all_oponnents.add(enemy)
        score = 0
    # Exiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    all_sprites.update()
    # Bullets and meteor
    hits = pygame.sprite.groupcollide(all_oponnents, all_bullets, True, True)
    for hit in hits:
        ran = random.randrange(20)
        score += 50 - hit.radius
        exp_l = Explosion(hit.rect.center, 'lg')
        all_sprites.add(exp_l)
        if ran == 1:
            power = Power_up(hit.rect.center)
            all_sprites.add(power)
            all_pups.add(power)
        enemy = Enemy()
        all_sprites.add(enemy)
        all_oponnents.add(enemy)
    # Ship and meteor
    hits = pygame.sprite.spritecollide(player, all_oponnents, True, pygame.sprite.collide_circle)
    for hit in hits:
        enemy = Enemy()
        exp_s = Explosion(hit.rect.center,'sm')
        all_sprites.add(exp_s)
        all_sprites.add(enemy)
        all_oponnents.add(enemy)
        player.shield -= 2*hit.radius
        if player.shield <=0:
            player.hide()
            player.lives -= 1
            player.shield = 100
            if player.lives == 0:
                screen.blit(background, background_rect)
                draw_text("GAME OVER", screen, 30, WIDTH / 2, 300)
                draw_text("SCORE : " + str(score), screen, 25, WIDTH / 2, 330)
                pygame.display.flip()
                wait  = True
                while wait:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                        elif event.type == pygame.KEYDOWN:
                            wait = False
                game_over = True
    # Ship and powerup
    hits = pygame.sprite.spritecollide(player, all_pups, True)
    for hit in hits:
        if hit.type == "health":
            player.shield += 50
        if hit.type == "speed":
            player.pspeed()
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    buf1 = "Score: " + str(score)
    draw_text(buf1, screen, 18, WIDTH/2, 10)
    draw_shield(player.shield, 50, 30, screen)
    draw_lives(screen, 630, 20)
    pygame.display.flip()
pygame.quit()