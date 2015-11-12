import pygame, sys, math

class Bal(pygame.sprite.Sprite): # de bal klasse

        def __init__(bal, (xy), beweging, speler1, speler2, schermklasse): #de bal krijgt een object, een positie, en een beweging (de verandering in x en y iedere frame) mee
                pygame.sprite.Sprite.__init__(bal) #initialiseer de sprite
                bal.image, bal.rect = schermklasse.laad_afbeelding('bal.png') # gebruik de methode laad_afbeelding om de afbeelding in te laden en de grootte hiervan
                scherm = pygame.display.get_surface() # een variabele binnen de bal voor het scherm zodat deze op de volgende regel gebruikt kan worden
                bal.grenzen = scherm.get_rect()#de grenzen van de bal zijn gelijk aan de grenzen van het scherm
                bal.beweging = beweging #stel de beweging van de bal in
                bal.speler1=speler1 # voeg een variabele speler 1 in (voor toekenning van de punten)
                bal.speler2=speler2 # voeg een variabele speler 2 in (voor toekenning van de punten)
		bal.geraakt = 0 #of de bal geraakt is of niet

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
				hoek = math.pi - hoek # eenvoudige hoekberekening voor het afketsen van de bal
				bal.speler2.punten += 1 # speler 2 krijgt een punt!!!
				bal.rect = bal.resetBalPositie(bal.rect,bal.beweging) #beweeg de bal naar aanleiding van de beweging
				
			if tr and br: #wanneer de bal aan de rechterkant uit het scherm gaat
				hoek = math.pi - hoek # eenvoudige hoekberekening voor het afketsen van de bal
				bal.speler1.punten += 1# speler 1 krijgt een punt!!!
				bal.rect = bal.resetBalPositie(bal.rect,bal.beweging) #beweeg de bal naar aanleiding van de beweging
	    
		else:
			bal.speler1.rect.inflate(-3, -3)
			bal.speler2.rect.inflate(-3, -3)
			if bal.rect.colliderect(bal.speler1.rect) == 1 and not bal.geraakt: #speler 1 raakt met zijn padje de bal
				hoek = math.pi - hoek # eenvoudige hoekberekening voor het afketsen van de bal
				bal.geraakt = not bal.geraakt # verander de boolean geraakt van een 0 in een 1
			elif bal.rect.colliderect(bal.speler2.rect) == 1 and not bal.geraakt:#speler 2 raakt met zijn padje de bal
				hoek = math.pi - hoek# eenvoudige hoekberekening voor het afketsen van de bal
				bal.geraakt = not bal.geraakt  # verander de boolean geraakt van een 0 in een 1
			elif bal.geraakt:
				bal.geraakt = not bal.geraakt  # verander de boolean geraakt van een 1 in een 0
		bal.beweging = (hoek,z) # stel de beweging van de bal in

        def berekenNieuwePositie(bal,rect,beweging): # berekening voor de nieuwe positie van de bal als er niets wordt geraakt
                (hoek,z) = beweging # hoek en z variabelen instellen op basis van de beweging variabele
                (dx,dy) = (z*math.cos(hoek),z*math.sin(hoek)) # de x en y waarmee de bal zal gaan bewegen worden bepaald op basis van sin en cos
                return rect.move(dx,dy)
                
        def resetBalPositie(bal,rect,beweging): # berekening voor de nieuwe positie van de bal als er niets wordt geraakt
                (hoek,z) = (0.47,beweging[1]) # hoek en z variabelen instellen op basis van de beweging variabele
                (dx,dy) = (-bal.rect[0],-bal.rect[1]) # de x en y waarmee de bal zal gaan bewegen worden bepaald op basis van sin en cos
                return rect.move(dx,dy)

if __name__ == '__main__':
	sys.stderr.write("Doe me niks aan! Ik ben maar een simpele bal... Als ik jou was zou ik pong.py draaien.")
	sys.exit()
