#!/bin/python3

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png') # load a background png 


#title and logo
pygame.display.set_caption("Spacyboiz")
icon = pygame.image.load('darkship.png')
pygame.display.set_icon(icon)

#the player
playerpic = pygame.image.load("spaceship.png")
playerx = 370
playery = 480
xchange = 0

enemypic = pygame.image.load("ufo.png")
enemyx = random.randint(0, 800)
enemyy = random.randint(50, 150)
enemyxchange = 4
enemyychange = 40


def player(x,y):
    screen.blit(playerpic, (x, y))

def enemy(x,y):
    screen.blit(enemypic, (x,y))


running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #checking if key is pressed right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xchange = -5
            if event.key == pygame.K_RIGHT:
                xchange = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                xchange = 0

    #player movement
    playerx += xchange
    
    if playerx <= 0:
        playerx = 0
    elif playerx >= 736:
        playerx = 736
    #enemy movement
    enemyx += enemyxchange

    if enemyx <= 0:
        enemyxchange = 4
        enemyy += enemyychange
    elif enemyx >= 736:
        enemyxchange = -4
        enemyy += enemyychange

    player(playerx, playery)
    enemy(enemyx, enemyy)
    pygame.display.update()
