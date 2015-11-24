#######################
# Catch the raspberry #
#######################
#
# Catch the raspberry is een simpel spel waarbij de framboos (hierna bal genoemd)
# gevangen moet worden met de emmer. Voor elke gevangen framboos krijg je 10 punten!
# Elke 100 punten gaat de framboos sneller bewegen.
# Kun jij de hoogste score bemachtigen ? Probeer het snel !
#
# AUTHOR:  Rick van Lieshout 
# LICENSE: MIT


# We hebben een aantal programma's nodig, die kunnen we hier importeren
import sys, pygame, spidev,time,os
from pygame import *
from random import randint

# Open spi op poort...
spi=spidev.SpiDev()
spi.open(0,0)


# Pin nummer van de POT 
potpin = 0;
last_read =0;
tolerance = 5;

# Methode om pot mee te lezen
def readadc(adcnum):
	if((adcnum > 7) or (adcnum < 0)):
		return -1
	r = spi.xfer2([1,(8+adcnum)<<4,0])
	adcout = ((r[1]&3)<< 8) +r[2]
	return adcout



# Start pygame en maak een scherm
init() 													# Start pygame
display.set_caption('Catch the raspberry!')				# Zet de titel van het venster
display.set_icon(image.load("Images/icon.png"))			# Zet het icoon van het spel
bg = image.load("Images/background.png")

# Start met het spelen van muziek
pygame.mixer.init(48000, -16, 1, 1024)

music = mixer.music.load("Sounds/bg_music.mp3")
catch = mixer.Sound("Sounds/bg_music.mp3")
mixer.music.set_volume(0.4)
mixer.music.play(-1)
heart = image.load("Images/heart.png")

# Scherm instellingen
scherm_breedte 	 = 400
scherm_hoogte 	 = 600
grootte 		 = width, height 					= scherm_breedte, scherm_hoogte
scherm 			 = display.set_mode(grootte)
Achtergrondkleur = 115, 115, 115 # [RED,GREEN,BLUE]

# Zet het aantal FPS gelijk aan de clock van 
fpsClock = time.Clock()

# Text instellingen
font_vorige_score = font.SysFont("monospace", 25)
font_big 		= font.SysFont("monospace", 50)
font_medium 	= font.SysFont("monospace", 20)

# Bal instellingen
bal 				= image.load("Images/bal.png") 						# Het plaatje van de bal toewijzen		
standaard_snelheid	= 5;												# Standaardsnelheid van de bal toewijzen. Hiermee wordt de snelheid ook verhoogt
speed 				= [0, standaard_snelheid]							# Balsnelheid [horizontaal, verticaal]
bal_sneller_naar	= 100												# Het aantal punten waar een snelheidsverhoging ingaat.
balrect 			= bal.get_rect() 									# Sla het vierkant van de bal op (makkelijk voor intersects)
balrect.centerx	= randint(0+(bal.get_size()[0]/2),scherm_breedte)		# Zet de eerste raspberry op een ranom x.

# Emmer instellingen
emmer 				= image.load("Images/bucket.png") 	# Het plaatje van de emmer toewijzen
emmerrect 			= emmer.get_rect()					# Sla het vierkant van de emmer op (makkelijk voor intersects)
emmerrect.centery 	= height -100						# Y positie van de emmer

# Overige instellingen
score 	= 0			# De startscore
vorige_score = 0	# De score bij de vorige snelheidsverhoging.
life 	= 3			# Het aantal levens dat nog over is.

# Kleuren
WIT = (255,255,255)

############
# Methodes #
############
#
# Een methode is een stukje code dat je kunt aanroepen met 1 woord!
# Dat is vooral handig als je dingen vaker wilt laten gebruiken.
# De syntax om een methode te maken is als volgt
#
# def titelVanMethode():
# 	Eerste regel code
#	Tweede regel code
#
# Vervolgens kunnen we die methode dan aanroepen met:
# 
# titelVanMethode()
#


# Als het spel wordt afgesloten laat dat gebeuren.
def wachtOpQuit():
	if event.type == QUIT:
		quit()
		sys.exit()

