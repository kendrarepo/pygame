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

end_it=False
while (end_it==False):
    gameDisplay.fill(black)
    myfont=pygame.font.SysFont("Britannic Bold", 20)
    nlabel=myfont.render("Diag Squirrel Dodger", True, (white))
    blabel = myfont.render("Click anywhere on the screen to continue", True, (white))
    blabel_rect = blabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    nlabel_rect = nlabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 -20))
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            end_it=True
    gameDisplay.blit(nlabel,nlabel_rect)
    gameDisplay.blit(blabel,blabel_rect)
    pygame.display.flip()

entergame=False
while (entergame==False):
    gameDisplay.fill(black)
    myfont=pygame.font.SysFont("Britannic Bold", 20)
    alabel=myfont.render("Oh no! You just woke up by the Michigan Stadium after a night", True, (white))
    alabel_rect = alabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    blabel = myfont.render("you can't remember with your friends.", True, (white))
    blabel_rect = blabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+20))
    clabel = myfont.render("As a Diag squirrel, you must find your way back to the Diag ", True, (white))
    clabel_rect = clabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+40))
    dlabel=myfont.render("before you miss out on all the food.", True, (white))
    dlabel_rect = dlabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 +60))
    elabel = myfont.render("Click anywhere on the screen to continue", True, (white))
    elabel_rect = elabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 +150))
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            entergame=True
    gameDisplay.blit(alabel,alabel_rect)
    gameDisplay.blit(blabel,blabel_rect)
    gameDisplay.blit(clabel,clabel_rect)
    gameDisplay.blit(dlabel,dlabel_rect)
    gameDisplay.blit(elabel,elabel_rect)
    pygame.display.flip()

bus_x = random.randrange(0, SCREEN_WIDTH) 
bus_y = random.randrange(200, SCREEN_HEIGHT) 

pygame.mixer.music.load('cars.wav')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(loops=-1)

gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #initialize with a tuple
pygame.display.set_caption("Diag Squirrel Dodger") # title

bus_horn = pygame.mixer.Sound('carhorn.wav')

clock = pygame.time.Clock()

background_image = pygame.image.load('road.bmp')
background_image = transform.scale(background_image, (600, 600))
background_position = [0,0]

player_image = pygame.image.load('squirrel.bmp')
bluebus_image = pygame.image.load('bluebus.bmp')

lives = 3


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

		def move(self): # moves bus off the screen is collision occurs
	        x = -200
	        y = 0
	        self.rect.center = (x,y)
			

all_sprites = pygame.sprite.Group()

for number in range(2):
	b = bus()
	all_sprites.add(b)

player = player()
all_sprites.add(player)

gameExit = False
while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	all_sprites.update()
	if pygame.sprite.collide_rect(player, b):
		bus_horn.play()
		lives -= 1 # bus honks when squirrel hits it
		b.move()
	else:
		ives = lives
	if lives <= 0: 
		gameExit = True

	alabel=newfont.render(("Lives:" + str(lives)), True, (white))
	alabel_rect = alabel.get_rect(center = (520, 10))

pygame.quit() # required
quit() #exits python