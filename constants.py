import pygame
pygame.init()
w = 480
h = 700

light_slat = (119,136,153)
bright_green = (40, 100, 0)
dark_red = (255, 0, 0)
BLACK = (0,0, 0)
WHITE = (255,255,255)
WHITEBOARD = (78, 118, 53)
BOARDER = (166, 115, 52)

word = ''
guesses = []
limbs = 0
btn_font = pygame.font.SysFont("Arial", 20)
guess_font = pygame.font.SysFont("monospace", 24)
lost_font = pygame.font.SysFont('arial', 45)


#if reaches 6 limbs then its game over

hangmanImgs = [pygame.image.load('img/hang1.png'), pygame.image.load('img/hang2.png'), pygame.image.load('img/hang3.png'), pygame.image.load('img/hang4.png'), pygame.image.load('img/hang5.png'), pygame.image.load('img/hang6.png'), pygame.image.load('img/hang7.png')]
