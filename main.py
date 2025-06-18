import pygame
from SceneGestion import SceneGestion


pygame.init()
    
screen = pygame.display.set_mode(( 0 , 0 ), pygame.FULLSCREEN) 
pygame.display.set_caption("Mastermind")
scene_gestion = SceneGestion(screen)
scene_gestion.game_loop()

 
pygame.quit()
