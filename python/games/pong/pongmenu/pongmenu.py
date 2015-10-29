import pygame
import mainmenu as menu
pygame.init()

size = width, height = 340,240	
screen = pygame.display.set_mode(size)
screen.fill(0)
pygame.display.update()
pygame.key.set_repeat(500,30)

choose = menu.mainmenu(screen, [
                        'Twee Speler Spel',
                        'Vier Speler Spel',
                        'Thema: Klassiek',
                        'Highscores',
                        'Spel Beeindigen'], 64,64,None,32,1.4,(0,255,0),(255,0,0))

if choose == 0:
    print "De gebruiker start een 2 speler spel"
elif choose == 1:
    print "De gebruiker start een 4 speler spel"
elif choose == 2:
    print "De gebruiker veranderd het thema"
elif choose == 3:
    print "De gebruiker vraagt de highscores op"
elif choose == 4:
    print "De gebruiker beeindigd het spel"
pygame.quit()
exit()
