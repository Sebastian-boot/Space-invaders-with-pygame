import os, sys
import pygame
from pygame.locals import *
import random
import math


pygame.init()
screen = pygame.display.set_mode((800, 600))


pygame.display.set_caption("Asteroids")
icon = pygame.image.load('images/asteroid.png')
pygame.display.set_icon(icon)

#player
nave = pygame.image.load('images/spaceship.png')
playerx = 350
playery = 500 #280
playerxchange = 0

#enemy 
enemyimg = pygame.image.load('images/enemy.png')
enemyx = random.randint(0, 733)
enemyy = 100
enemyxchange = 0.3
enemychange = 30

#bullet
bullet = pygame.image.load('images/bullet.png')
bulletx = 0
bullety = 520 
bulletychange = 1.5
bullet_state = "ready"


score = 0

def player (x,y):
    screen.blit(nave, (x, y))

def enemy (x,y):
    screen.blit(enemyimg, (x,y))


def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x-5, y+10))
"""
def vision (self):
    pos = pygame.mouse.get_pos()
    self.rect.midtop = pos
    if self.punching:
        self.rect.move_ip(5, 10)
"""
def isCollision(enemyx, enemyy, bulletx, bullety) :
    distance = math.sqrt((math.pow(enemyx - bulletx,2)) + (math.pow(enemyy - bullety,2)))
    if distance < 20:
        return True
    else:
        return False        

running = True
while running:
    
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxchange = -0.3
            if event.key == pygame.K_RIGHT:
                playerxchange = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready" :
                    bulletx = playerx
                    fire_bullet(bulletx,bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerxchange = 0

    #añadiendo bordes a al jugador           
    playerx = playerx + playerxchange

    if playerx <= 0:
        playerx = 0
    elif playerx >= 733:
        playerx = 733
    

    enemyx = enemyx + enemyxchange

    if enemyx <= 0:
        enemyxchange = 0.3
        enemyy = enemyy + enemychange
    elif enemyx >= 710:
        enemyxchange = -0.3
        
    #bullet movement
    if bullety <= 0:
        bullety = 520
        bullet_state = "ready"   
    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety -= bulletychange

    player(playerx,playery)
    enemy(enemyx,enemyy)
    pygame.display.update()

 #collision
    collision = isCollision(enemyx,enemyy,bulletx,bullety)
    if collision:
        bulletY = 520
        score += 1
        bullet_state = "ready" 
        print(score)

""""
if __name__ == "__main__":
    main()
"""

