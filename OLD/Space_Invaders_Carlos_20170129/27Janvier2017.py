import pygame

pygame.init()

SIZE = (500,500)
BLACK = [0,0,0]
GREEN = [0,255,0]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("pratique 27 Janvier")

done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		
	keys = pygame.key.get_pressed()
	if keys[pygame.K_ESCAPE]:
		done = True

	screen.fill((0,0,0))
	pygame.draw.rect(screen, GREEN, (50,50,50,50))
	pygame.display.update()

pygame.quit()