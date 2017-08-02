import pygame
from SpriteSheet_Functions import SpriteSheet
from Constants import *

from Player import Player
from Alien import Alien
from AlienExplosion import AlienExplosion
from Ship import Ship
from FlyingSaucer import FlyingSaucer
from Missile import Missile
from ShieldBase import ShieldBase
from Sounds import *
import math
from random import shuffle


class App(object):

	def __init__(self):
		self.gameStart = True
		self.gameOver = False
		self.beginGame = False
		self.nbLives = 0
		self.player1 = None
		self.clock = None
		self.sprite_sheet = None
		self.screen = pygame.display.set_mode(SIZE)

	def scaleSprite(thisSprite, sprite_coord_list, scale_info):
		sprite_coord_list[2] = sprite_coord_list[2] * scale_info
		sprite_coord_list[3] = sprite_coord_list[3] * scale_info 
		thisSprite.image = pygame.transform.scale(thisSprite.image,(sprite_coord_list[2], sprite_coord_list[3]))

	def makeAliens(self):
	        
	    for row in range(ALIEN_ROWS):
	        for column in range(ALIEN_COLUMNS):
	            alien = Alien(row, column)
	            alien.rect.x = (column * (ENEMYWIDTH + ENEMYGAP)) + ENEMYWIDTH
	            alien.rect.y = (row * (ENEMYHEIGHT + ENEMYGAP)) + 110
	            #alien.rect.y = (row * (ENEMYHEIGHT + ENEMYGAP)) + 290
	            all_aliens_group.add(alien)

	def placeShieldBase(self,group_shieldBase, coordY):
		division = SIZE[1]/4
		for shieldBase in group_shieldBase:
			shieldBase.rect.center = (division, coordY)
			division = division + SIZE[1]/4

	def placeExtraLives(self, _nbLives, startX, startY):
		spaceBetweenShips = 0
		if _nbLives >8:
			_nbLives = 8
		for i in range(_nbLives):
			self.screen.blit(SPRITE_SHEET.imgat(SHIP_COORD[0]), (startX + spaceBetweenShips, startY))
			spaceBetweenShips += 30
			#screen.blit(theScoreP2, (380, 35))


	def placeBlocksForShieldBase(self,coordX, coordY,sizeX, sizeY):
		reinitCoordX = coordX
		for row in BARRIER_DESIGN:
			for col in row:
				if col != 0:
					shield_tmp = ShieldBase()
					shield_tmp.rect.center = (coordX,coordY)
					#myShields.append(shield_tmp)
					#print "crisse", shield_tmp
					all_blockShields_group.add(shield_tmp)
				coordX = coordX + 1
			coordY = coordY + 1
			coordX = reinitCoordX
		
	def alienRowDown():

		for alien in all_aliens_group:
			#for i in range(1,4):
			#	if alien.rowId == i:
			alien.reverseDirection()
			alien.moveVertical()
			#	for pause in range(0,1000):
			#		print pause
			
	def switchSound():
		global counterSound
		sound = invaders_sounds[counterSound]
		if counterSound > len(invaders_sounds):
			counterSound = 0
		counterSound = counterSound + 1
		return sound

	def setUp(self):
		pygame.init()
		pygame.key.set_repeat(10)

		self.clock = pygame.time.Clock()
		#screen = pygame.display.set_mode(SIZE)
		pygame.display.set_caption("test du 13 janvier")
		self.sprite_sheet = SpriteSheet(SPRITE_SHEET_FILE)
		counterSound = 0

		#done = False

		#all_sprites_group = pygame.sprite.Group()
		#all_aliens_group = pygame.sprite.Group()
		#all_missile_group = pygame.sprite.Group()

		newtime = pygame.time.get_ticks()

		self.nbLives = 8
		flyingSaucer = FlyingSaucer(FLYING_SAUCER_COORD, self.sprite_sheet)
		self.player1 = Player()
		self.makeAliens()

		self.placeShieldBase(all_shieldBases_group,435)

		self.placeBlocksForShieldBase(100, 375,46,34)
		self.placeBlocksForShieldBase(220, 375,46,34)
		self.placeBlocksForShieldBase(340, 375,46,34)


		all_sprites_group.add(self.player1.ship)
		all_flyingSaucers_group.add(flyingSaucer)
		all_sprites_group.add(flyingSaucer)
		all_sprites_group.add(all_aliens_group)

		all_sprites_group.add(all_blockShields_group)

		"""
		score1 = FONT.render("SCORE <1>", True, WHITE)
		score2 = FONT.render("SCORE <2>", True, WHITE)
		hi_score = FONT.render("HI-SCORE", True, WHITE)
		credit =  FONT.render("CREDIT", True, WHITE)
		nbCredits = FONT.render("00", True, WHITE)
		nbLivesText = FONT.render(str(nbLives), True, WHITE)

		theScoreP1 = FONT.render(str(player1.score), True, WHITE)
		theHi_Score = FONT.render("0018", True, WHITE)
		theScoreP2 = FONT.render("0000", True, WHITE)
		"""
	def mainLoop(self):
		
		done = False
		self.setUp()

		while not done:
			currentTime = pygame.time.get_ticks()
			all_sprites_group.update(currentTime, all_aliens_group)
			
				#print "current row: ", current_row
			#channel = switchSound().play(-1, 500)
			#all_flyingSaucers_group.update()
			#channel = ufoHighpitch_sound.play()
			
			"""for alien in all_aliens_group:
				if alien.isAtWall():
					alienRowDown()
					break
			"""	

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
				
			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				self.player1.ship.moveLeft()
			elif keys[pygame.K_RIGHT]:
				self.player1.ship.moveRight()
			elif keys[pygame.K_ESCAPE]:
				done = True
			
			if keys[pygame.K_SPACE]:
				now = pygame.time.get_ticks()
				channel = shoot_sound.play()
				#chan2 = pygame.mixer.find_channel()
				#chan2.queue(shoot_sound)


				if now - self.player1.ship.last_shot >= SHOT_DELAY:
					self.player1.ship.last_shot = now
					miss = Missile(MISSILE_SHIP_COORD, self.sprite_sheet, self.player1)
					miss.rect.x = self.player1.ship.rect.x + SHIP_COORD[0][2]/2
					miss.rect.y = self.player1.ship.rect.y
					all_sprites_group.add(miss)
					self.player1.missile_group.add(miss)
					#all_Ship_missles.append(miss)

			# Tout ca se fait dans setup
			self.screen = pygame.display.set_mode(SIZE)
			score1 = FONT.render("SCORE <1>", True, WHITE)
			score2 = FONT.render("SCORE <2>", True, WHITE)
			hi_score = FONT.render("HI-SCORE", True, WHITE)
			credit =  FONT.render("CREDIT", True, WHITE)
			nbCredits = FONT.render("00", True, WHITE)
			
			
			nbLivesText = FONT.render(str(self.nbLives), True, WHITE)

			

			theScoreP1 = FONT.render(str(self.player1.score), True, WHITE)
			theHi_Score = FONT.render("0018", True, WHITE)
			theScoreP2 = FONT.render("0000", True, WHITE)

			# fin de section de setupd



			self.screen.fill(BLACK)	
			self.screen.blit(score1, (67, 10))
			self.screen.blit(hi_score, (210, 10))
			self.screen.blit(score2, (360, 10))
			#format(5, "04")
			#theScoreP1 = FONT.render(format(str(player1.score),"04"), True, WHITE)

			theScoreP1 = FONT.render(format(self.player1.score,"04"), True, WHITE)
			self.screen.blit(theScoreP1, (80, 35))
			#print "score blit: ", the
			self.screen.blit(theHi_Score, (230, 35))
			self.screen.blit(theScoreP2, (380, 35))
			self.screen.blit(credit, (335, 465))
			self.screen.blit(nbCredits, (420, 465))
			self.screen.blit(nbLivesText, (55, 465))
			pygame.draw.line(self.screen, GREEN_SPACE, (50, 460), (450, 460), 1)
			self.placeExtraLives(self.player1.lives -1, 80, 465)
			#screen.blit(score1_image, (67, 10))
			#screen.blit(hi_score_image, (200,10))
			#screen.blit(score1_image, (375,10))
			
			all_sprites_group.draw(self.screen)
			all_flyingSaucers_group.draw(self.screen)

					
			pygame.display.flip()
			
			#pygame.display.update()
			self.clock.tick(60)

		#print "\nContent of all sprite group"
		#for sprite in all_sprites_group:
		#	print sprite
		pygame.quit()

if __name__ == '__main__':
    app = App()
    app.mainLoop()
