from scene import *
import pygame
from ScoreGestion import *

class SceneGestion:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.current_scene = MenuScene(screen)
        self.best_score = load_score()
        self.last_scene_launched = None 
        
        
        
    
    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                    ret = self.current_scene.handle_events(event)
                    if ret == "fin" :
                        self.running = False
                    elif ret  == "Easy" :
                        self.last_scene_launched = "Easy"
                        self.best_score_easy = self.best_score.get("Easy")
                        self.current_scene = GameScene(self.screen,4,4, self.best_score_easy)
                    elif ret  == "Medium" :
                        self.last_scene_launched = "Medium"
                        self.best_score_medium = self.best_score.get("Medium")
                        self.current_scene = GameScene(self.screen,6,4, self.best_score_medium)
                    elif ret  == "Hard" :
                        self.last_scene_launched = "Hard"
                        self.best_score_hard = self.best_score.get("Hard")
                        self.current_scene = GameScene(self.screen,8,4, self.best_score_hard)
                    elif ret == "Perso":
                        self.current_scene = SettingScene(self.screen)
                        self.last_scene_launched = None
                    elif  isinstance(ret, int) :
                        self.current_scene =  GameScene(self.screen,ret//10,ret%10, None) #le nombre de couleur est dans les dizaines et le nombre de trou dans les unites
                        self.last_scene_launched = None
                    elif isinstance(ret, tuple) and ret[0] == "WIN" :
                        try_number = ret[1]
                        if self.last_scene_launched in self.best_score:
                            current_best_score = self.best_score[self.last_scene_launched]
                            if current_best_score is None or try_number < current_best_score:
                                self.best_score[self.last_scene_launched] = try_number 
                                save_score(self.best_score)
                        self.current_scene = WinScene(self.screen, try_number)
                    elif ret == "Menu" :
                        self.current_scene = MenuScene(self.screen)
                    elif ret == "Explaination" :
                        self.current_scene = ExplanationScene(self.screen)
            
            self.current_scene.draw()
            pygame.display.flip()          
                                     