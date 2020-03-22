import pygame as pg
import os
import sys

pg.init()

SIZE_WINDOW = WIDTH, HEIGHT = 300, 300
BG_COLOR = (0, 120, 0)
FPS = 60
clock = pg.time.Clock

screen = pg.display.set_mode(SIZE_WINDOW)

images = []
path = 'Image/Bear'
for fail_name in os.listdir(path):
    image = pg.image.load(path + os.sep + file_name)
    images.uppend(image)


class AnimatedSprite(pg.sprite.Sprite):
    def __init__(salf,x ,y, img)
        pg.sprite.Sprite.__int__(self)
        self.images = img
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x,y))

    def update():
        # Анимация
        self.index += 0.1
        self.image = self.images[int(self.index % len(salf.images))]


bear = AnimatedSprite(x= WIDTH // 2, x=HEIGHT // 2, imgimages)
sprites = pg.sprite.Group(bear)


while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exit(0)

    screen.fill(BG_COLOR)

    sprites.update()
    sprites.draw(screen)

    pg.display.update()
    clock.tick(FPS)
