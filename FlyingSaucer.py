import pygame
from SpriteSheet_Functions import SpriteSheet
from Constants import *
from Sounds import *


class FlyingSaucer(pygame.sprite.Sprite):

	animcycle = 22
	vectorX = 1
	
	#myCounterSpeed = 0
	def __init__(self, flying_saucer_coord, sprite_sheet):
		super(FlyingSaucer, self).__init__()
		self.images = sprite_sheet.imgsat(flying_saucer_coord)
		self.imagesExplosion = self.images[1:]
		self.image = sprite_sheet.imgat(flying_saucer_coord[0])
		#self.imageExplosion = sprite_sheet.imgat(flying_saucer_coord[1])
		self.rect = self.image.get_rect()
		self.maxcount = len(self.imagesExplosion)*self.animcycle
		self.counter = 1
		self.killed = False
		#self.maxcount = len(self.images)*self.animcycle
		#self.rect.y = flying_saucer_coord[0][2]
		self.rect.y = 65
		self.rect.x = SIZE[1] + flying_saucer_coord[0][2] + 10
	def update(self, *args):
		if not self.killed:
			self.rect.move_ip(-self.vectorX,0)
			#ufoLowpitch_sound.play()
		if self.killed:
			self.image = self.imagesExplosion[self.counter/self.animcycle]
			self.counter = self.counter + 1
			#print "counter dans update: ", self.counter
			if self.counter == self.maxcount:
				self.kill()
				

		if self.rect.x < -45:
			self.resetPos()
			#print "Saucer depasser ecran"
	
	def resetPos(self):
		self.rect.x =SIZE[1] + 40

	def isAtWall(self):
		if self.rect.x >  SIZE[0]-flying_saucer_coord[0][2]:
			self.rect.x = SIZE[0]-flying_saucer_coord[0][2]
			return True
		if self.rect.x < 0:
			self.rect.x = 0
			return True
		return False

	def explode(self):
		#if self.killed:
		#self.image = sprite_sheet.imgat(FLYING_SAUCER_COORD(2))
		#self.image = self.imageExplosion
		self.killed = True
		#self.kill()
		print "le FlyingSaucer a explose dans Flying saucer!!!"
		
	def __str__(self):
		return "FlyingSaucer: x: %d and y: %d " % (self.rect.x, self.rect.y)
