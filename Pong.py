import pygame
from setup import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
background_top = pygame.image.load("Images\Background_Top.png").convert()
background_bot = pygame.image.load("Images\Background_Bottom.png").convert()

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	screen.blit(background_top, BTP)
	screen.blit(background_bot, BBP)

	pygame.display.flip()
	clock.tick(60)

pygame.quit()