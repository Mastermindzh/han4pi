import pygame, sys, potmeter

class Speler(pygame.sprite.Sprite):

        def __init__(speler, spelernummer, scherm, kant):
                pygame.sprite.Sprite.__init__(speler) # initialiseer de sprite
                speler.image, speler.rect = scherm.laad_afbeelding('padje.png') # gebruik de methode laad_afbeelding om de afbeelding in te laden en de grootte hiervan
                scherm = pygame.display.get_surface() # een variabele binnen de speler voor het scherm zodat deze op de volgende regel gebruikt kan worden
                speler.grenzen = scherm.get_rect()#de grenzen van de speler zijn gelijk aan de grenzen van het scherm
                speler.punten = 0 # de speler begint met nul punten
                speler.kant = kant # de kant van de speler (speler 1 heeft kant links, speler 2 heeft kant rechts)
                speler.bewegingsPosities = [0,0] # de bewegingsposities van de speler
                speler.stelPositiesIn() # stel de positie van de speler in
                speler.potMeter = potmeter.PotMeter(spelernummer, speler.rect[1], scherm.get_height())

        def stelPositiesIn(speler):#stel de positie van de speler in
                if speler.kant == "links": # stel de grenzen voor de linker speler in
                        speler.rect.midleft = speler.grenzen.midleft
                elif speler.kant == "rechts": # stel de grenzen voor de rechter speler in
                        speler.rect.midright = speler.grenzen.midright

        def update(speler): # speler update (wordt iedere loop aangeroepen)
                nieuwePositie = speler.rect.move(speler.bewegingsPosities) # bepaal de nieuwe positie van de speler
                if speler.grenzen.contains(nieuwePositie): #zorg dat de speler niet het scherm uit wandelt
                        speler.rect = nieuwePositie 
                pygame.event.pump()

        def beweeg(speler): #bepaling van positie als de speler beweegt. Logischerwijs hoeft alleen de y positie aangepast te worden.
			spelerBeweging=speler.potMeter.positieVerandering(speler.rect)
			if(spelerBeweging==0.0):
				speler.bewegingsPosities = [0,0] #de speler mag niet meer bewegen
			else:
				speler.bewegingsPosities[1] = spelerBeweging

if __name__ == '__main__':
	sys.stderr.write("Jij kan mij besturen, maar niet op deze manier. Als ik jou was zou ik pong.py draaien.")
	sys.exit()
