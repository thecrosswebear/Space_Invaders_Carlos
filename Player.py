import pygame

from Ship import Ship
#from Constants import Constants

class Player (object):
	
	def __init__(self):
		self.lives = 4
		self.score = 0
		self.ship = Ship(self)
		self.missile_group = pygame.sprite.Group()

	