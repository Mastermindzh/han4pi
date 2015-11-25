import pygame, sys

class Speler(pygame.sprite.Sprite):

        def __init__(speler, scherm, kant):
                pygame.sprite.Sprite.__init__(speler) # initialiseer de sprite
                speler.image, speler.rect = scherm.laad_afbeelding('padje.png') # gebruik de methode laad_afbeelding om de afbeelding in te laden en de grootte hiervan
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

        def beweegNaarBeneden(speler):#bepaling van positie als de speler naar beneden beweegt. Logischerwijs hoeft alleen de y positie aangepast te worden.
                speler.bewegingsPosities[1] += speler.snelheid

if __name__ == '__main__':
	sys.stderr.write("Jij kan mij besturen, maar niet op deze manier. Als ik jou was zou ik pong.py draaien.")
	sys.exit()
