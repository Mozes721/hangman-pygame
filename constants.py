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
wrong_guesses = []
limbs = 0
btn_font = pygame.font.SysFont("Arial", 20)
guess_font = pygame.font.SysFont("monospace", 60)
finish_font = pygame.font.SysFont('Arial', 45)
txt_font = pygame.font.SysFont('freesandbold.ttf', 32)
wrong_guesses_font = pygame.font.SysFont("Arial", 20)

#if reaches 6 limbs then its game over

hangmanImgs = [pygame.image.load('img/hang1.png'), pygame.image.load('img/hang2.png'), pygame.image.load('img/hang3.png'), pygame.image.load('img/hang4.png'), pygame.image.load('img/hang5.png'), pygame.image.load('img/hang6.png'), pygame.image.load('img/hang7.png')]

#button class
# class Button():
# 	def __init__(self, x, y, image, scale):
# 		width = image.get_width()
# 		height = image.get_height()
# 		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
# 		self.rect = self.image.get_rect()
# 		self.rect.topleft = (x, y)
# 		self.clicked = False

# 	def draw(self, surface):
# 		action = False
# 		#get mouse position
# 		pos = pygame.mouse.get_pos()

# 		#check mouseover and clicked conditions
# 		if self.rect.collidepoint(pos):
# 			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
# 				self.clicked = True
# 				action = True

# 		if pygame.mouse.get_pressed()[0] == 0:
# 			self.clicked = False

# 		#draw button on screen
# 		surface.blit(self.image, (self.rect.x, self.rect.y))

# 		return action

# #load button images
# start_img = pygame.image.load('img/start_btn.png').convert_alpha()
# exit_img = pygame.image.load('img/exit_btn.png').convert_alpha()

# #create button instances
# start_button = Button(100, 200, start_img, 0.8)
# exit_button = Button(450, 200, exit_img, 0.8)