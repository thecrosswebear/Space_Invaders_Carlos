import pygame



pygame.init()

SIZE = (500,500)
BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0, 252,0]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("I will rock tonight")

symbol = "*"

print "\nTriangle \n"

def printTriangle(les_rangee):
	for rangee in range(les_rangee):
		for colonne in range (30):
			print symbol,
		print "\n"




printTriangle(6)


class TestAlien(object):
	outNumber = 55
	def __init__(self, firstNumber, secondNumber):
		self.firstNumber = firstNumber
		self.secondNumber = secondNumber
	def __str__(self):
		return "outNumber: %d \nfirstNumber: %d \nsecondNumber: %d \n" % (self.outNumber, self.firstNumber, self.secondNumber)

testAlienAVANT = TestAlien(3,4)
print testAlienAVANT
#print "testAlienAVANT outNumber: " , testAlienAVANT.outNumber
#print "testAlienAVANT firstNumber: " , testAlienAVANT.firstNumber
#print "testAlienAVANT secondNumber: " , testAlienAVANT.secondNumber
print "\n"

TestAlien.outNumber = 77777
TestAlien.firstNumber = 8888
TestAlien.secondNumber = 8888
testAlienAVANT.firstNumber = 11111
print "apres \n", testAlienAVANT
#print "testAlienAVANT outNumber: " , testAlienAVANT.outNumber
#print "testAlienAVANT firstNumber: " , testAlienAVANT.firstNumber
#print "testAlienAVANT secondNumber: " , testAlienAVANT.secondNumber
print "\n"



#print "testAlienAPRE animCyle: " , testAlienAPRES.animcycle

done = False

#carre = (1,1)
#rect(Surface, color, Rect, width=0) -> Rect
image = pygame.Surface([1, 1])
image.fill(GREEN)
carre = image.get_rect()
widthCarre = 1
heightCarre = 1
xStart = 250
yStart = 250
sizeShield = (20,14)

screen.fill(BLACK)

for xStart in range(sizeShield[0]):
	for yStart in range(sizeShield[1]):
		pygame.draw.rect(screen, GREEN, (xStart,yStart,1,1) )		
		pygame.display.update()

pygame.draw.rect(screen, RED, (xStart+60, yStart+ 360,50,50) )			
pygame.display.update()







while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	keys = pygame.key.get_pressed()

	if keys[pygame.K_ESCAPE]:
		done = True

		#keys2 = pygame.key.get_pressed()

tab1 = [1,2,3,4]
tab2 = tab1[1:]
print tab2

pygame.quit()