from pygame import *

w = 700
h = 500

main = display.set_mode((w, h))
display.set_caption("ping no ne pong")

background = transform.scale(image.load('pole_png.jpg'), (w, h))

ronaldy_chet = 0
messi_chet = 0


class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_w, player_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        main.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_1p(self):        
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y  -= self.speed
        if keys_pressed[K_s] and self.rect.y < h - 150:
            self.rect.y += self.speed
    def update_2p(self):        
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y  -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < h - 150:
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self, player_img, player_x, player_y, player_w, player_h, player_speed):
        super().__init__(player_img, player_x, player_y, player_w, player_h, player_speed)
        self.speed_y = player_speed
        self.speed_x = player_speed
        self.score_ronaldy = 0
        self.score_messi = 0
    def update(self, messi, ronaldy):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        if self.rect.x < -50:
            self.rect.x = 325
            self.rect.y = 225
            self.speed_x *= -1
            self.score_messi += 1
            self.speed_y = 10
            self.speed_x = 10
        if self.rect.x > 700:
            self.rect.x = 325
            self.rect.y = 225
            self.speed_x *= -1
            self.score_ronaldy += 1
            self.speed_y = 10
            self.speed_x = 10
        if self.rect.y < 0 or self.rect.y > 450:
            self.speed_y *= -1
        if sprite.collide_rect(self, ronaldy) or sprite.collide_rect(self, messi):
            self.speed_x *= -1
            self.speed_x *= 1.1

game = True
game_over = False

ronaldy_p1 = Player('Ronaldy_jpg.png', 20, 200, 60, 150, 6)
messi_p2 = Player('Messi_jpg.png', 640, 200, 60, 150, 6)

ball = Ball('myach_jpg.png', 325, 225, 50, 50, 10)
font.init()
font1 = font.SysFont('Calibri', 70)

font2 = font.SysFont('Calibri', 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    main.blit(background, (0, 0))
    ball.reset()
    ronaldy_p1.reset()
    messi_p2.reset()
    if not game_over:
        ronaldy_p1.update_1p()
        messi_p2.update_2p()
        ball.update(ronaldy_p1, messi_p2)
        if ball.score_messi >= 5 or ball.score_ronaldy >= 5:
            game_over = True 
    if game_over:
        if ball.score_messi > ball.score_ronaldy:
            win1 = font1.render('Win Messi', True, (0, 0, 150))
            main.blit(win1, (200, 225))
        else:
            win = font1.render('Win Ronaldy', True, (200, 0, 0))
            main.blit(win, (175, 225))
    score_ronaldy = font2.render(str(ball.score_ronaldy), True, (200, 0, 0))
    score_messi = font2.render(str(ball.score_messi), True, (0, 0, 150))
    main.blit(score_ronaldy, (300, 10))
    main.blit(score_messi, (375, 10))
    display.update()
    time.delay(40)