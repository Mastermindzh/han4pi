import pygame
import mainmenu as menu
pygame.init()

def bepaalThema(thema):
  if thema == "Modern":
	return "Klassiek"
  return "Modern"


size = width, height = 340,240	
scherm = pygame.display.set_mode(size)
pygame.key.set_repeat(500,30)
thema = bepaalThema("")

while True:
  scherm.fill(0)
  pygame.display.update()
  keuze = menu.mainmenu(scherm, [
                        'Twee Speler Spel',
                        'Vier Speler Spel',
                        'Thema: '+thema,
                        'Highscores',
                        'Spel Beeindigen'], 64,64,None,32,1.4,(0,255,0),(255,0,0))

  if keuze == 0:
      print "De gebruiker start een 2 speler spel"
  elif keuze == 1:
      print "De gebruiker start een 4 speler spel"
  elif keuze == 2:
      thema = bepaalThema(thema)
  elif keuze == 3:
      print "De gebruiker vraagt de highscores op"
  elif keuze == 4:
      print "De gebruiker beeindigd het spel"
      pygame.quit()
      exit()
