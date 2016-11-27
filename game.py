import pygame, random, sys
from pygame import *
from pygame.locals import *
from pygame.sprite import *
pygame.init(); # required

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

white = (255,255,255) # global colors
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #initialize with a tuple
pygame.display.set_caption("Diag Squirrel Dodger") # title

class player(pygame.sprite.Sprite):
	""" Cretes a squirrel that can be moved by arrow keys"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) # Calls the sprite initializer

		self.image = pygame.image.load('squirrel.bmp') # Creates the player image
		self.image = transform.scale(self.image, (60, 60))
		self.rect = self.image.get_rect()
		self.rect.centerx = SCREEN_WIDTH/2
		self.rect.y = SCREEN_HEIGHT-60

		def update(self): 
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			self.rect.x += 6
		if keys[pygame.K_LEFT]:
			self.rect.x -= 6
		if keys[pygame.K_UP]:
			self.rect.y -= 6
		if keys[pygame.K_DOWN]:
			self.rect.y += 6

		def update(self):
		self.rect.y += 10
		if self.rect.top > SCREEN_HEIGHT + 10:
			self.rect.x = random.randrange(0, SCREEN_WIDTH-60)
			self.rect.y = 0

class bus(pygame.sprite.Sprite):
	"""Creates bluebusses that the player must try to dodge"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('bluebus.bmp') # Creates the bluebus image
		self.image = transform.scale(self.image, (75,250))
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(0, SCREEN_WIDTH-60)
		self.rect.y = 0


gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

pygame.quit() # required
quit() #exits python