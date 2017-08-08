import pygame
from SpriteSheet_Functions import SpriteSheet
from Alien import Alien
from Constants import *

class AlienExplosion(pygame.sprite.Sprite):
    animcycle = 4
    def __init__(self, Alien, sprite_sheet):
    	#print "Alien Explosion created!"
    	super(AlienExplosion, self).__init__()
    	self.image = sprite_sheet.imgat(ALIEN_EXPLOSION_COORD)
    	self.counter = 0
    	self.maxcount = self.animcycle**2
    	self.rect = self.image.get_rect()
    	self.rect.center = Alien.rect.center

    	#Il y a peut-etre une difference de 3 pixels entre l'alien et l'explosion
    	#self.rect.x +=3
    	Alien.kill()
   
    def update(self):
        self.counter = self.counter + 1
        if self.counter == self.maxcount:
            self.kill()

    def __str__(self):
    	return "AlienExplosion: x: %d and y: %d " % (self.rect.x, self.rect.y)