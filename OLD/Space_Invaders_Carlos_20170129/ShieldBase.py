
import pygame
from Constants import *

class ShieldBase (pygame.sprite.Sprite):
	
	#def __init__(self, shieldBase_coord_list, sprite_sheet):
	def __init__(self):
		super(ShieldBase, self).__init__()
		self.image = pygame.Surface([1, 1])
		self.image.fill(GREEN_SPACE)
		self.rect = self.image.get_rect()
		#self.rect.x = x
		#self.rect.y = y
		#self.shieldBase_coord_list = shieldBase_coord_list
		#self.image = sprite_sheet.imgat(self.shieldBase_coord_list)
		#self.rect = self.image.get_rect()
	
	def __str__(self):
		return "Shieldbase coord: %d , %d " % (self.rect.x, self.rect.y)


	def update(self):
		
		pass