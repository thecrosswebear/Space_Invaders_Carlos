import pygame
from SpriteSheet_Functions import SpriteSheet
from Alien import Alien
from AlienExplosion import AlienExplosion
from Constants import *
from Sounds import *
from ShieldBase import ShieldBase
from random import randint
#from Player import Player


class Missile(pygame.sprite.Sprite):
	
	speed = 9
	animcycle = 4
    
	def __init__(self, missile_coord_list, sprite_sheet, player):
		super(Missile, self).__init__()
		self.player = player
		self.missile_coord_list = missile_coord_list
		self.sprite_sheet = sprite_sheet
		self.image = sprite_sheet.imgat(self.missile_coord_list[0])
		self.images = sprite_sheet.imgsat(self.missile_coord_list)
		self.imagesTopExplosion = self.images[1:]
		self.rect = self.image.get_rect()
		self.deplacement_hor = 10
		self.rect.x = 0
		self.maxcount = len(self.imagesTopExplosion)*self.animcycle
		self.counter = 1
		#self.rect.y = SIZE[1] - SHIP_COORD[0][3] - 30 # le dernier nombre (30) est le coordonne y du bateau du bas
		self.rect.y = SIZE[1] - self.missile_coord_list[0][3] - 30 
			
	def update(self, *args):
		self.rect.move_ip(0, -self.speed)

		alien_hit_list = pygame.sprite.spritecollide(self, all_aliens_group, True)
		flying_saucer_hit_list = pygame.sprite.spritecollide (self, all_flyingSaucers_group, False)
		
		#shield_hit_list_for_sure = pygame.sprite.spritecollide(self, all_blockShields_group, True, pygame.sprite.collide_rect_ratio(1.5))
		shield_hit_list_for_sure = pygame.sprite.spritecollide(self, all_blockShields_group, True)
		shield_hit_list_random = pygame.sprite.spritecollide(self, all_blockShields_group, False, pygame.sprite.collide_rect_ratio(2))
		
		for shield in shield_hit_list_for_sure:
			print "shield", shield
			self.kill()
			break

		for shield in shield_hit_list_random:
			chiffre = randint(0,3)
			if chiffre == 2:
				shield.kill()


		#for sprite in (sprite for sprite in a_sprite_group.sprites() if sprite.x == 88 and sprite.y == 112): sprite.remove(a_sprite_group)
		
		for flyingSaucer in flying_saucer_hit_list:
			print "elle a explose dans missile"
			self.player.score += 100
			flyingSaucer.explode()
			self.kill()

		for alien in alien_hit_list:
			#print "Alien qui est hit dans missle"
			#print "sprite collide missile and alien in MISSILE CLASS: alien: ", alien.rect.x, alien.rect.y
			all_sprites_group.add(AlienExplosion(alien, self.sprite_sheet))
			self.player.score +=10
			print "score: ", self.player.score
			#chan1 = pygame.mixer.find_channel()
			#chan1.queue(invaderKilled_sound)
			channel = invaderKilled_sound.play()
			Alien.speedLimitChangeImage = Alien.speedLimitChangeImage -1.125
			self.kill()
			#alien.explode()
			#alien.kill()
			#self.kill()
			#print "missile top dans le sprite collide!: ", self.rect.top
		
	
		if self.rect.y <55:
			self.rect.y = 55
			
			#self.image = self.imagesTopExplosion[0]
			print "self.counter/self.animcyle: ", self.counter/self.animcycle 
			self.image = self.imagesTopExplosion[self.counter/self.animcycle]
			self.counter = self.counter + 1
			print "maxcount: ", self.maxcount
			print "counter dans update: ", self.counter
			print self.counter == self.maxcount
			if self.counter == self.maxcount:
				print "it was killed in update missile"
				self.kill()
			


	def __str__(self):
		return "Missile: (x: %d , y: %d)" % (self.rect.x, self.rect.y)