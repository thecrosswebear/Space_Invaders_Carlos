import pygame
from SpriteSheet_Functions import SpriteSheet
from Constants import *


class FlyingSaucer(pygame.sprite.Sprite):

	animcycle = 4
	speed = 1
	
	#myCounterSpeed = 0
	def __init__(self, flying_saucer_coord, sprite_sheet):
		super(FlyingSaucer, self).__init__()
		self.image = sprite_sheet.imgat(flying_saucer_coord)
		self.imageExplosion = sprite_sheet.imgat(ALIEN_EXPLOSION_COORD)
		self.rect = self.image.get_rect()
		self.maxcount = self.animcycle**2
		self.counter = 0
		self.killed = False
		#self.maxcount = len(self.images)*self.animcycle
		self.rect.y = flying_saucer_coord[2]
		self.rect.x = SIZE[1] + flying_saucer_coord[2] + 10
	def update(self):
		if not self.killed:
			self.rect.move_ip(-self.speed,0)

		if pygame.sprite.spritecollide(self, all_missile_group, True):
			print "saucer explose missle"
			#self.image = sprite_sheet.imgat(ALIEN_EXPLOSION_COORD)
			self.image = self.imageExplosion
			self.killed = True
			return
	
		if self.killed:
			self.counter = self.counter + 1
			if self.counter == self.maxcount:
				self.kill()
		if self.rect.x < -35:
			self.kill()
			print "Saucer depasser ecran"
	
	def isAtWall(self):
		if self.rect.x >  SIZE[0]-flying_saucer_coord[2]:
			self.rect.x = SIZE[0]-flying_saucer_coord[2]
			return True
		if self.rect.x < 0:
			self.rect.x = 0
			return True
		return False

	def explode(self):
		self.image = sprite_sheet.imgat(ALIEN_EXPLOSION_COORD)
		self.kill()
		"le FlyingSaucer a explose!!!"
		
	def __str__(self):
		return "FlyingSaucer: x: %d and y: %d " % (self.rect.x, self.rect.y)
