import pygame
from SpriteSheet_Functions import SpriteSheet
from Constants import *

from Alien import Alien
from AlienExplosion import AlienExplosion
from Ship import Ship
from FlyingSaucer import FlyingSaucer
from Missile import Missile
import math

pygame.init()
pygame.key.set_repeat(10)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("test du 13 janvier")
sprite_sheet = SpriteSheet("Data/space_invaders_sprite_sheet.png")

done = False

#all_sprites_group = pygame.sprite.Group()
#all_aliens_group = pygame.sprite.Group()
#all_missile_group = pygame.sprite.Group()

newtime = pygame.time.get_ticks()

# to scale sprite
def scaleSprite(thisSprite, sprite_coord_list, scale_info):
	sprite_coord_list[2] = sprite_coord_list[2] * scale_info
	sprite_coord_list[3] = sprite_coord_list[3] * scale_info 
	thisSprite.image = pygame.transform.scale(thisSprite.image,(sprite_coord_list[2], sprite_coord_list[3]))


def placeAliensinRow(group_aliens, coordX, coordY):
	multiplicateur = 1
	for alien in group_aliens:
		#alien.rect.x = coordX * multiplicateur
		#alien.rect.y = coordY
		alien.rect.center = (coordX * multiplicateur, coordY)
		print "alien dans place aliens: ", alien
		multiplicateur = multiplicateur + 1
	print "   end row \n"

def alienRowDown():
	for alien in all_aliens_group:
		
		alien.reverseDirection()
		alien.moveVertical()
		#alien.moveBack()
		

ship = Ship(SHIP_COORD, sprite_sheet)
flyingSaucer = FlyingSaucer(FLYING_SAUCER_COORD, sprite_sheet)
for i in range(ALIENS_PER_ROW):
	all_aliens_group1.add(Alien(ALIEN1_COORD, sprite_sheet))
	all_aliens_group2.add(Alien(ALIEN2_COORD, sprite_sheet))
	all_aliens_group3.add(Alien(ALIEN3_COORD, sprite_sheet))
#	all_sprites_group.add(Alien(ALIEN1_COORD[0]))

placeAliensinRow(all_aliens_group1,35, 200)
placeAliensinRow(all_aliens_group2,35, 230)
placeAliensinRow(all_aliens_group3,35, 260)

all_aliens_group.add(all_aliens_group1)
all_aliens_group.add(all_aliens_group2)
all_aliens_group.add(all_aliens_group3)

all_sprites_group.add(ship)
all_sprites_group.add(flyingSaucer)
all_sprites_group.add(all_aliens_group)
#print "\nContent of all_aliens_group!:\n ",
#for alien in all_aliens_group:
#	print alien


while not done:

	all_sprites_group.update()

	for alien in all_aliens_group:
		if alien.isAtWall():
			#all_aliens_group.reverseDirection()
			#all_aliens_group.moveVertical()
			alienRowDown()
			break
			#continue

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		
	keys = pygame.key.get_pressed()
	if keys[pygame.K_LEFT]:
		ship.moveLeft()
	elif keys[pygame.K_RIGHT]:
		ship.moveRight()
	elif keys[pygame.K_ESCAPE]:
		done = True

	
	if keys[pygame.K_SPACE]:
		now = pygame.time.get_ticks()
		if now - ship.last_shot >= SHOT_DELAY:
			ship.last_shot = now
			miss = Missile(MISSILE_SHIP_COORD, sprite_sheet)
			miss.rect.x = ship.rect.x + SHIP_COORD[0][2]/2
			all_sprites_group.add(miss)
			all_missile_group.add(miss)
			#all_Ship_missles.append(miss)

	screen.fill(BLACK)	
	all_sprites_group.draw(screen)

			
	pygame.display.flip()
	
	#pygame.display.update()
	clock.tick(60)

#print "\nContent of all sprite group"
#for sprite in all_sprites_group:
#	print sprite
pygame.quit()