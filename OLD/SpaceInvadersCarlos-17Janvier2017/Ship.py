import pygame
from SpriteSheet_Functions import SpriteSheet
from Constants import *

class Ship(pygame.sprite.Sprite):	
	def __init__(self, ship_coord_list, sprite_sheet):
		super(Ship, self).__init__()
		self.ship_coord_list = ship_coord_list
		self.images = sprite_sheet.imgsat(ship_coord_list)
		self.image = sprite_sheet.imgat(ship_coord_list[0])
		self.rect = self.image.get_rect()
		self.rect.x = 200
		self.rect.y = 470
		self.deplacement_hor = 5
		self.last_shot = 0

	def isAtWall(self):
		if self.rect.x > (SIZE[0]- self.ship_coord_list[0][2]):
			self.rect.x = SIZE[0]- self.ship_coord_list[0][2]
			return True
		elif self.rect.x < 0:
			self.rect.x = 0
			return True
		return False
 
	def moveRight(self):
		if not self.isAtWall():
			self.rect.x += self.deplacement_hor

	def moveLeft(self):
		if not self.isAtWall():
			self.rect.x -= self.deplacement_hor
	
	def explode(self, theScreen):
		self.image = sprite_sheet.imgat(self.ship_coord_list[1])
		theScreen.blit(self.image,(self.rect.x, self.rect.y))
	
	def update(self):
		global all_aliens_group
		if pygame.sprite.spritecollide(self, all_aliens_group, True):
			"explode ship!!!"
	def __str__(self):
		return "Ship: (x: %d , y: %d)" % (self.rect.x, self.rect.y)