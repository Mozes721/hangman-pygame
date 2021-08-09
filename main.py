import pygame, sys
import random 
import time
from constants import *
pygame.init()

clock = pygame.time.Clock()

gameDisplay=pygame.display.set_mode((h,w))

pygame.display.set_caption('Hangman')
gameDisplay.fill(BOARDER)
pygame.draw.rect(gameDisplay, WHITEBOARD, pygame.Rect(22, 20, 650, 430))

img1 = pygame.image.load('img/hang1.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    gameDisplay.blit(img1, [100, 120])	    
    pygame.display.update()
 
