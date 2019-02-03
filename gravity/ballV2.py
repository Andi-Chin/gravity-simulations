import pygame
import sys
import time

pygame.init()
pygame.font.init()
pygame.display.set_caption("bouncing ball version 2")
screen = pygame.display.set_mode([1200, 800])
font = pygame.font.SysFont('Comic Sans MS', 30)

color = {
	'BLACK': (0, 0, 0),
	'WHITE': (255, 255, 255),
	'RED': (255, 0, 0),
	'GREEN': (0, 255, 0),
	'BLUE': (0, 0, 255)
}

dy = 0
gravity = -0.15
yCoord = 0

while True:
	screen.fill(color["BLACK"])
	pygame.draw.circle(screen, color['BLUE'], [100, round(yCoord)], 50)

	dy -= gravity

	yCoord += dy

	if yCoord + 50 >= 800:
		dy *= -1

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()


	time.sleep(0.005)



