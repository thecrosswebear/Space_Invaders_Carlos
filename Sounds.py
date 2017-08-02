import pygame

#pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init(frequency=22050,size=-16,channels=4)

shoot_sound = pygame.mixer.Sound("Sounds/shoot.wav")
invaderKilled_sound = pygame.mixer.Sound("Sounds/invaderKilled.wav")
fastInvader1_sound= pygame.mixer.Sound("Sounds/fastInvader1.wav")
fastInvader2_sound= pygame.mixer.Sound("Sounds/fastInvader2.wav")
fastInvader3_sound= pygame.mixer.Sound("Sounds/fastInvader3.wav")
fastInvader4_sound= pygame.mixer.Sound("Sounds/fastInvader4.wav")
ufoLowpitch_sound = pygame.mixer.Sound("Sounds/ufo_lowpitch.wav")
ufoHighpitch_sound = pygame.mixer.Sound("Sounds/ufo_highpitch.wav")

invaders_sounds=[fastInvader1_sound, fastInvader2_sound, fastInvader3_sound,fastInvader4_sound]