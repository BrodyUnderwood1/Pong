import pygame
from setup import *
import math
from random import randint
import serial


pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
background_top = pygame.image.load(BTI).convert()
background_bot = pygame.image.load(BBI).convert()

# Select the font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 25, True, False)
players_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()


#Pong ball class
class Ball(pygame.sprite.Sprite):
	
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load(BI).convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.x = 345
		self.rect.y = 295
		self.x_vel = 0
		while(self.x_vel==0):
			self.x_vel=randint(-1,1)
		self.y_vel = 0
		while(self.y_vel==0):
			self.y_vel=randint(-1,1)
	def updt(self):
		if (abs(self.x_vel)>=8):
			self.x_vel=self.x_vel
		elif (self.x_vel>0):
			self.x_vel+=.01
		else:
			self.x_vel-=.01
		self.rect.x+=self.x_vel

		
		self.rect.y+=self.y_vel

		if (self.rect.y>=502):
			self.y_vel = -self.y_vel
			self.rect.y=502
		if (self.rect.y<=88):
			self.y_vel = -self.y_vel
			self.rect.y=88

	def reset(self):
		
		self.x_vel = 0
		while(self.x_vel==0):
			self.x_vel = randint(-1,1)
		self.y_vel = 0
		#while(self.y_vel==0):
		#	self.y_vel=randint(-1,1)
		self.rect.x = 345
		self.rect.y = 295



class players(pygame.sprite.Sprite):

	def __init__(self, image):
		super().__init__()
		self.image = pygame.image.load(image).convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.score = 0
		self.y_last = 250
		self.y_vel = 0
	def getVel(self):
		self.y_vel = self.rect.y - self.y_last
		self.y_last = self.rect.y
		
			
p1 = players(P1I)
p1.rect.x = P1XP
p1.rect.y = 250
players_list.add(p1)
all_sprites_list.add(p1)
p2 = players(P2I)
p2.rect.x = P2XP
p2.rect.y = 250
players_list.add(p2)
all_sprites_list.add(p2)

ball = Ball()
all_sprites_list.add(ball)

def drawBackground():
	screen.fill(WHITE)
	screen.blit(background_top, BTP)
	screen.blit(background_bot, BBP)

def drawScores():
	text = font.render(SCORE1 + str(p1.score), True, GREEN)
	screen.blit(text, [10, 10])
	text = font.render(SCORE2 + str(p2.score), True, GREEN)
	screen.blit(text, [570,10])

def checkScore(pos):
	if (pos <= 0):
		p2.score+=1
		ball.reset()
	elif (pos >= 700):
		p1.score+=1
		ball.reset()
	else:
		return


ser1 = serial.Serial()
ser1.port = 'COM4'
ser1.timeout = None


while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	
	ser1.open()
	p1.rect.y=int(ser1.read(3))
	ser1.reset_input_buffer()
	ser1.close()
	
	p1.getVel()
	p2.getVel()
	
	ball.updt()
	checkScore(ball.rect.x)
	blocks_hit_list = pygame.sprite.spritecollide(ball, players_list, False)
	
	if(len(blocks_hit_list)==1):
		ball.x_vel = -ball.x_vel
		if(ball.rect.x <350):
			ball.rect.x = 40
		else:
			ball.rect.x = 620

		if((ball.y_vel<=8) and (ball.y_vel>=-8)):
			ball.y_vel+=blocks_hit_list[0].y_vel


	drawBackground()
	drawScores()
	all_sprites_list.draw(screen)
	pygame.display.flip()
	clock.tick(60)


pygame.quit()