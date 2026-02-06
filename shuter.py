#Создай собственный Шутер
from pygame import *
from random import *
font.init()
mixer.init()

font = font.Font(None, 40)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_h, player_w):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y)) 

for_1 = 0

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
            

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, -15, 15, 10)
        puli.add(bullet)

lost = 0 

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.y = 0
            self.rect.x = randint(10, 650)
            lost = lost + 1

class Bullet (GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


puli = sprite.Group()


monsters = sprite.Group()
for i in range(6):
    enemy =Enemy('ufo.png', randint(10, 380), -55, randint(1, 5), 45, 90)
    monsters.add(enemy)
            
        


player = Player('rocket.png', 100, 400, 10, 100, 55)

window = display.set_mode((900, 650))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (900, 650))
clock = time.Clock()
FPS = 60

fire = mixer.Sound('fire.ogg')


mixer.music.load('space.ogg')
#mixer.music.play(-1)



game = True
while game:
    

    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_a:
                player.fire()
                

    if finihs != True:

        window.blit(background, (0, 0))
        player.update()
        player.reset()
        monsters.update()
        puli.update()
        text_lose = font.render('Пропущено:' + str(lost), 1, (255, 255, 255))
        text_for_1 = font.render('Счет:' + str(lost), 1, (255, 255, 255))
        window.blit(text_lose, (15, 15))
        puli.draw(window)
        monsters.draw(window)
        collides_list = sprite.groupcollide(monsters, puli, True, True)
    
    clock.tick(FPS)
    display.update()
