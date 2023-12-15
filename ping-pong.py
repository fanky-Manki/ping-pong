from pygame import *
from random import randint
from time import time as timer


class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, picture, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(
            image.load(picture),
            (width, height)
        )
        self.width = width
        self.height = height
        self.speed = speed
        # создаем физическую модельку спрайта
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#! Класс игрока
class Player(GameSprite):
    # метод для управления стрелками
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - self.height - 5:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - self.height - 5:
            self.rect.y += self.speed

# размеры окна
width = 600
height = 500

# создание окна
window = display.set_mode((width, height))
display.set_caption("Ping Pong")
back = (200, 255, 255)  # цвет заливки для фона
window.fill(back)  # заливка фона



game = True  
finish = False 
clock = time.Clock()
FPS = 60
ball_x = 3
ball_y = 3


racket1 = Player('racket.png', 30, 200 , 50, 150, 4)
racket2 = Player('racket.png', 520, 200 , 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)

        racket1.update_l()
        racket2.update_r()

        ball.rect.x += ball_x
        ball.rect.y += ball_y

        racket1.reset()
        racket2.reset()
        ball.reset()
      
    display.update()
    clock.tick(FPS)


