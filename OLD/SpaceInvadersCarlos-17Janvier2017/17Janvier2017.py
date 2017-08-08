import pygame

pygame.init()

SIZE = (500,500)
BLACK = [0,0,0]
RED = [255,0,0]

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("I will rock tonight")


done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	keys = pygame.key.get_pressed()

	if keys[pygame.K_ESCAPE]:
		done = True

		#keys2 = pygame.key.get_pressed()

	screen.fill(BLACK)
	pygame.draw.rect(screen, RED, (50,50,50,50) )
	pygame.display.update()

pygame.quit()