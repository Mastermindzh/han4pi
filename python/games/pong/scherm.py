import pygame, sys, os
import speler as spelerklasse
import bal as balklasse

class Scherm():
		def __init__(schermobject, spelLengte, lettertypeGrootte): 
			schermobject.scherm = pygame.display.set_mode((640, 640)) #schermgrootte. Het programma is zo gemaakt dat deze zich automatisch aanpast bij verandering van de schermgrootte.
			pygame.font.init() # initialisatie van pygame font
			schermobject.lettertype = pygame.font.Font(None, lettertypeGrootte) # lettertype instellen
			schermobject.achtergrond=schermobject.maakAchtergrondAan()
			schermobject.speler1 = spelerklasse.Speler(0, schermobject, "links") # linker speler aanmaken
			schermobject.speler2 = spelerklasse.Speler(1, schermobject, "rechts") # rechter speler aanmaken
			schermobject.speler3 = spelerklasse.Speler(2, schermobject, "midden") # rechter speler aanmaken
			schermobject.bal = balklasse.Bal((0.47,3), schermobject) # maak de bal aan. Eerste arhument is de positie, tweede de beweging (hoek en snelheid) en de 2 spelers worden meegegeven
			schermobject.bal2 = balklasse.Bal((2.67,3), schermobject)
			schermobject.bal2.rect=schermobject.bal2.rect.move(schermobject.scherm.get_width()-25,0)
			schermobject.bal2.geraakt=False 
			schermobject.spelersprite = pygame.sprite.RenderPlain((schermobject.speler1, schermobject.speler2, schermobject.speler3)) # de sprite van de speler voor het tekenen op het scherm
			schermobject.balsprite = pygame.sprite.RenderPlain(schermobject.bal)# de sprite van de bal voor het tekenen op het scherm
			schermobject.balsprite2 = pygame.sprite.RenderPlain(schermobject.bal2)# de sprite van de bal voor het tekenen op het scherm
			schermobject.winnaar=0
			schermobject.spelLengte=spelLengte
		

		def laad_afbeelding(schermobject, bestandsnaam): #deze methode probeert een afbeelding in te laden.
				bestandspad = os.path.join('afbeeldingen', bestandsnaam) # alle afbeeldingen worden uitgelezen uit een map genaamd "afbeeldingen"
				try:
					afbeelding = pygame.image.load(bestandspad) #laad de afbeelding in
					if afbeelding.get_alpha is None:
							afbeelding = afbeelding.convert()
					else:
							afbeelding = afbeelding.convert_alpha()
				except pygame.error, message:#Mocht dit niet lukken dan geeft de methode een foutmelding weer.
					print "Kan deze afbeelding niet laden : ", bestandspad
					raise SystemExit, message
				return afbeelding, afbeelding.get_rect() #geef de afbeelding en de grootte van de afbeelding terug
				
		def maakAchtergrondAan(schermobject):
			achtergrond = pygame.Surface(schermobject.scherm.get_size()) # de achtergrond krijgt de grootte van het scherm
			achtergrond = achtergrond.convert()
			return achtergrond
		
		def maakAchtergrondZwart(schermobject):
			schermobject.scherm.blit(schermobject.achtergrond, (0, 0))
			
		def tekenTekst(schermobject, tekst, x, y):
			tekst =  schermobject.lettertype.render(tekst,True, (255,255,255)) #Maak het tekstobject met witte kleur
			tekstrect = tekst.get_rect()
			tekstrect = tekstrect.move(x,y) # tekst op de juiste positie zetten
			schermobject.scherm.blit(tekst, tekstrect) #tekenen van de tekst
			
		def initializeerLettertype(schermobject):
			pygame.font.init() # initialisatie van pygame font
			schermobject.lettertype = pygame.font.Font(None, 20) # lettertype instellen

if __name__ == '__main__':
	sys.stderr.write("Al heeft pong mij hard nodig, blijf ik maar een nietszeggend scherm. Als ik jou was zou ik pong.py draaien.")
	sys.exit()
