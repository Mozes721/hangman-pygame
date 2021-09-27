import sys
import pygame
import random 
import time
from constants import *
pygame.init()
pygame.font.init()


gameDisplay=pygame.display.set_mode((h,w))
word = None

pygame.display.set_caption('Hangman')
gameDisplay.fill(BOARDER)
pygame.draw.rect(gameDisplay, WHITEBOARD, pygame.Rect(22, 20, 650, 430))

###text object render
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()


#game text display
def game_texts(text, x, y):
    TextSurf, TextRect = text_objects(text, txt_font)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

#button display
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    TextSurf, TextRect = text_objects(msg, btn_font)
    TextRect.center = ((x + (w/2)), (y + (h/2)))
    gameDisplay.blit(TextSurf, TextRect)


def redraw_window():
    global word
    global guesses
    global limbs
    global hangmanImgs
    
    #img of hangman
    gameDisplay.blit(hangmanImgs[limbs], [100, 120])

    #draw word
    display_word = ''
    for letter in word:
        if letter in guesses:
            display_word += letter + ' '
        else:
            display_word += '_ '
            

    TextSurf, TextRect = text_objects(display_word, guess_font)
    TextRect.center = (350, 400)
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()

def random_word():
    guessed_word = random.choice(open('words.txt').read().split()).strip()
    return guessed_word


def finished_game():
    pass

def play_again():
    pass
    
 
def exit():
    pygame.quit()


def reset():
    global limbs
    global guesses
    global word

    limbs = 0
    guesses = []
    word = random_word()


word = random_word()
inGame = True


print(word)
while inGame:
    redraw_window()
    pygame.time.delay(10)
    press=pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key in range(pygame.K_a, pygame.K_z + 1):
                if event.unicode not in word:
                    game_texts("The letter %s is not in the word" % event.unicode , 450, 230)
                    limbs += 1
                    time.sleep(3)
                    pygame.draw.rect(gameDisplay, WHITEBOARD, pygame.Rect(22, 20, 600, 230))
                if event.unicode in guesses:
                    game_texts("You already pressed it!", 450, 230)
                    time.sleep(3)
                    pygame.draw.rect(gameDisplay, WHITEBOARD, pygame.Rect(22, 20, 600, 230))
                else:
                    guesses += event.unicode
            print(guesses)
    # gameDisplay.blit(word, (200, 300))
            # button("PLAY AGAIN?", 400, 100, 150, 50, light_slat, bright_green, play)
            # button("EXIT", 400, 200, 150, 50, light_slat, dark_red, exit)

