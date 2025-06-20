import pygame
from MenuScene import MenuScene
from GameScene import GameScene
from ExplanationScene import ExplanationScene
from SettingScene import SettingScene
from ScoreGestion import *
from Winscene import WinScene

class SceneGestion:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.current_scene = MenuScene(screen)
        self.best_scores = load_score()
        self.last_game_launched = None 
        
        
        
    
    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                    ret = self.current_scene.handle_events(event)
                    if ret == "fin" :
                        self.running = False
                    elif ret  == "Easy" :
                        self.best_score_easy = self.best_scores.get("Easy")
                        self.current_scene = GameScene(self.screen,4,4, self.best_score_easy)
                        self.last_game_launched = "Easy" 
                    elif ret  == "Medium" :
                        self.best_score_medium = self.best_scores.get("Medium")
                        self.current_scene = GameScene(self.screen,6,4, self.best_score_medium)
                        self.last_game_launched = "Medium"
                    elif ret  == "Hard" :
                        self.best_score_hard = self.best_scores.get("Hard")
                        self.current_scene = GameScene(self.screen,8,4, self.best_score_hard)
                        self.last_game_launched = "Hard"
                    elif ret == "Perso":
                        self.current_scene = SettingScene(self.screen)
                    elif  isinstance(ret, int) :
                        self.current_scene =  GameScene(self.screen,ret//10,ret%10, None) #le nombre de couleur est dans les dizaines et le nombre de trou dans les unites
                        self.last_game_launched = "Perso"
                    elif ret == "WIN":
                        try_number =len(self.current_scene.game.doneLineGestion.DoneLines) #récupération du nombre de tentative de l'utilisateur
                        #gestion du meilleur score 
                        if self.last_game_launched in self.best_scores:#si c'est une partie où l'on stock nos données
                            current_best_score = self.best_scores[self.last_game_launched] #récupération du meilleur score dans le type de partie effectué 
                            if current_best_score is None or try_number < current_best_score: # si le score réalisé par le joueur est mieux 
                                self.best_scores[self.last_game_launched] = try_number #on met à jour
                                save_score(self.best_scores)
                        combination = self.current_scene.game.combination   #récupération de la combianaison gagnante
                        self.current_scene = WinScene(self.screen, try_number,combination)
                    elif ret == "Menu" :
                        self.current_scene = MenuScene(self.screen)
                    elif ret == "Explaination" :
                        self.current_scene = ExplanationScene(self.screen)
        
            
            self.current_scene.draw()
            pygame.display.flip()          
                                     