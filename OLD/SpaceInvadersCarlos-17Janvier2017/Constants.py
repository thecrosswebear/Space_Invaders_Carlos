import pygame


"""
Global constants
"""
#from SpriteSheet_Functions import SpriteSheet

#sprite_sheet = SpriteSheet("Data/space_invaders_sprite_sheet.png")
all_sprites_group = pygame.sprite.Group()
all_aliens_group = pygame.sprite.Group()
all_aliens_group1 = pygame.sprite.Group()
all_aliens_group2 = pygame.sprite.Group()
all_aliens_group3 = pygame.sprite.Group()
all_missile_group = pygame.sprite.Group()



# Screen dimensions
SIZE = (500, 500)

# Colors
BLACK    = (   0,   0,   0) 
WHITE    = ( 255, 255, 255) 
BLUE     = (   0,   0, 255)
RED = [255,0,0]

COUNTER_ALIEN_SPEED = 0

#Coordinates of sprites on sprite sheet
SHIP_COORD = [(275, 226, 31,20),(365,271,31,20)]
#SHIP_LARGE = (353, 1161, 108, 71)


MISSILE_SHIP_COORD = (335,220,2,12)

#ALIEN1_COORD = [(5, 223, 20, 21), (39, 223, 20, 21)]
#ALIEN2_COORD = [(72, 223,26,21), (106, 223, 26,21)]
#ALIEN3_COORD = [(143, 224, 28,21), (177, 224,28,21)]

ALIEN1_COORD = [(5, 223, 28, 21), (39, 223, 28, 21)]
ALIEN2_COORD = [(72, 223,28,21), (106, 223, 28,21)]
ALIEN3_COORD = [(143, 224, 28,21), (177, 224,28,21)]

ALIEN_EXPLOSION_COORD = [437, 275, 27, 21]

FLYING_SAUCER_COORD = [214, 221, 50, 25]

SHOT_DELAY = 200
ALIENS_PER_ROW = 11
NB_ROWS_ALIENS = 5

