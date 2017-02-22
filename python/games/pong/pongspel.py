try: #probeer de benodigde klassen te importeren
        import sys
        import random
        import potmeter
        import pygame
        from pygame.locals import *
except ImportError, err: # Mocht dit niet lukken dan geef ik een foutmelding weer
        print "Kan deze module niet laden. %s" % (err)
        sys.exit(2)

def startPong(scherm, aantalBallen):
        pygame.init()
        pygame.display.set_caption('HAN4PI Pong') # naam van het programma

	klok = pygame.time.Clock()
	
        while 1:
		klok.tick(60)
		doQuit = False
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			elif event.type == KEYDOWN: #als de toets wordt ingedrukt
				if event.key == K_ESCAPE:
					doQuit = True
		if doQuit:
			break
		scherm.maakAchtergrondZwart() # hele achtergrond zwart
		scherm.tekenTekst('Punten speler 1: '+str(scherm.speler1.punten),10, 10)
		scherm.tekenTekst('Punten speler 2: '+str(scherm.speler2.punten),scherm.scherm.get_width()-125,10)
		if(scherm.winnaar!=0):
			scherm.tekenTekst('Speler ' +str(scherm.winnaar)+ ' wint', 300,300)
		else:
			scherm.balsprite.update()#balsprite updaten
			if(aantalBallen == 2):
				scherm.balsprite2.update()#balsprite updaten
				scherm.balsprite2.draw(scherm.scherm)#balsprite tekenen
			
			scherm.speler1.beweeg()
			scherm.speler2.beweeg()
			scherm.speler3.beweeg()
			
			scherm.spelersprite.update()#spelersprite updaten
			scherm.balsprite.draw(scherm.scherm)#balsprite tekenen
			scherm.spelersprite.draw(scherm.scherm)#spelersprite tekenen
		pygame.display.flip()

if __name__ == '__main__': 
	sys.stderr.write("Voer alstublieft het hoofdmenu (pong.py) uit. Vanuit daar zal ik worden aangeroepen.")
	sys.exit()
