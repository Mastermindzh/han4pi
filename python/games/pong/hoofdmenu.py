import pygame, sys


def hoofdmenu(scherm, menu, 
            lettertypeGrootte = 70, afstand = 1.4, fgcolor = (255,255,255),
            cursorkleur = (255,0,0)):

	x_pos=(scherm.scherm.get_width()/2)-(scherm.scherm.get_width()/3.2)#xpositie menu
	y_pos=(scherm.scherm.get_height()/2)-(len(menu)*32)#ypositie menu
	lettertype = pygame.font.Font(None, lettertypeGrootte) #Stel het lettertype en de grootte van het lettertype in
	cursorPositie = 0 # De cursor begint op positie 0
	for i in menu: #Voor ieder menuitem worden de volgende regels code aangeroepen
		tekst =  lettertype.render(str(cursorPositie + 1)+".  " + i,
			True, fgcolor) # De tekst van het menuitem wordt samengesteld (er wordt een nummertje aan toegevoegd)
		tekstvierkant = tekst.get_rect() 
		tekstvierkant = tekstvierkant.move(x_pos, 
		           (lettertypeGrootte // afstand * cursorPositie) + y_pos) #Het menuitem wordt op de goede plaats neergezet
		scherm.scherm.blit(tekst, tekstvierkant) #De tekst wordt getekend op het scherm
		pygame.display.update(tekstvierkant) #De display wordt geupdate waardoor de zojuist getekende tekst ook daadwerkelijk zichtbaar wordt op het scherm
		cursorPositie += 1 #De cursorpositie wordt opgehoogd

	cursorPositie = 0 #Na het samenstellen van het menu wordt de cursor weer op 0 gezet. Nu kan deze zelfde variabele gebruikt worden voor de daadwerkelijke positie van de cursor.
	cursor = lettertype.render(">", True, cursorkleur) # Het pijltje die de cursor moet voorstellen
	cursorvierkant = cursor.get_rect()
	cursorvierkant = cursorvierkant.move(x_pos - (lettertypeGrootte // afstand),
	             (lettertypeGrootte // afstand * cursorPositie) + y_pos) #Zet dit pijltje op de juiste plek

	pijltjeIngedrukt = True #De variabele pijltjeIngedrukt, die bepaald of er een knop is ingedrukt en er daadwerkelijk opnieuw op het scherm moet worden getekend, begint op True. Hierdoor wordt dadelijk in de loop het pijltje bij het geselecteerde menuitem op het scherm getekend.
	menuAfsluiten = False #Een variabele die op true staat als het tijd is om de loop uit te gaan en het menu te verlaten.
	klok = pygame.time.Clock() #Maak de klok aan
	opvuller = pygame.Surface.copy(scherm.scherm) #maak een vakje aan die steeds over de vorige positie van het pijltje (>) wordt getekend 
	opvullervierkant = opvuller.get_rect() 
	
	print "Welkom bij pong!"
	
	while True:
		klok.tick(30)
		if pijltjeIngedrukt == True: #Nadat er op pijltje omhoog of pijltje omlaag is gedrukt moet de opvuller over de oude positie van het pijltje worden getekend. Ook wordt hier het nieuwe pijltje getekend.
			scherm.scherm.blit(opvuller, opvullervierkant) # Teken de opvuller
			pygame.display.update(cursorvierkant) # Geef de opvuller op het scherm weer
			cursorvierkant = cursor.get_rect()
			cursorvierkant = cursorvierkant.move(x_pos - (lettertypeGrootte // afstand),
			             (lettertypeGrootte // afstand * cursorPositie) + y_pos) #Beweeg het cursorvierkant naar aanleiding van de laatste druk op een pijltje van het toetsenbord
			scherm.scherm.blit(cursor, cursorvierkant) # Teken het pijltje (>)
			pygame.display.update(cursorvierkant) # Geef het pijltje (>) op het scherm weer
			pijltjeIngedrukt = False #Het pijltje is nu niet meer ingedrukt
		if menuAfsluiten == True: #Als het menu wordt afgesloten slopen we de loop.
			break
		for event in pygame.event.get(): #Ga alle events af
			if event.type == pygame.QUIT: #Als de speler op kruisje drukt
				return 2
			if event.type == pygame.KEYDOWN: # Als de speler op een toets van het toetsenbord drukt
				if event.key == pygame.K_ESCAPE: # In het geval van escape
					if cursorPositie == len(menu) - 1: # Als de cursor al op de laatste optie in het menu staat sluit het spel zich af. 
						menuAfsluiten = True
					else: # Anders dan zal het pijltje naar de laatste optie in het menu (beeindigen) springen. 
						cursorPositie = len(menu) - 1; pijltjeIngedrukt = True 

				if event.key == pygame.K_1: #Als er op de '1' toets wordt gedrukt wordt het eerste menuitem uitgevoerd.
					cursorPositie = 0; pijltjeIngedrukt = True; menuAfsluiten = True
				elif event.key == pygame.K_2 and len(menu) >= 2:#Als er op de '2' toets wordt gedrukt wordt het tweede menuitem uitgevoerd.
					cursorPositie = 1; pijltjeIngedrukt = True; menuAfsluiten = True
				elif event.key == pygame.K_3 and len(menu) >= 3:#Als er op de '3' toets wordt gedrukt wordt het derde menuitem uitgevoerd.
					cursorPositie = 2; pijltjeIngedrukt = True; menuAfsluiten = True
				elif event.key == pygame.K_4 and len(menu) >= 4:#Als er op de '4' toets wordt gedrukt wordt het vierde menuitem uitgevoerd.
					cursorPositie = 3; pijltjeIngedrukt = True; menuAfsluiten = True
				elif event.key == pygame.K_UP: #Als er op pijltje omhoog wordt gedrukt
					pijltjeIngedrukt = True
					if cursorPositie == 0: #Als de cursorpositie op 0 staat wordt deze opgehoogd naar de lengte van het menu
						cursorPositie = len(menu) - 1
					else: #anders wordt de cursorpositie met 1 verlaagd
						cursorPositie -= 1
				elif event.key == pygame.K_DOWN:
					pijltjeIngedrukt = True
					if cursorPositie == len(menu) - 1: #Als de cursorpositie op de lengte van het menu (-1 natuurlijk) staat wordt deze verlaagd naar 0
						cursorPositie = 0
					else: #anders wordt de cursorpositie met 1 opgehoogd
						cursorPositie += 1
				elif event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:#Als er op enter wordt gedrukt mag het menu af worden gesloten
							menuAfsluiten = True
	
	return cursorPositie

if __name__ == '__main__':
	sys.stderr.write("Je moet mij importeren, niet draaien.")
	sys.exit()
