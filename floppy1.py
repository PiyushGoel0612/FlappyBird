import pygame
import random as rd
import floppy2

pygame.init()

S_H = 600
S_W = 800
screen = pygame.display.set_mode((S_W,S_H))

bg = pygame.image.load("bg.png").convert_alpha()
p_t = pygame.image.load("p_top.png").convert_alpha()
p_base = pygame.image.load("p_base.png").convert_alpha()
brd_img = pygame.image.load("brir.png").convert_alpha()

run = True
clock = pygame.time.Clock()

current1 = pygame.time.get_ticks()
current2 = pygame.time.get_ticks()

p = [floppy2.pillars(750,300,300)]
lst = [i for i in range(200,450,20)]

brd = floppy2.bird(200,200)    

while run:

    clock.tick(28)
    screen.blit(bg,(0,0))
    screen.blit(brd_img,(brd.rect.x-12,brd.rect.y-15))

    brd.move() 

    for i in p:

        screen.blit(p_base,(i.rect.x,0))
        screen.blit(p_base,(i.rect.x,523))
        screen.blit(p_t,(i.rect_u.x-1,i.rect_u.h-20))
        screen.blit(p_t,(i.rect.x-1,i.rect.y))

        for j in range(i.rect.y+20,523,27):
            screen.blit(p_base,(i.rect.x,j))

        for k in range(i.rect_u.h-47,0,-27):
            screen.blit(p_base,(i.rect.x,k))

        i.move()

        if i.rect.x < -50:
            p.remove(i)

    if pygame.time.get_ticks() - current2 > 2000:
        k = rd.choice(lst)
        p.insert(0,floppy2.pillars(800,k,600-k))
        current2 = pygame.time.get_ticks()

    if (brd.rect.colliderect(p[len(p)-1].rect)) or (brd.rect.colliderect(p[len(p)-1].rect_u )):
        run = False
    if (brd.rect.y > 550) or (brd.rect.y < 0):
        run = False

    pygame.display.update()


pygame.quit()