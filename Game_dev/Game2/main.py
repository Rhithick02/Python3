import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="hide"
import pygame as pg
import random
from settings import *
from sprites import *
class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((HEIGHT,WIDTH))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.platform = pg.sprite.Group()
        self.player = Player()
        self.ground = Ground(0, 650, WIDTH, 70)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.ground)
        self.platform.add(self.ground)
        self.run()

    def run(self):
        self.play = True
        while self.play: 
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platform, False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.play = False
                self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
ob = Game()
while ob.running:
    ob.new()
pg.quit()