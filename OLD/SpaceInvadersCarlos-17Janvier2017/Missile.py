import pygame
from SpriteSheet_Functions import SpriteSheet
from Alien import Alien
from AlienExplosion import AlienExplosion
from Constants import *

class Missile(pygame.sprite.Sprite):
	
	speed = 9
    
	def __init__(self, missile_coord_list, sprite_sheet):
		super(Missile, self).__init__()
		self.missile_coord_list = missile_coord_list
		self.sprite_sheet = sprite_sheet
		self.image = sprite_sheet.imgat(self.missile_coord_list)
		self.rect = self.image.get_rect()
		self.deplacement_hor = 10
		self.rect.x = 0
		#self.rect.y = SIZE[1] - SHIP_COORD[0][3] - 30 # le dernier nombre (30) est le coordonne y du bateau du bas
		self.rect.y = SIZE[1] - self.missile_coord_list[3] - 30 
			#le dernier nombre (30) est le coordonne y du bateau du bas
			#def move(self):
			#self.rect.y -= self.deplacement_hor
	def isOffScreen(self):
		if self.rect.y <0:
			return True
		return False
	def update(self):
		self.rect.move_ip(0, -self.speed)
		
		alien_hit_list = pygame.sprite.spritecollide(self, all_aliens_group, True)
		for alien in alien_hit_list:
			#print "Alien qui est hit dans missle"
			#print "sprite collide missile and alien in MISSILE CLASS: alien: ", alien.rect.x, alien.rect.y
			all_sprites_group.add(AlienExplosion(alien, self.sprite_sheet))
			self.kill()
			#alien.explode()
			#alien.kill()
			#self.kill()
			#print "missile top dans le sprite collide!: ", self.rect.top
		if self.isOffScreen():
			self.kill()
		
	def __str__(self):
		return "Missile: (x: %d , y: %d)" % (self.rect.x, self.rect.y)