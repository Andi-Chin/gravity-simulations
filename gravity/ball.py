import pygame
import sys
from settings import Settings

pygame.init()
pygame.font.init()
pygame.display.set_caption("ball bouncing simulation")
screen = pygame.display.set_mode([Settings.screenHeight, Settings.screenHeight])
font = pygame.font.SysFont('Comic Sans MS', 30)

iterations = 1
acceleration = 1

K = 0.001
while True:

	screen.fill(Settings.color['BLACK'])

	pygame.draw.circle(screen, Settings.color['BLUE'], [int(Settings.xCoord), int(Settings.yCoord)], Settings.size)


	Settings.yCoord += Settings.yDirection

	Settings.yDirection *= acceleration + K

#bouncing up
	if Settings.yCoord + Settings.size >= Settings.screenHeight or Settings.yCoord - Settings.size <= 0:
		Settings.yDirection *= -1
		acceleration = 0.995
		K = 0.001



#going down
	if abs(Settings.yDirection) <= 0.1 and (Settings.yDirection + Settings.size + 2 < Settings.screenHeight):
		Settings.yDirection = 0.3
		acceleration = 1.001
		K = 0.001


	textsurface = font.render(str(Settings.yDirection), False, Settings.color['WHITE'])


	screen.blit(textsurface, (0, 0))

	pygame.display.flip()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()




	iterations += 1




