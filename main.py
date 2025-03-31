from random import randint
from pygame import *

window = display.set_mode((700, 500))
display.set_caption('')
background = transform.scale(image.load(''), (700, 500))

clock = time.Clock()
FPS = 60

rocket = transform.scale(image.load(''), (70, 70))
ufo = transform.scale(image.load(''), (120,70))

mixer.init()
mixer.music.load('')
mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed=7):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.dir  = 'left'
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -=self.speed
        if keys_pressed[K_d] and self.rect.x < 625:
            self.rect.x +=self.speed


finish = True
game = True
while game == True:
    if finish == True:
        window.blit(background, (0,0))
        text_score = font1.render('Счет: '+ str(score), 1, (255,255,255))
        text_lose = font1.render('Пропущено: '+ str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (10,50))
        window.blit(text_score, (10,20))     
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_w:
                hero.fire()
    display.update()
    clock.tick(FPS)