# Muisbeweging van de emmer
def beweegEmmer():
	global last_read , emmerrect, emmer
	trim_pot = readadc(potpin)

	# Check of de emmer te ver naar links zit
	if(trim_pot < emmer.get_size()[0]/2):
		trim_pot = emmer.get_size()[0]/2 + 2
	# Check of de emmer te ver naar rechts zit
	if(trim_pot > width - emmer.get_size()[0]/2):
		trim_pot = width - emmer.get_size()[0]/2
	emmerrect.centerx=trim_pot


#beweeg de bal
def beweegBal():
	global balrect,speed #we willen de variabele boven aan het script gebruiken
	balrect = balrect.move(speed)

# Als de onderkant van de bal voorbij of op de hoogte van het scherm is.
def checkBalVoorbijEmmer():
	global balrect,life
	if balrect.bottom >= height:
		life -=1										# Trek er een leven af.
		balrect.centerx = randint(50,scherm_breedte) 	# Zet de bal terug op een random positie
		balrect.centery = 0								# Zet het Y coordinaat van de bal weer op 0 (bovenaan)		

# Controlleer of de bal gevangen is
def checkBalGevangen():
	global score,balrect
	if (balrect.bottom > emmerrect.top and balrect.top < emmerrect.bottom) and (emmerrect.right > balrect.centerx and emmerrect.left < balrect.centerx):
		score += 10
		balrect.centerx = randint(50,scherm_breedte)
		balrect.centery = 0	
		
		

# Controlleer of de bal sneller moet gaan bewegen.
def controlleerVersnelling():
	global speed,vorige_score,bal
	if score >= vorige_score+bal_sneller_naar:
		speed[1] += standaard_snelheid
		vorige_score = score

def controlleerLevens():
	global scorelabel
	# Controlleer of er nog levens zijn
	if life <= 0:
		# Als de levens 0 of lager zijn tekenen we een game over scherm
		scherm.blit(bg,(0,0))
		gameoverlabel = font_big.render("GAME OVER", 1, WIT) 							# Zet de gameover tekst in een variabele
		musiccredits = font_medium.render("Music by Kevin McLeod", 1, WIT) 				# Zet de gameover tekst in een variabele
		scherm.blit(gameoverlabel, (width/2-gameoverlabel.get_size()[0]/2, height/3))   # Het gameoverlabel tekenen
		scherm.blit(scorelabel, (width/2-scorelabel.get_size()[0]/2, (height/3)+100))	# Het scoreLabel tekenen
		scherm.blit(musiccredits, (width/2-musiccredits.get_size()[0]/2, (height)-100))	# Het musiccreditslabel tekenen
		display.flip()
		# Wacht op het "quit" command (kruisje) om het spel af te sluiten
		while 1:
			for event in pygame.event.get():
				if event.type == QUIT: 
					quit()
					sys.exit()

def tekenScherm():
	global scorelabel
	# Teken de score
	scorelabel = font_vorige_score.render("Score : "+str(score), 1, WIT)
	scherm.blit(bg,(0,0))
	scherm.blit(bal, balrect)			# Teken de bal
	scherm.blit(emmer, emmerrect)		# Teken de emmer	
	scherm.blit(scorelabel, (25, 25))	# Teken het scorelabel
	tekenLevens()						# Teken de hartjes
	display.update() 					# Teken het scherm
	fpsClock.tick(30) 					# Laat de pygame clock 30 keer tikken (30fps)

def tekenLevens():
	for x in range(0, life):
		scherm.blit(heart, (x*40 +25,50)) # +25 om de hartjes uit te lijnen met de scores
	
	

# Een game loop, deze loopt zolang het spel loopt.
while 1:
	# Een for loop om het toetsenbord / muis op te vangen
	for event in pygame.event.get():
		wachtOpQuit() # controlleer of de gebruiker het spel wil afsluiten
	
	beweegEmmer() 				# controlleer of de emmer moet bewegen	
	beweegBal() 				# Beweeg de bal
	checkBalVoorbijEmmer() 		# Controlleer of de bal voorbij de emmer is.
	checkBalGevangen()			# Controlleer of de bal gevangen is
	controlleerVersnelling()	# Controlleer of de bal versneld moet worden
	tekenScherm()				# Teken alles op het scherm
	controlleerLevens()			# Controlleer of er nog levens over zijn.
	
