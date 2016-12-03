import pygame, random, sys
from pygame import *
from pygame.locals import *
from pygame.sprite import *
from os import path
pygame.init(); # required

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

resources = path.join(path.dirname(__file__), "resources") # for opening file with media

white = (255,255,255) # global colors
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow= (255, 255, 51)

bus_x = random.randrange(0, SCREEN_WIDTH) 
bus_y = random.randrange(200, SCREEN_HEIGHT) 

#create a surface
gameDisplay = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #initialize with a tuple
pygame.display.set_caption("Diag Squirrel Dodger") # title

#clock = pygame.time.Clock()

end_it1=False
while (end_it1==False):
    screen1_image = pygame.image.load(path.join(resources, "diag.bmp")).convert()
    screen1_image = transform.scale(screen1_image, (600, 600))
    screen1_position = [0,0]
    gameDisplay.blit(screen1_image, screen1_position)
    afont=pygame.font.SysFont("Britannic Bold", 40)
    bfont=pygame.font.SysFont("Britannic Bold", 30)
    alabel=afont.render("Diag Squirrel Dodger", True, (white))
    blabel = bfont.render("Click anywhere on the screen to continue", True, (white))
    blabel_rect = blabel.get_rect(center = (SCREEN_WIDTH/2, 550))
    alabel_rect = alabel.get_rect(center = (SCREEN_WIDTH/2, 50))
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            end_it1=True
    gameDisplay.blit(alabel,alabel_rect)
    gameDisplay.blit(blabel,blabel_rect)
    pygame.display.flip()

entergame=False
while (entergame==False):
    screen2_image = pygame.image.load(path.join(resources, "stadium.bmp")).convert()
    screen2_image = transform.scale(screen2_image, (600, 600))
    screen2_position = [0,0]
    gameDisplay.blit(screen2_image, screen2_position)
    myfont=pygame.font.SysFont("Britannic Bold", 30)
    alabel=myfont.render("Oh no! You just woke up by the Michigan Stadium", True, (yellow))
    alabel_rect = alabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    blabel = myfont.render("after a night you can't remember with your friends.", True, (yellow))
    blabel_rect = blabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+20))
    clabel = myfont.render("As a Diag squirrel, you must find your way back to the Diag ", True, (yellow))
    clabel_rect = clabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+40))
    dlabel=myfont.render("before you miss out on all the food.", True, (yellow))
    dlabel_rect = dlabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 +60))
    elabel = myfont.render("Click anywhere on the screen to continue", True, (white))
    elabel_rect = elabel.get_rect(center = (SCREEN_WIDTH/2, 575))
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            entergame=True
    gameDisplay.blit(alabel,alabel_rect)
    gameDisplay.blit(blabel,blabel_rect)
    gameDisplay.blit(clabel,clabel_rect)
    gameDisplay.blit(dlabel,dlabel_rect)
    gameDisplay.blit(elabel,elabel_rect)
    pygame.display.flip()

end_it3=False
while (end_it3==False):
    screen3_image = pygame.image.load(path.join(resources, "road.bmp")).convert()
    screen3_image = transform.scale(screen3_image, (600, 600))
    screen3_position = [0,0]
    gameDisplay.blit(screen3_image, screen3_position)
    myfont=pygame.font.SysFont("Britannic Bold", 30)
    alabel=myfont.render("Use the arrow keys to avoid the Blue Busses", True, (white))
    alabel_rect = alabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-60))
    blabel = myfont.render("Click anywhere on the screen to continue", True, (white))
    blabel_rect = elabel.get_rect(center = (SCREEN_WIDTH/2, 575))
    clabel = myfont.render("You have three lives. Make it to the other", True, (white))
    clabel_rect = clabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2+40))
    dlabel=myfont.render("side of the road three times to reach the Diag!", True, (white))
    dlabel_rect = dlabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 +60))
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            end_it3=True
    gameDisplay.blit(alabel,alabel_rect)
    gameDisplay.blit(blabel,blabel_rect)
    gameDisplay.blit(clabel, clabel_rect)
    gameDisplay.blit(dlabel, dlabel_rect)
    pygame.display.flip()

