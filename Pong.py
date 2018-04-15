import pygame
from setup import *
import math

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


class players(pygame.sprite.Sprite):

	def __init__(self, image):
		super().__init__()
		self.image = pygame.image.load(image).convert()
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.score=0




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
ball.rect.x = 345
ball.rect.y = 295
all_sprites_list.add(ball)

theta = 0

def drawBackground():
	screen.fill(WHITE)
	screen.blit(background_top, BTP)
	screen.blit(background_bot, BBP)

def drawScores():
	text = font.render(SCORE1 + str(p1.score), True, GREEN)
	screen.blit(text, [10, 10])
	text = font.render(SCORE2 + str(p2.score), True, GREEN)
	screen.blit(text, [570,10])

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	p1.rect.y = 250 + math.sin(theta)*160 #just to show animation of sprites
	p2.rect.y = 250 - math.sin(theta)*160
	drawBackground()
	drawScores()
	all_sprites_list.draw(screen)
	pygame.display.flip()
	clock.tick(60)
	theta += .01

pygame.quit()