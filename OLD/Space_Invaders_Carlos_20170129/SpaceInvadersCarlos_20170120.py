import pygame
from SpriteSheet_Functions import SpriteSheet
from Constants import *

from Alien import Alien
from AlienExplosion import AlienExplosion
from Ship import Ship
from FlyingSaucer import FlyingSaucer
from Missile import Missile
from ShieldBase import ShieldBase
from Sounds import *
import math

pygame.init()
pygame.key.set_repeat(10)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("test du 13 janvier")
sprite_sheet = SpriteSheet("Data/space_invaders_sprite_sheet.png")
counterSound = 0

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
		#print "alien dans place aliens: ", alien
		multiplicateur = multiplicateur + 1
	#print "   end row \n"

def placeShieldBase(group_shieldBase, coordY):
	division = SIZE[1]/4
	for shieldBase in group_shieldBase:
		shieldBase.rect.center = (division, coordY)
		division = division + SIZE[1]/4

def placeBlocksForShieldBase(coordX, coordY,sizeX, sizeY):
	proportionY = int ((sizeY * 2)/7)
	proportionX = int ((sizeX *1)/4)
	begin = True
	end = False
	print proportionY

	for i in range(coordX, coordX + sizeX ,1):
		for j in range(coordY, coordY + sizeY,1):
			if (j<(coordY + proportionY) and i < (coordX +proportionX)):
				print i,j
				#proportionX = proportionX -1
				continue
			else:
				shield_tmp = ShieldBase()
				shield_tmp.rect.center = (i,j)
				all_blockShields_group.add(shield_tmp)

			#if (i > (sizeX - proportionX) and j <(coordY + proportionY)):
			#	continue

		proportionY = proportionY -1
		#if (i > (sizeX - proportionX)):
		#	proportionY = int ((sizeY * 2)/7)

			#shield_tmp = ShieldBase()
			#shield_tmp.rect.center = (i,j)
			#all_blockShields_group.add(shield_tmp)
	print "fin block for shiled base"




def alienRowDown():

	for alien in all_aliens_group:
		#alien.speedLimitChangeImage = alien.speedLimitChangeImage -30
		alien.reverseDirection()
		alien.moveVertical()
		#alien.moveBack()

def switchSound():
	global counterSound
	sound = invaders_sounds[counterSound]
	if counterSound > len(invaders_sounds):
		counterSound = 0
	counterSound = counterSound + 1
	return sound
		

ship = Ship(SHIP_COORD, sprite_sheet)
flyingSaucer = FlyingSaucer(FLYING_SAUCER_COORD, sprite_sheet)

#for i in range(3):
#	all_shieldBases_group.add(ShieldBase(SHIELD_BASE_COORD, sprite_sheet))
#shieldBase = ShieldBase(SHIELD_BASE_COORD, sprite_sheet)

for i in range(ALIENS_PER_ROW):
	all_aliens_group1.add(Alien(ALIEN1_COORD, sprite_sheet))
	all_aliens_group2.add(Alien(ALIEN2_COORD, sprite_sheet))
	all_aliens_group3.add(Alien(ALIEN3_COORD, sprite_sheet))
#	all_sprites_group.add(Alien(ALIEN1_COORD[0]))

placeAliensinRow(all_aliens_group1,35, 200)
placeAliensinRow(all_aliens_group2,35, 230)
placeAliensinRow(all_aliens_group3,35, 260)

placeShieldBase(all_shieldBases_group,435)
placeBlocksForShieldBase(120, 420,46,34)
#placeBlocksForShieldBase(120, 420,20,14)
all_aliens_group.add(all_aliens_group1)
all_aliens_group.add(all_aliens_group2)
all_aliens_group.add(all_aliens_group3)

all_sprites_group.add(ship)
all_flyingSaucers_group.add(flyingSaucer)
#all_sprites_group.add(flyingSaucer)
all_sprites_group.add(all_aliens_group)
#all_sprites_group.add(all_shieldBases_group)
all_sprites_group.add(all_blockShields_group)
#print "\nContent of all_aliens_group!:\n ",
#for alien in all_aliens_group:
#	print alien

score1 = FONT.render("SCORE <1>", True, WHITE)
score2 = FONT.render("SCORE <2>", True, WHITE)
hi_score = FONT.render("HI-SCORE", True, WHITE)
credit =  FONT.render("CREDIT", True, WHITE)

score_image = sprite_sheet.imgat(SCORE)
score_rect = score_image.get_rect()



while not done:

	all_sprites_group.update()
	#channel = switchSound().play(-1, 500)
	all_flyingSaucers_group.update()
	#channel = ufoHighpitch_sound.play()
	
	for alien in all_aliens_group:
		if alien.isAtWall():
			#print "alien.deplacement vertical: ", alien.deplacement_vert
			#all_aliens_group.reverseDirection()
			#all_aliens_group.moveVertical()
			alienRowDown()
			#Alien.speed = Alien.speed + 10

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
		channel = shoot_sound.play()
		#chan2 = pygame.mixer.find_channel()
		#chan2.queue(shoot_sound)


		if now - ship.last_shot >= SHOT_DELAY:
			ship.last_shot = now
			miss = Missile(MISSILE_SHIP_COORD, sprite_sheet)
			miss.rect.x = ship.rect.x + SHIP_COORD[0][2]/2
			all_sprites_group.add(miss)
			all_missile_group.add(miss)
			#all_Ship_missles.append(miss)

	screen.fill(BLACK)	
	screen.blit(score1, (30, 10))
	screen.blit(score_image, (27, 37))
	all_sprites_group.draw(screen)
	all_flyingSaucers_group.draw(screen)

			
	pygame.display.flip()
	
	#pygame.display.update()
	clock.tick(60)

#print "\nContent of all sprite group"
#for sprite in all_sprites_group:
#	print sprite
pygame.quit()