import pygame
from setup import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
background_top = pygame.image.load(BTI).convert()
background_bot = pygame.image.load(BBI).convert()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.blit(background_top, BTP)
	screen.blit(background_bot, BBP)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()