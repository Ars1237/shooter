from pygame  import *
from random import randint

display.set_caption('Shooter')
width = 500
height = 700

background = transform.scale(image.load('galaxy.jpg'),(700,500))
window = display.set_mode((700,500))
class GameSprite(sprite.Sprite):
 # нужно добавить еще два аргумента: ширину и длину т.к. по проекту 
 # будет много спрайтов разного размера 
#  init(self,player_image,player_x,player_y,player_speed, и еще два аргумента):
    def  init(self,player_image,player_x,player_y,player_speed,player_width,player_height):
        super().init()
        self.image = transform.scale(image.load(player_image),(80,100))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.player_width = player_width
        self.player_height = player_height
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <0:
            self.kill()


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < width - 80:
             self.rect.x += self.speed
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))       
    def fire(self):
        
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)


player = Player('rocket.png',365,180,5,100,80)
# метод должнен находится классе Player
# def fire(self):
#     pass 
lost = 0 
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        # здесь область видимости локальная, поэтому нужно сделать так чтоб переменная 
        # lost стала глобальной
        global lost
        if self.rect.y > width:
            # в функцию randint передается два аргмента: с какого числа 
            # по какое будет выбираться случайное число
            self.rect.x = randint(20,620)
            self.rect.y = 0
            lost = lost + 1

ufos = sprite.Group()

for i in range(5):
    # группу спрайтов нужно создавать вне цикла, а в самом цикле мы создаем 
    # объект и помейщаем внутрь группы при помощи функции add - добавить 
    enemy = Enemy('ufo.png',randint(5,610),0,randint(1,4))
    ufo =ufos.add(enemy)


class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y <0:
            self.kill()

bullets = sprite.Group()




run = True
finish = False
fps = 60
while run:
    sprites_list = sprite.groupcollide(ufo, bullets, True, True)
    sprites_list2 = sprite.spritecollide(player, ufo, False)
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    if not finish:
        window.blit(background,(0, 0))
        player.update()
        player.reset()
        ufo.draw(window)
        ufo.update()
        bullets.update()
        bullets.draw(window)                
    
        for c in sprites_list:
            points +=1
            enemy = Enemy('ufo.png',randint(5,610),0,randint(1,4))
            ufo =ufos.add(enemy)


           # не отрисовываешь спрайты: ракету и врагов
           # если посмотришь в класс GameSprite найдешь метод reset(), 
           # который служит для отприсовки спрайтов
           # также здесь нужно вызвать метод для управления игроком и врагом
           # метод называется update()
    display.update()
    clock.tick(fps)