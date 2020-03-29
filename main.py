import pygame as pg
import os
import sys

# слава Украие!!!

pg.init()

SIZE_WINDOW = WIDTH, HEIGHT = 500, 500
BG_COLOR = (0, 120, 0)
FPS = 60
clock = pg.time.Clock

screen = pg.display.set_mode(SIZE_WINDOW)

BG = pg.image.load('Image/stars.jpg')

images1 = []
path = 'Image/Bear'
for fail_name in os.listdir(path):
    image = pg.image.load(path + os.sep + file_name)
    images1.uppend(image)

images2 = []
image = pg.image.load('Imaage/1.png')
images2.append(image)

class AnimatedSprite(pg.sprite.Sprite):
    def __init__(salf,x ,y, img)
        pg.sprite.Sprite.__int__(self)
        self.images = img
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(x,y))
        if self is bear:
            self.rect.x += 1


    def update():
        # Анимация
        self.index += 0.1
         self.image = self.images [int(self.index % len(salf.images1))]
        self.rect = self.image.get_rect(center-self.rect.center)

bear = AnimatedSprite(x= WIDTH // 2, x=HEIGHT // 2, imgimages1)
cet = AnimatedSprite(x= WIDTH // 2, x=HEIGHT // 2, imgimages2)
sprites = pg.sprite.Group(bear, cat)
sprates.remove(cat) # спрятатся
sprites.add(cat) # показатся
bearW, bearH = bear.image.get_width(), bear.image.get_height()
catW, catH = cat.image.get_width(), cat.image.get_height()
K - bearH * 0.16

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            sys.exiG_COLOR(0)

    cat.rect.y = bear.rect.y - catH
    cat.rect.y =  bear.rect.center[0] - cat // 2

    if bear.rect.x > WIDTH:
        bear.rect.x = - bearW
    screen.blit(BG, (0, ))

    sprites.update()
    sprites.draw(screen)

    pg.display.update()
    clock.tikc FPS
