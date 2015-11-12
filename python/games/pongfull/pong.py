import pygame
import hoofdmenu as menu
import pongspel as spel
import scherm as schermklasse
pygame.init()

def bepaalThema(thema):
  if thema == "Modern":
	return "Klassiek"
  return "Modern"


scherm = schermklasse.Scherm()
pygame.key.set_repeat(500,30)
thema = bepaalThema("")

while True:
  scherm.maakAchtergrondZwart()
  pygame.display.update()
  keuze = menu.hoofdmenu(scherm.scherm, [
                        'Twee Speler Spel',
                        'Vier Speler Spel',
                        'Thema: '+thema,
                        'Highscores',
                        'Spel Beeindigen'], None,scherm.scherm.get_width()/10,1.4,(0,255,0),(255,0,0))

  if keuze == 0:
      spel.startPong(scherm)
  elif keuze == 1:
      print "De gebruiker start een 4 speler spel"
  elif keuze == 2:
      thema = bepaalThema(thema)
  elif keuze == 3:
      print "De gebruiker vraagt de highscores op"
  elif keuze == 4:
      pygame.quit()
      exit()
