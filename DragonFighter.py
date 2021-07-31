import pygame,  sys
from pygame.locals import *
pygame.init()
canvas = pygame.display.set_mode((1360, 660))
pygame.display.set_caption("Dragon Fighter")
Home = pygame.image.load("HomePage.png")
Play = pygame.image.load("Play.png")
def HomePage():
	while True:
		canvas.fill((255, 255, 255))
		canvas.blit(Home, (0, 0))
		canvas.blit(Play, (800, 0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if pygame.Rect(800, 0, 500, 200).collidepoint(pos):
					GamePage()
		pygame.display.update()
def GamePage():
HomePage()
