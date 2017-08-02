import pygame

pygame.init()

SIZE = (400,400)
BLACK = [0,0,0]
GREEN = [0,255,0]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("14 juin 2017")

done = False

xVector = 2
yVector = 5

xCoord = 10
yCoord = 10

largeur = 40
hauteur = 40



while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		done = True
	
	xCoord += xVector
	yCoord += yVector
	screen.fill(BLACK)
	pygame.draw.ellipse(screen, GREEN, (xCoord, yCoord,largeur,hauteur))
	pygame.display.update()

	if xCoord > SIZE[0]:
		xCoord = SIZE[0] - largeur
		xVector = -xVector
	if yCoord > SIZE[1]:
		yCoord = SIZE[1] - hauteur
		yVector = -yVector
	if xCoord < 0:
		xCoord = 0 + largeur
		xVector = -xVector
	if yCoord < 0:
		yCoord = 0 + hauteur
		yVector = -yVector	

pygame.quit()