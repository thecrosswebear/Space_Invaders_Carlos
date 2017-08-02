import pygame
from SpriteSheet_Functions import SpriteSheet
from Constants import *

pygame.init()

# chepas pq j'ai eu besoin de cette ligne tabarnak
screen = pygame.display.set_mode(SIZE)

class Ship(pygame.sprite.Sprite):	
	#def __init__(self, sprite_sheet = SpriteSheet(SPRITE_SHEET_FILE), ship_coord_list = SHIP_COORD):
	def __init__(self, player):
		super(Ship, self).__init__()
		#SPRITE_SHEET.imgsat(ALIEN1_COORD)
		#self.ship_coord_list = ship_coord_list
		self.images = SPRITE_SHEET.imgsat(SHIP_COORD)
		self.image = SPRITE_SHEET.imgat(SHIP_COORD[0])
		self.rect = self.image.get_rect()
		self.rect.x = 200
		self.rect.y = 422
		self.vectorX = 5
		self.last_shot = 0
		self.player = player
	
	def isAtWall(self):
		if self.rect.x > (SIZE[0]- SHIP_COORD[0][2]):
			self.rect.x = SIZE[0]- SHIP_COORD[0][2]
			return True
		elif self.rect.x < 0:
			self.rect.x = 0
			return True
		return False
 
	def moveRight(self):
		if not self.isAtWall():
			self.rect.x += self.vectorX

	def moveLeft(self):
		if not self.isAtWall():
			self.rect.x -= self.vectorX
	
	def explode(self):
		self.image = SPRITE_SHEET.imgat(SHIP_COORD[1])
		#theScreen.blit(self.image,(self.rect.x, self.rect.y))
	
	def update(self, *args):
		global all_aliens_group
		if pygame.sprite.spritecollide(self, all_aliens_group, True):
			print "explode ship!!!"
			self.explode()
			self.player.lives -= 1
			self.kill()
	def __str__(self):
		return "Ship: (x: %d , y: %d)" % (self.rect.x, self.rect.y)