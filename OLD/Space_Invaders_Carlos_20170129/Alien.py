import pygame
from SpriteSheet_Functions import SpriteSheet
from Constants import *
from SpriteSheet_Functions import SpriteSheet
from Sounds import *

class Alien(pygame.sprite.Sprite):
	animcycle = 50
	speed = 5
	speedLimitChangeImage = 32
	counterSound = 0
	#invaders_sounds=[fastInvader1_sound, fastInvader2_sound, fastInvader3_sound,fastInvader4_sound]
	#myCounterSpeed = 0
	def __init__(self, alien_coord_list, sprite_sheet):
		super(Alien, self).__init__()
		self.alien_coord_list = alien_coord_list
		#self.images = sprite_sheet.imgsat(ALIEN1_COORD)
		self.images = sprite_sheet.imgsat(self.alien_coord_list)
		#self.image = sprite_sheet.imgat(ALIEN1_COORD[0])
		self.image = sprite_sheet.imgat(self.alien_coord_list[0])
		self.rect = self.image.get_rect()
		self.deplacement_vert = 15
		self.indexImage = 0
		self.counter = 0
		self.maxcount = len(self.images)*self.animcycle
		self.rowChangeAdjustment = self.speed
		self.myCounterSpeed = 0
		#self.speedLimitChangeImage = 32
	def switchSound(self):
		sound = invaders_sounds[self.counterSound]
		if self.counterSound > len(invaders_sounds) -2:
			self.counterSound = 0
		self.counterSound = self.counterSound + 1
		return sound

	def update(self):
		#global COUNTER_ALIEN_SPEED
		#COUNTER_ALIEN_SPEED = COUNTER_ALIEN_SPEED + 1

		self.myCounterSpeed = self.myCounterSpeed + 1
		if (self.myCounterSpeed > self.speedLimitChangeImage):
			#channel = self.switchSound().play(-1, 500)
			self.switchImage()
			self.rect.move_ip(self.speed,0)
						#COUNTER_ALIEN_SPEED  = 0
			self.myCounterSpeed = 0
		#if self.isAtWall():
		#	self.reverseDirection()
		#	pass
			#alienRowDown()
			#all_aliens_group.moveVertical()
			#all_aliens_group.reverseDirection()
			#self.moveVertical()
			#self.reverseDirection()
		
		if self.rect.top > SIZE[1]:
			self.kill()
			#print "i just killed"

	def moveVertical(self):
		self.rect.y = self.rect.y + self.deplacement_vert

	def isAtWall(self):
		if self.rect.x >  (SIZE[0]- self.alien_coord_list[0][2]):
			#self.rect.x = SIZE[0]- self.alien_coord_list[0][2]
			return True
		if self.rect.x < 0:
			#self.rect.x = 0 
			return True
		return False

	def moveBack(self):
		self.rect.x = self.rect.x - 30

	def reverseDirection(self):
		self.speed = -self.speed
		if self.speed < 0:
			#print "self.speed: ", self.speed
			self.rect.x = self.rect.x - self.rowChangeAdjustment
			#print "self.rect.x: ", self.rect.x
		if self.speed >0:
			self.rect.x = self.rect.x + self.rowChangeAdjustment


	def switchImage(self):
		if self.image == self.images[0]:
				self.image = self.images[1]
		else:
			self.image = self.images[0]

	#def draw(self, theScreen):
	#	self.switchImage()
		#screen.blit(ALIEN1_POS2.image,(ALIEN1_POS1.rect.x, ALIEN1_POS1.rect.y))
	#	theScreen.blit(self.image,(self.rect.x, self.rect.y))
	def explode(self):
		self.image = sprite_sheet.imgat(ALIEN_EXPLOSION_COORD)
		"le alien a explose!!!"
		#theScreen.blit(self.image,(self.rect.x, self.rect.y))

	def __str__(self):
		return "Alien: x: %d and y: %d " % (self.rect.x, self.rect.y)

