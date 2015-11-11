VERSION = "0.4"

try: #probeer de benodigde klassen te importeren
        import sys
        import random
        import math
        import os
        #import getopt
        import pygame
        #from socket import *
        from pygame.locals import *
except ImportError, err: # Mocht dit niet lukken dan geef ik een foutmelding weer
        print "Kan deze module niet laden. %s" % (err)
        sys.exit(2)

class Bal(pygame.sprite.Sprite): # de bal klasse
        def __init__(bal, (xy), beweging, initialiseren): #de bal krijgt een object, een positie, en een beweging (de verandering in x en y iedere frame) mee
                pygame.sprite.Sprite.__init__(bal) #initialiseer de sprite
                bal.image, bal.rect = initialiseren.laad_afbeelding('bal.png') # gebruik de methode laad_afbeelding om de afbeelding in te laden en de grootte hiervan
                scherm = pygame.display.get_surface() # een variabele binnen de bal voor het scherm zodat deze op de volgende regel gebruikt kan worden
                bal.grenzen = scherm.get_rect()#de grenzen van de bal zijn gelijk aan de grenzen van het scherm
                bal.beweging = beweging #stel de beweging van de bal in
                bal.speler1 = speler1 # voeg een variabele speler 1 in (voor toekenning van de punten)
                bal.speler2 = speler2 # voeg een variabele speler 2 in (voor toekenning van de punten)
		bal.geraakt = 0 #of de bal geraakt is of niet

		def resetPositie(bal,rect,beweging):# reset de positie van de bal na het midden van het scherm als er gescoort is. 
				(hoek, z) = beweging# MSS NIET NODIG!
				(dx, d,y) = (random.uniform(0, 1), random.uniform(0, 1))# Randomiseer de vector waar de bal op moet gaan bewegen. 
				return rect.move(dx, dy)# return de nieuwe move richting van de bal.
				
        def update(bal):
                nieuwePositie = bal.berekenNieuwePositie(bal.rect,bal.beweging) #beweeg de bal naar aanleiding van de beweging
                bal.rect = nieuwePositie #stel de nieuwe positie van de bal in
		(hoek,z) = bal.beweging #maak de hoek en de z variabele van de bal gelijk aan de beweging 
		
		if not bal.grenzen.contains(nieuwePositie):
			tl = not bal.grenzen.collidepoint(nieuwePositie.topleft)#check over welke grenzen de bal heen is
			tr = not bal.grenzen.collidepoint(nieuwePositie.topright)
			bl = not bal.grenzen.collidepoint(nieuwePositie.bottomleft)
			br = not bal.grenzen.collidepoint(nieuwePositie.bottomright)
			if (tr and tl) or (br and bl): #wanneer de bal in de hoek over 2 grenzen heen gaat ketst deze recht af
				hoek = -hoek
			if tl and bl: #wanneer de bal aan de linkerkant uit het scherm gaat
				#hoek = math.pi - hoek # eenvoudige hoekberekening voor het afketsen van de bal
				speler2.punten += 1 # speler 2 krijgt een punt!!!
				print "kut"
		#		test = bal.resetPositie(bal.rect,bal.beweging)
				#bal.berekenNieuwePositie(bal.rect, bal.beweging)
			if tr and br: #wanneer de bal aan de rechterkant uit het scherm gaat
				#hoek = math.pi - hoek # eenvoudige hoekberekening voor het afketsen van de bal
				speler1.punten += 1# speler 1 krijgt een punt!!!
		#		test = bal.resetPositie(bal.rect,bal.beweging)
		else:
			speler1.rect.inflate(-3, -3)
			speler2.rect.inflate(-3, -3)
			if bal.rect.colliderect(speler1.rect) == 1 and not bal.geraakt: #speler 1 raakt met zijn padje de bal
				hoek = math.pi - hoek # eenvoudige hoekberekening voor het afketsen van de bal
				bal.geraakt = not bal.geraakt # verander de boolean geraakt van een 0 in een 1
			elif bal.rect.colliderect(speler2.rect) == 1 and not bal.geraakt:#speler 2 raakt met zijn padje de bal
				hoek = math.pi - hoek# eenvoudige hoekberekening voor het afketsen van de bal
				bal.geraakt = not bal.geraakt  # verander de boolean geraakt van een 0 in een 1
			elif bal.geraakt:
				bal.geraakt = not bal.geraakt  # verander de boolean geraakt van een 1 in een 0
		bal.beweging = (hoek,z) # stel de beweging van de bal in
        def berekenNieuwePositie(bal,rect,beweging): # berekening voor de nieuwe positie van de bal als er niets wordt geraakt
                (hoek, z) = beweging # hoek en z variabelen instellen op basis van de beweging variabele
                (dx,dy) = (z*math.cos(hoek),z*math.sin(hoek)) # de x en y waarmee de bal zal gaan bewegen worden bepaald op basis van sin en cos
                return rect.move(dx,dy)
                
