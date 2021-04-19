from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def update_2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

img_p = "racket.png"
img_ball = "tenis_ball.png"
img_back = "back.png"

win_width = 700
win_height = 500
display.set_caption("pinpong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

p1 = Player(img_p, 5, win_height - 100, 80, 100, 10)
p2 = Player(img_p, 5, win_height - 100, 80, 100, 10)
ball = GameSprite(img_ball, 5, win_height - 100, 80, 100, 10)

game_over=False

while not game_over:
    window.blit(background,(0,0))
    p1.update()
    p2.update()
    ball.update()
    for e in event.get():
        if e.type==QUIT:
            game_over=True
 
quit()