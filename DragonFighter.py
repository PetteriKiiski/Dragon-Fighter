import pygame, sys, time
from pygame.locals import *
pygame.init()
EntrySpeed = 5
#Move/second
DragonSpeed = 1.0
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
	clock = pygame.time.Clock()
	DragonTimer = time.time()
	NinjaO = 1
	NinjaDist = 200
	DragonO = 3
	while True:
		canvas.fill(255, 255, 255)
		if time.time() - DragonTimer >= 1.0/DragonSpeed:
			if NinjaO == DragonO and NinjaDist == "???":
				
		clock.tick(10)
HomePage()
#1360/2
#615
