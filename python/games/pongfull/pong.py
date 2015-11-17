import pygame
import hoofdmenu as menu
import pongspel as spel
import scherm as schermklasse
pygame.init()

def bepaalAantalBallen(aantalBallen): #bepaalt het aantal ballen als de gebruiker heeft aangevraagd dit te veranderen
  if aantalBallen == "1":
	return "2"
  return "1"


scherm = schermklasse.Scherm() #Maakt het schermobject aan
pygame.key.set_repeat(500,30) #Dit zorgt ervoor dat elke 30 milliseconden het key event een nieuw KEYDOWN event zal produceren, ipv slecht 1x als de toets wordt ingedrukt.
aantalBallen = "1" #Het aantal ballen is standaard 1

while True:
  scherm.maakAchtergrondZwart()
  pygame.display.update() #Zorgt ervoor dat het scherm weer zwart wordt (voor een nieuw menu) als het aantal ballen is veranderd
  keuze = menu.hoofdmenu(scherm, [
                        'Start spel',
                        'Aantal ballen: '+aantalBallen,
                        'Spel Beeindigen'], scherm.scherm.get_width()/10,1.4,(0,255,0),(255,0,0)) #maak het hoofdmenu aan

  if keuze == 0: #Als de keuze 0 is start het spel
      spel.startPong(scherm, aantalBallen)
  elif keuze == 1:#Als de keuze 1 is wordt het aantal ballen veranderd
      aantalBallen = bepaalAantalBallen(aantalBallen)
  elif keuze == 2:#Als de keuze 2 is beeindingd de gebruiker het spel
      pygame.quit()
      exit()
