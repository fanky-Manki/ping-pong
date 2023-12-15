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
score_1 = 0
score_2 = 0


racket1 = Player('racket.png', 30, 200 , 50, 150, 4)
racket2 = Player('racket.png', 520, 200 , 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 20)
lose1 = font1.render('Игрок 1 проиграл!', True, (180, 0, 0))
lose2 = font1.render('Игрок 2 проиграл!', True, (0, 0, 180))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)

        text_1 = font2.render(f'Счёт игрока 1: {score_1}', True, (0, 0, 0))
        text_2 = font2.render(f'Счёт игрока 2: {score_2}', True, (0, 0, 0))
        window.blit(text_1, (10, 10))
        window.blit(text_2, (440, 10))
        racket1.update_l()
        racket2.update_r()

        ball.rect.x += ball_x
        ball.rect.y += ball_y

        if sprite.collide_rect(racket1, ball):
            ball_x *= -1
        if sprite.collide_rect(racket2, ball):
            ball_x *= -1
        if ball.rect.y < 0 or ball.rect.y > height - 50:
            ball_y *= -1
        
        if ball.rect.x < 0:
            finish = True
            score_2 += 1
            window.blit(lose1, (200, 250))
            
        if ball.rect.x > width - 50:
            finish = True
            score_1 += 1
            window.blit(lose2, (200, 250))

        

        racket1.reset()
        racket2.reset()
        ball.reset()

    else:
        finish = False
        time.delay(3000)
        racket1 = Player('racket.png', 30, 200 , 50, 150, 4)
        racket2 = Player('racket.png', 520, 200 , 50, 150, 4)
        ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)
        ball_x = 3
        ball_y = 3
      
    display.update()
    clock.tick(FPS)


