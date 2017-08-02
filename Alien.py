import pygame
from SpriteSheet_Functions import SpriteSheet
from Constants import *
from SpriteSheet_Functions import SpriteSheet
from Sounds import *

class Alien(pygame.sprite.Sprite):
	animcycle = 50
	vectorX = 5
	speedLimitChangeImage = 32
	counterSound = 0
	deplacement_vert = 15
	#invaders_sounds=[fastInvader1_sound, fastInvader2_sound, fastInvader3_sound,fastInvader4_sound]
	#myCounterSpeed = 0
	"""
	def __init__(self, row, column):
        pygame.sprite.Sprite.__init__(self)
        self.width = ENEMYWIDTH
        self.height = ENEMYHEIGHT
        self.row = row
        self.column = column
        self.image = self.setImage()
        self.rect = self.image.get_rect()
        self.name = 'enemy'
        self.vectorx = 1
        self.moveNumber = 0
        self.moveTime = MOVETIME
        self.timeOffset = row * TIMEOFFSET
        self.timer = pygame.time.get_ticks() - self.timeOffset

        
        ENEMYWIDTH = 25
        ENEMYHEIGHT = 25
        ENEMYNAME = 'Enemy'
        ENEMYGAP = 20
        ARRAYWIDTH = 10
        ARRAYHEIGHT = 4
        MOVETIME = 1000
        MOVEX = 10
        MOVEY = ENEMYHEIGHT
        TIMEOFFSET = 300
      
"""

	#def __init__(self, alien_coord_list, sprite_sheet, row, column):
	def __init__(self, row, column):
		super(Alien, self).__init__()
		self.row = row
		self.column = column
		self.images = self.setImages()
		self.image = self.setImage()#sprite_sheet.imgat(self.alien_coord_list[0])
		self.rect = self.image.get_rect()
		#self.deplacement_vert = 15
		self.indexImage = 0
		self.counter = 0
		self.maxcount = len(self.images)*self.animcycle
		self.rowChangeAdjustment = self.vectorX
		self.myCounterSpeed = 0
		self.moveTime = MOVETIME
		self.timeOffset = self.row * TIMEOFFSET
		self.timer = pygame.time.get_ticks() - self.timeOffset
		self.moveNumber = 0
		#self.speedLimitChangeImage = 32

		#if currentTime - self.timer > self.moveTime:

		#ALIEN1_COORD = [(5, 223, 28, 21), (39, 223, 28, 21)]
		#ALIEN2_COORD = [(72, 223,28,21), (106, 223, 28,21)]
		#ALIEN3_COORD = [(143, 224, 28,21), (177, 224,28,21)]
	def setImages(self):
		if self.row == 0:
			images = SPRITE_SHEET.imgsat(ALIEN1_COORD)
		elif self.row == 1 or self.row == 2:
			images = SPRITE_SHEET.imgsat(ALIEN2_COORD)
		elif self.row == 3:
			images = SPRITE_SHEET.imgsat(ALIEN3_COORD)
		else:
			images = SPRITE_SHEET.imgsat(ALIEN3_COORD)
		return images

	def setImage(self):
		return self.images[0]
	
	def switchSound(self):
		sound = invaders_sounds[self.counterSound]
		if self.counterSound > len(invaders_sounds) -2:
			self.counterSound = 0
		self.counterSound = self.counterSound + 1
		return sound

	#def update(self, currentTime, all_aliens_group):

	def alienRowDown(self):

		for alien in all_aliens_group:
			alien.reverseDirection()
			alien.moveVertical()

	#self.myCounterSpeed = self.myCounterSpeed + 1
	#	if (self.myCounterSpeed > self.speedLimitChangeImage):
			
	#		self.switchImage()
	#		self.rect.move_ip(self.speed,0)
	#		self.myCounterSpeed = 0
		
	def update(self, *args):

		currentTime = args[0]
		all_aliens_group_here = args[1]

		#self.moveTime = MOVETIME
		#self.timeOffset = self.row * TIMEOFFSET
		#self.timer = pygame.time.get_ticks() - self.timeOffset
		#self.moveNumber = 0
				
		if (currentTime - self.timer) > self.moveTime:
			print "\ncurrentTime: ", currentTime
			print "pygame.time.get_ticks():", pygame.time.get_ticks()
			print "self.timeOffset: ", self.timeOffset
			print "self.timer (pygame.time.get_ticks() - self.timeOffset): ", self.timer
			print "currentTime - self.time: ", currentTime - self.timer
			print "self.moveTime: ", self.moveTime
			
			print "crisse"
			
			self.switchImage()
			if not self.isAtWall():
				#self.rect.x += MOVEX * self.speed
				self.rect.move_ip(self.vectorX,0)
				
			elif self.isAtWall():
				self.alienRowDown()
				
				#reduce move time will make aliens move faster
				if self.moveTime > 100:
					self.moveTime -= 50
			self.timer = currentTime	
    		
		"""self.myCounterSpeed = self.myCounterSpeed + 1
		if (self.myCounterSpeed > self.speedLimitChangeImage):
			self.switchImage()
			self.rect.move_ip(self.speed,0)
			self.myCounterSpeed = 0
		"""
		if self.rect.top > SIZE[1]:
			self.kill()
			

	def moveVertical(self):
		self.rect.y = self.rect.y + self.deplacement_vert

	def isAtWall(self):
		#if self.rect.x >  (SIZE[0]- self.alien_coord_list[0][2]):
		if self.rect.x >  (SIZE[0]- 28):
			#self.rect.x = SIZE[0]- self.alien_coord_list[0][2]
			return True
		if self.rect.x < 0:
			#self.rect.x = 0 
			return True
		return False

	def moveBack(self):
		self.rect.x = self.rect.x - 30

	def reverseDirection(self):
		self.vectorX = -self.vectorX 
		if self.vectorX < 0:
			#print "self.speed: ", self.speed
			self.rect.x = self.rect.x - self.rowChangeAdjustment
			#print "self.rect.x: ", self.rect.x
		if self.vectorX >0:
			self.rect.x = self.rect.x + self.rowChangeAdjustment

	#ALIEN1_COORD = [(5, 223, 28, 21), (39, 223, 28, 21)]
	#ALIEN2_COORD = [(72, 223,28,21), (106, 223, 28,21)]
	#ALIEN3_COORD = [(143, 224, 28,21), (177, 224,28,21)]
	
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
		self.image = SPRITE_SHEET.imgat(ALIEN_EXPLOSION_COORD)
		"le alien a explose!!!"
		#theScreen.blit(self.image,(self.rect.x, self.rect.y))

	def __str__(self):
		return "Alien: x: %d and y: %d " % (self.rect.x, self.rect.y)