pygame.mixer.music.load(path.join(resources, 'cars.wav'))
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(loops=-1)

bus_horn = pygame.mixer.Sound(path.join(resources, 'carhorn.wav'))

clock = pygame.time.Clock()

background_image = pygame.image.load(path.join(resources, "road.bmp")).convert()
background_image = transform.scale(background_image, (600, 600))
background_position = [0,0]

player_image = pygame.image.load(path.join(resources, "squirrel.bmp")).convert()
bluebus_image = pygame.image.load(path.join(resources, "bluebus.bmp")).convert()

lives = 3

class player(pygame.sprite.Sprite):
	""" Cretes a squirrel that can be moved by arrow keys"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) # Calls the sprite initializer

		self.image = pygame.image.load(path.join(resources,'squirrel.bmp')) # Creates the player image
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
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
		if self.rect.left< 0:
			self.rect.left = 0
	
class bus(pygame.sprite.Sprite):
	"""Creates bluebusses that the player must try to dodge"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(path.join(resources,'bluebus.bmp')) # Creates the bluebus image
		self.image = transform.scale(self.image, (300,75))
		self.rect = self.image.get_rect()
		self.rect.x = 600
		self.rect.y = random.randrange(0, 550)

	def update(self):
		self.rect.x -= 10
		if self.rect.left < 0:
			self.rect.x = 600
			self.rect.y = random.randrange(0, 600)

	def move(self): # moves bus off the screen if collision occurs
	        x = -200
	        y = 0
	        self.rect.center = (x,y)
			

all_sprites = pygame.sprite.Group()

for number in range(2):
	b = bus()
	all_sprites.add(b)

player = player()
all_sprites.add(player)

roads = 0 
gameExit = False
while not gameExit:
	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gameExit = True

	all_sprites.update()
	if pygame.sprite.collide_rect(player, b):
		bus_horn.play() # bus honks when squirrel hits it
		lives -= 1
		b.move()
	else:
		lives = lives
	if lives <= 0: 
		print ("Sorry, you did make it back to the Diag! :(")
		gameExit = True
	if player.rect.y < 0:
			roads += 1
			player.rect.y = SCREEN_HEIGHT - 60
	if roads is 3:
		print ("Congratulations! You made it back to the Diag!")
		gameExit = True	
		
	newfont=pygame.font.SysFont("Britannic Bold", 30)
	alabel=newfont.render(("Lives:" + str(lives)), True, (white))
	alabel_rect = alabel.get_rect(center = (520, 10))
	gameDisplay.fill(white) # redraws screen so player can move smoothly
	gameDisplay.blit(background_image, background_position)
	gameDisplay.blit(alabel,alabel_rect)
	all_sprites.draw(gameDisplay)
	pygame.display.flip()

# if game_over:
# 	myfont=pygame.font.SysFont("Britannic Bold", 20)
# 	alabel=myfont.render("Oh no! You just woke up by the Michigan Stadium after a night", True, (white))
# 	alabel_rect = alabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
# 	gameDisplay.blit(alabel,alabel_rect)
# 	for event in pygame.event.get():
# 		if event.type==MOUSEBUTTONDOWN:
# 			gameExit=True

# endgame=False
# while (endgame==False):
#  	gameDisplay.fill(black)
#  	myfont=pygame.font.SysFont("Britannic Bold", 20)
#  	alabel=myfont.render("Oh no! You just woke up by the Michigan Stadium after a night", True, (white))
#  	alabel_rect = alabel.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
#  	for event in pygame.event.get():
#  		if event.type==MOUSEBUTTONDOWN:
#  			endgame=True
#  	gameDisplay.blit(alabel,alabel_rect)

pygame.quit() # required
quit() #exits python