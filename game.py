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

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True
			
pygame.quit() # required
quit() #exits python