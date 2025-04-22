import pygame
from SceneGestion import SceneGestion
from GameScene import GameScene

pygame.init()
    
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mastermind")

scene_gestion = SceneGestion(screen)
scene_gestion.current_scene = GameScene(screen)
scene_gestion.game_loop()

pygame.quit()
