import pygame
import random as rd

class pillars:

    def __init__(self,x,y,h):
        self.rect = pygame.Rect(x,y,50,h)
        m = rd.choice([140,150,160,130,120])
        self.rect_u = pygame.Rect(x,0,50,y-m)

    def move(self):
        dx = 4
        self.rect.x -= dx
        self.rect_u.x -= dx

class bird:

    def __init__(self,x,y):
        self.rect = pygame.Rect(x,y,25,25)
        self.velocity = 0
        self.tmr = 0

    def move(self):
        acn = 4

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.velocity < 0:
                        self.velocity = 12
                    else:
                        self.velocity += 10
            
        self.rect.y -= self.velocity - acn
        self.tmr += 1
        
        if self.tmr % 3 == 0:
            self.velocity -= 1