class Speler(pygame.sprite.Sprite):# de klasse die een speler aanmaakt. Dit houdt in dat alle methoden die nodig zijn om een speler op het scherm te krijgen en te laten bewegen hierin staan.
        def __init__(speler, kant, initialiseren): # soort constructor van de speler klasse.
                pygame.sprite.Sprite.__init__(speler) # initialiseer de sprite
                speler.image, speler.rect = initialiseren.laad_afbeelding('padje.png') # gebruik de methode laad_afbeelding om de afbeelding in te laden en de grootte hiervan
                scherm = pygame.display.get_surface() # een variabele binnen de speler voor het scherm zodat deze op de volgende regel gebruikt kan worden
                speler.grenzen = scherm.get_rect()#de grenzen van de speler zijn gelijk aan de grenzen van het scherm
                speler.punten = 0 # de speler begint met nul punten
                speler.kant = kant # de kant van de speler (speler 1 heeft kant links, speler 2 heeft kant rechts)
                speler.snelheid = 10 # snelheid van de beweging van de speler
                speler.stelPositiesIn() # stel de positie van de speler in

        def stelPositiesIn(speler):#stel de positie van de speler in
                speler.bewegingsPosities = [0,0] # de bewegingsposities van de speler
                if speler.kant == "links": # stel de grenzen voor de linker speler in
                        speler.rect.midleft = speler.grenzen.midleft
                elif speler.kant == "rechts": # stel de grenzen voor de rechter speler in
                        speler.rect.midright = speler.grenzen.midright

        def update(speler): # speler update (wordt iedere loop aangeroepen)
                nieuwePositie = speler.rect.move(speler.bewegingsPosities) # bepaal de nieuwe positie van de speler
                if speler.grenzen.contains(nieuwePositie): #zorg dat de speler niet het scherm uit wandelt
                        speler.rect = nieuwePositie 
                pygame.event.pump()

        def beweegNaarBoven(speler): #bepaling van positie als de speler naar boven beweegt. Logischerwijs hoeft alleen de y positie aangepast te worden.
                speler.bewegingsPosities[1] -= speler.snelheid
                print speler.rect

        def beweegNaarBeneden(speler):#bepaling van positie als de speler naar beneden beweegt. Logischerwijs hoeft alleen de y positie aangepast te worden.
                speler.bewegingsPosities[1] += speler.snelheid
                
		def bestaIk():
				return "kut tering python"
			
def main(): # methode van de main. Vanaf deze methode wordt het spel gerund. OM de main overzichtelijk te houden is er een object initialisatie aangemaakt die de werkzaamheden van de main netjes opdeelt in methoden.
    pygame.init()
    initialiseren = algemeneInitialisatie()
    pygame.display.set_caption('HAN4PI Pong') # naam van het programma
    scherm = initialiseren.achtergrond()
    
    initialiseren.maakSpelers(initialiseren)
    
    initialiseren.maakBal()
	
    initialiseren.spelersBewegen(speler1,speler2)
    
    scherm.blit(scherm, (0, 0))# hele achtergrond zwart
    lettertype = pygame.font.Font(None, 20) # lettertype instellen
    initialiseren.spelersPuntenMaken(scherm, lettertype)
	
    klok = pygame.time.Clock()
    while 1:
		klok.tick(60)

		
