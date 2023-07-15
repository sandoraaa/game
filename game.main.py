import random

import pygame



#import random

pygame.init()


class Ship(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.speed=10
        self.life=5
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect(center=(x, y))
    def update(self):
        global fire

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left>-35 :
            self.rect.centerx -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right<735:
            self.rect.centerx += self.speed
        if  keys[pygame.K_SPACE] and fire:

            bul=Bullet(self.rect.centerx + 6, self.rect.centery - 40)
            bullet_group.add(bul)
            fire=False
        if spship.life==0:
            self.kill()



class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 3
        self.step = 0
        self.left = True
        self.image = pygame.image.load('enemy.png')
        self.rect = self.image.get_rect(center=(x, y))
    def update(self):
        if self.left:
            self.rect.centerx-= self.speed
            self.step += 1
        elif not self.left:
            self.rect.centerx+= self.speed
            self.step += 1
        if self.step> 20:
            self.left = not self.left
            self.step=0
        if pygame.sprite.spritecollide(self, bullet_group, True):
            self.kill()


class E_bullet(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.speed=random.randint(3,7)
        self.image=pygame.image.load('ball.png')
        self.rect = self.image.get_rect(center=(x, y))
    def update(self):
        global life
        self.rect.centery += self.speed
        if self.rect.bottom> h-50:
            self.kill()
        if pygame.sprite.spritecollide(self, spship_group, False):
            spship.life -=1
            print(spship.life)
            self.kill()



class Bullet(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.speed= 5
        self.image = pygame.image.load('bullet.png')
        self.rect = self.image.get_rect(center=(x,y))
    def update (self):
        self.rect.centery -= self.speed
        if self.rect.centery < 15:
            self.kill()
        if pygame.sprite.spritecollide(self, enemy_group, True):
            self.kill()


fire=False
t1 = pygame.time.get_ticks()


font =pygame.font.SysFont("verdana",30 , 1 ,0)


w=700
h =650

text= font.render('Game over!', True, pygame.Color("black"))
text2= font.render('You lose!', True, pygame.Color("black"))
text3= font.render('You win!', True, pygame.Color("black"))



bg=pygame.image.load('bg.jpg')
lifeimg = pygame.image.load('life.png')
size_window = (w, h)
window = pygame.display.set_mode(size_window)
pygame.display.set_caption('Game ')
state='run'
run=True

      #enemy
enemy_group = pygame.sprite.Group()
x=95
y=50
for i in range(2):
    for k in range(8):
        enemy = Enemy(x,y)
        enemy_group.add(enemy)
        x += 80
    x=95
    y+=80

      #ship
spship_group=pygame.sprite.Group()
spship=Ship(w//2,h-100)
spship_group.add(spship)


    #enemyBULLET
ebullet_group=pygame.sprite.Group()


     #bullet
bullet_group=pygame.sprite.Group()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    window.fill ('black')
    window.blit(bg,(0,0))

    enemy_group.draw(window)
    spship_group.draw(window)
    ebullet_group.draw(window)
    bullet_group.draw(window)

    lx=15
    for i in range (spship.life):
        window.blit(lifeimg, (lx, 590))
        lx+=50


    enemy_group.update()
    spship.update()
    ebullet_group.update()
    bullet_group.update()



    if len(ebullet_group)<7 and state == 'run':
        ataka=random.choice(enemy_group.sprites())
        ebullet = E_bullet(ataka.rect.centerx, ataka.rect.centery)
        ebullet_group.add(ebullet)

    t2 = pygame.time.get_ticks()
    if t2-t1>3000:
        fire=True
        t1=t2
    if spship.life == 0:
        state='lose'
        enemy_group.empty()
        spship_group.empty()
        bullet_group.empty()
        ebullet_group.empty()
        window.fill('white')
        window.blit(text, (w//2, 170))
        window.blit(text2, (w//2, 200))

    if len(enemy_group)==0 and spship.life>0 :
        state = 'win'
        enemy_group.empty()
        spship_group.empty()
        bullet_group.empty()
        ebullet_group.empty()
        window.fill('white')
        window.blit(text3, (w//2,h-200))










    #enemy_group.empty()


    pygame.time.delay(50)
    pygame.display.update()

pygame.quit()