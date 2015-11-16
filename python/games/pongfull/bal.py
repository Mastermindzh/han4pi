import pygame, sys, math, time, random

class Bal(pygame.sprite.Sprite): # de bal klasse

        def __init__(bal, (xy), beweging, speler1, speler2, schermklasse): #de bal krijgt een object, een positie, en een beweging (de verandering in x en y iedere frame) mee
                pygame.sprite.Sprite.__init__(bal) #initialiseer de sprite
                bal.image, bal.rect = schermklasse.laad_afbeelding('bal.png') # gebruik de methode laad_afbeelding om de afbeelding in te laden en de grootte hiervan
                scherm = pygame.display.get_surface() # een variabele binnen de bal voor het scherm zodat deze op de volgende regel gebruikt kan worden
                bal.grenzen = scherm.get_rect()#de grenzen van de bal zijn gelijk aan de grenzen van het scherm
                bal.beweging = beweging #stel de beweging van de bal in
                bal.speler1=speler1 # voeg een variabele speler 1 in (voor toekenning van de punten)
                bal.speler2=speler2 # voeg een variabele speler 2 in (voor toekenning van de punten)
                bal.scherm=schermklasse
		bal.geraakt = True #of de bal geraakt is of niet

        def update(bal):
                nieuwePositie = bal.berekenNieuwePositie() #beweeg de bal naar aanleiding van de beweging
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
				#bal.speler2.punten += 1 # speler 2 krijgt een punt!!!
				bal.rect, bal.speler2.punten, hoek, z = bal.scoorBal(bal.speler2.punten, hoek) #beweeg de bal naar aanleiding van de beweging
				
			if tr and br: #wanneer de bal aan de rechterkant uit het scherm gaat
				#hoek = math.pi - hoek # eenvoudige hoekberekening voor het afketsen van de bal
				#bal.speler1.punten += 1# speler 1 krijgt een punt!!!
				bal.rect, bal.speler1.punten, hoek, z = bal.scoorBal(bal.speler1.punten, hoek) #beweeg de bal naar aanleiding van de beweging
	    
		else:
			bal.speler1.rect.inflate(-3, -3)
			bal.speler2.rect.inflate(-3, -3)
			if bal.rect.colliderect(bal.speler1.rect) == 1 and not bal.geraakt: #speler 1 raakt met zijn padje de bal
				hoek = math.pi - hoek # eenvoudige hoekberekening voor het afketsen van de bal
				bal.geraakt = not bal.geraakt # verander de boolean geraakt van een 0 in een 1	
				z+=1
			elif bal.rect.colliderect(bal.speler2.rect) == 1 and bal.geraakt:#speler 2 raakt met zijn padje de bal
				hoek = math.pi - hoek# eenvoudige hoekberekening voor het afketsen van de bal
				bal.geraakt = not bal.geraakt  # verander de boolean geraakt van een 0 in een 1
				z+=1
			#elif bal.geraakt:
				#bal.geraakt = not bal.geraakt  # verander de boolean geraakt van een 1 in een 0
		bal.beweging = (hoek,z) # stel de beweging van de bal in

        def berekenNieuwePositie(bal): # berekening voor de nieuwe positie van de bal als er niets wordt geraakt
                (hoek,z) = bal.beweging # hoek en z variabelen instellen op basis van de beweging variabele
                (dx,dy) = (z*math.cos(hoek),z*math.sin(hoek)) # de x en y waarmee de bal zal gaan bewegen worden bepaald op basis van sin en cos
                return bal.rect.move(dx,dy)
                
        def scoorBal(bal, punten, hoek): # berekening voor de nieuwe positie van de bal als er niets wordt geraakt
                punten += 1
                (dx,dy) = (-bal.rect[0]+(bal.scherm.scherm.get_width()/2),-bal.rect[1]+(bal.scherm.scherm.get_height()/2)) # de x en y waarmee de bal zal gaan bewegen worden bepaald op basis van sin en cos
                hoek = math.pi - hoek # eenvoudige hoekberekening voor het afketsen van de bal
                bal.geraakt = not bal.geraakt
                return bal.rect.move(dx,dy), punten, hoek, 3

if __name__ == '__main__':
	sys.stderr.write("Doe me niks aan! Ik ben maar een simpele bal... Als ik jou was zou ik pong.py draaien.")
	sys.exit()