class algemeneInitialisatie(): # een klasse die zorgt dat er alle main settings netjes zijn opgedeeld in diverse  methoden.
	def maakBal(self):
		snelheid = 13 # snelheid waarmee de bal over het veld heen beweegt.
		bal = Bal((0, 0),(random.uniform(0, 1),snelheid), self) # maak de bal aan. Eerste argument is de positie, tweede de beweging (hoek en snelheid) en de 2 spelers worden meegegeven
		
	def maakSpelers(self, initialiseren): # maakt de gewenste hoeveelheid spelers aan.
		global speler1
		global speler2
		speler1 = Speler("links", initialiseren) # linker speler aanmaken
		speler2 = Speler("rechts", initialiseren) # rechter speler aanmaken
		print speler1.bestaIk
	
	def achtergrond(self): # tekent de achtergrond naar de gewenste kleur.
		pygame.font.init() # initialisatie van pygame font
		scherm = pygame.display.set_mode((640, 640)) #schermgrootte. Het programma is zo gemaakt dat deze zich automatisch aanpast bij verandering van de schermgrootte.
		achtergrond = pygame.Surface(scherm.get_size()) # de achtergrond krijgt de grootte van het scherm
		achtergrond = achtergrond.convert()
		achtergrond.fill((0, 0, 0)) #zwarte achtergrond
		return scherm
	
	def updateEnTekenSprites(self, scherm): # het tekenen en updaten van alle plaatjes (sprites) wordt in deze methode gedaan.
			spelersprite = pygame.sprite.RenderPlain((speler1, speler2)) # de sprite van de speler voor het tekenen op het scherm
			balsprite = pygame.sprite.RenderPlain(bal)# de sprite van de bal voor het tekenen op het scherm
			balsprite.update()#balsprite updaten
			spelersprite.update()#spelersprite updaten
			balsprite.draw(scherm)#balsprite tekenen
			spelersprite.draw(scherm)#spelersprite tekenen
			pygame.display.flip()
			updateEnTekenSprites(scherm) # update en teken de sprites op het scherm.
			
	def spelersBewegen(self, speler1, speler2): # in deze methode staat de code die ervoor zorgt dat de spelers ook daadwerkelijk kunnen bewegen.
			for event in pygame.event.get():#dit moet vervangen worden door de potentiometers. Voor nu test ik met besturing via pijltje naar boven/beneden en w en s.
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN: #als de toets wordt ingedrukt
					if event.key == K_w: 
						speler1.beweegNaarBoven()
					if event.key == K_s:
						speler1.beweegNaarBeneden()
					if event.key == K_UP:
						speler2.beweegNaarBoven()
					if event.key == K_DOWN:
						speler2.beweegNaarBeneden() 
				elif event.type == KEYUP: #als de toets wordt uitgedrukt
					if event.key == K_w or event.key == K_s:
						speler1.bewegingsPosities = [0,0] #de speler mag niet meer bewegen
					if event.key == K_UP or event.key == K_DOWN:
						speler2.bewegingsPosities = [0,0] #de speler mag niet meer bewegen
			
	def spelersPuntenMaken(self, scherm, lettertype): # het tekenen van het vakje waar de tekst met de score opkomt.
			tekst =  lettertype.render('Punten speler 1: '+str(speler1.punten),True, (255,255,255)) #scorebord speler 1
			tekstrect = tekst.get_rect()
			tekstrect = tekstrect.move(10,10) # tekst op de juiste positie zetten
			scherm.blit(tekst, tekstrect) #tekenen van de tekst
			tekst2 =  lettertype.render('Punten speler 2: '+str(speler2.punten),True, (255,255,255))#scorebord speler 2
			tekstrect2 = tekst2.get_rect()
			tekstrect2 = tekstrect2.move(scherm.get_width()-125,0)# tekst op de juiste positie zetten
			scherm.blit(tekst2, tekstrect2)#tekenen van de tekst
			
	def laad_afbeelding(self, bestandsnaam): #deze methode probeert een afbeelding in te laden.
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
				
			
if __name__ == '__main__': main()
