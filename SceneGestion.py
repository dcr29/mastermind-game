from scene import *
import pygame

class SceneGestion:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.current_scene = MenuScene(screen)
        
    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                    ret = self.current_scene.handle_events(event) # recupere la réponse de la scène actuelle
                    if ret == "fin" :
                        self.running = False
                    elif ret  == "Easy" :
                        self.current_scene = GameScene(self.screen,4,4)
                    elif ret  == "Medium" :
                        self.current_scene = GameScene(self.screen,6,4)
                    elif ret  == "Hard" :
                        self.current_scene = GameScene(self.screen,8,4)
                    elif ret == "Perso":
                        self.current_scene = SettingScene(self.screen)
                    elif  isinstance(ret, int) :
                        self.current_scene =  GameScene(self.screen,ret//10,ret%10) #le nombre de couleur est dans les dizaines et le nombre de trou dans les unites
                    elif ret == "WIN" :
                        self.current_scene = WinScene(self.screen)
                    elif ret == "Menu" :
                        self.current_scene = MenuScene(self.screen)
                    elif ret == "Explaination" :
                        self.current_scene = ExplanationScene(self.screen)
                        
            self.current_scene.draw()
            pygame.display.flip()          
                                     