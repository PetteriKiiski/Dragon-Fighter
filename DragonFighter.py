import pygame, sys, time
from pygame.locals import *
pygame.init()
EntrySpeed = 5
#Move/second
DragonSpeed = 2.0
canvas = pygame.display.set_mode((1360, 660))
pygame.display.set_caption("Dragon Fighter")
Home = pygame.image.load("HomePage.png")
Play = pygame.image.load("Play.png")
Back = pygame.image.load("Back.png")
YouWin = pygame.image.load("YouWin.png")
YouLose = pygame.image.load("YouLose.png")
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
	DragonO = 1
	leavepage = False
	while True:
		if leavepage:
			break
		canvas.fill((255, 255, 255))
		DragonRect = pygame.Rect(0, 0, *([100, 200] if DragonO % 2 == 1 else [200, 100]))
		DragonRect.centerx = 615
		DragonRect.centery = 330
		canvas.blit(pygame.image.load("Dragon{}.png".format(DragonO)), DragonRect)
		NinjaRect = pygame.Rect(0, 0, *([100, 200] if NinjaO % 2 == 0 else [200, 100]))
		NinjaRect.centerx = DragonRect.centerx + (-1 if NinjaO == 4 else 1) * (NinjaDist if NinjaO % 2 == 0 else 0) - (200 if NinjaO == 4 else 0)
		NinjaRect.centery = DragonRect.centery + (-1 if NinjaO == 3 else 1) * (NinjaDist if NinjaO % 2 == 1 else 0) # - (200 if NinjaO == 1 else 0)
		img = pygame.image.load("Ninja{}.png".format(NinjaO))
		canvas.blit(img, NinjaRect)
		canvas.blit(Back, (0, 0))
		if abs(NinjaO - DragonO) == 2:
			if NinjaDist <= 100:
				print ("You Lose")
				canvas.blit(YouLose, (380, 255))
				pygame.display.update()
				while True:
					if leavepage:
						break
					for event in pygame.event.get():
						if event.type == QUIT:
							pygame.quit()
							sys.exit()
						if event.type == MOUSEBUTTONDOWN:
							pos = pygame.mouse.get_pos()
							if pygame.Rect(0, 0, 200, 100).collidepoint(pos):
								leavepage = True
					pygame.display.update()
		if time.time() - DragonTimer >= 1.0/DragonSpeed:
			DragonTimer = time.time()
			if NinjaO == DragonO:
				DragonO += 1 if DragonO != 4 else -3
			elif abs(NinjaO - DragonO) == 2:
				if NinjaDist <= 100:
					print ("You Lose")
					canvas.blit(YouLose, (380, 255))
					pygame.display.update()
					while True:
						if leavepage:
							break
						for event in pygame.event.get():
							if event.type == QUIT:
								pygame.quit()
								sys.exit()
							if event.type == MOUSEBUTTONDOWN:
								pos = pygame.mouse.get_pos()
								if pygame.Rect(0, 0, 200, 100).collidepoint(pos):
									leavepage = True
						pygame.display.update()
			else:
				if NinjaO == (DragonO + (1 if DragonO != 4 else -3)):
					print ("Annoying +")
					DragonO -= 1 if DragonO != 1 else -3
				else:
					DragonO += 1 if DragonO != 4 else -3
		clear = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				if pygame.Rect(0, 0, 200, 100).collidepoint(pos):
					leavepage = True
			if event.type == KEYDOWN:
				if event.key == K_LEFT:
					NinjaO -= 1 if NinjaO != 1 else -3
				if event.key == K_RIGHT:
					NinjaO += 1 if NinjaO != 4 else -3
				if event.key == K_RETURN:
					NinjaDist -= EntrySpeed
				if event.key == K_SPACE and NinjaDist <= 100:
					print ("You Win")
					canvas.blit(YouWin, (380, 255))
					pygame.display.update()
					while True:
						if leavepage:
							break
						for event in pygame.event.get():
							if event.type == QUIT:
								pygame.quit()
								sys.exit()
							if event.type == MOUSEBUTTONDOWN:
								pos = pygame.mouse.get_pos()
								if pygame.Rect(0, 0, 200, 100).collidepoint(pos):
									leavepage = True
			break
		pygame.event.clear()
		pygame.display.update()
		clock.tick(10)
HomePage()
