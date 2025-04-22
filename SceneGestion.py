from scene import *
from GameScene import GameScene
import pygame

class SceneGestion:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.current_scene = GameScene(self.screen)
        
    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                    ret = self.current_scene.handle_events(event) # recupere la réponse de la scène actuelle
                    if ret == "fin" :
                        self.running = False
            self.current_scene.draw()
            pygame.display.flip()                                   