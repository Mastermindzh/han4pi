import sys, pygame
pygame.init()
size = breedte, hoogte = 800, 400
snelheid = [1, 1]
black = 0, 0, 0
 
scherm = pygame.display.set_mode(size)
 
bal = pygame.image.load("bal.png")
vierkantbal = bal.get_rect()

while 1:
 for event in pygame.event.get():
   if event.type == pygame.QUIT: sys.exit()
 vierkantbal = vierkantbal.move(snelheid)
 if vierkantbal.left < 0 or vierkantbal.right > breedte:
  snelheid[0] = -snelheid[0]
 if vierkantbal.top < 0 or vierkantbal.bottom > hoogte:
  snelheid[1] = -snelheid[1]

 scherm.fill(black)
 scherm.blit(bal, vierkantbal)
 pygame.display.flip()
