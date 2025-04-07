from random import randint
from pygame import *
font.init()

window = display.set_mode((700, 500))
display.set_caption('фон.jpg')
background = transform.scale(image.load('фон.jpg'), (700, 500))

clock = time.Clock()
FPS = 60


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x=65, size_y=65, speed=2):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speedx = speed
        self.speedy = speed
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.dir = 'left'
        speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 625:
            self.rect.y += self.speed

    def Left(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 625:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self, racket1, racket2):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            self.speedx *= -1
        if self.rect.y >= 400 or self.rect.y <= 0:
            self.speedy *= -1


font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 LOSE!!', True, (180, 0, 0))
lose2 = font1.render('Player 2 LOSE!!', True, (180, 0, 0))
finish = True
game = True
ball = Ball('мячик.png', 200, 200, 120, 130)
racket1 = Player('R3_KPKFvHgQ.png', 5, 150 , 100, 150)
racket2 = Player('R3_KPKFvHgQ (1).png', 600, 150 , 100, 150)
while game == True:
    if finish == True:
        window.blit(background, (0, 0))
        racket2.update()
        racket1.Left()
        racket1.reset()
        racket2.reset()
        ball.update(racket1,racket2)
        ball.reset()
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (200, 200))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
