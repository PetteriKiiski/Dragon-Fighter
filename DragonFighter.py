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
	NinjaDist = 500
	DragonO = 3
	while True:
		canvas.fill((255, 255, 255))
		DragonRect = pygame.Rect(0, 0, *([100, 200] if DragonO % 2 == 1 else [200, 100]))
		DragonRect.centerx = 615
		DragonRect.centery = 330
		canvas.blit(pygame.image.load("Dragon{}.png".format(DragonO)), DragonRect)
		NinjaRect = pygame.Rect(DragonRect.centerx + (-1 if NinjaO == 2 else 1) * (NinjaDist if NinjaO % 2 == 0 else 0), DragonRect.centery + (-1 if NinjaO == 3 else 1) * (NinjaDist if NinjaO % 2 == 1 else 0), *([100, 200] if NinjaO % 2 == 1 else [200, 100]))
		canvas.blit(pygame.image.load("Ninja{}.png".format(NinjaO)), NinjaRect)
		if time.time() - DragonTimer >= 1.0/DragonSpeed:
			if NinjaO == DragonO and NinjaDist <= 100:
				print ("You Lose")
				for event in pygame.event.get():
					if event.type == QUIT:
						pygame.quit()
						sys.exit()
			elif abs(NinjaO - DragonO) == 2:
				DragonO += 1 if DragonO != 4 else 0
			else:
				if NinjaO == (DragonO + 1):
					DragonO += 1 if DragonO != 4 else 0
				else:
					DragonO -= 1 if DragonO != 0 else 4
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == K_DOWN:
				if event.key == K_LEFT:
					NinjaO -= 1 if NinjaO != 0 else 4
				if event.key == K_RIGHT:
					NinjaO += 1 if NinjaO != 4 else 0
				if event.key == K_RETURN:
					NinjaDist -= EntrySpeed
				if event.key == K_SPACE and NinjaDist <= 100:
					print ("You Lose")
					for event in pygame.event.get():
						if event.type == QUIT:
							pygame.quit()
							sys.exit()
		pygame.display.update()
		clock.tick(10)
HomePage()
