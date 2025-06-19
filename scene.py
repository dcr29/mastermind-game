import pygame
from Button import Button
from Line import Line
from ColorPalette import ColorPalette
from GameGestion import GameGestion
from confirmation import confirmation_popup
from DoneLineGestion import DoneLineGestion
from ScoreGestion import *

class Scene:
    def __init__(self, screen):
        self.screen = screen

    def handle_events(self, event):
        pass

    def draw(self):
        pass  



class GameScene(Scene):
    def __init__(self, screen, nb_colors, nb_hole, best_score):
        super().__init__(screen)
        self.game = GameGestion( self.screen.get_width(), self.screen.get_height(), nb_colors, nb_hole)
        self.best_score = best_score
        
    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                result = self.game.click(event.pos)
                if result == "WIN":
                    return ("WIN")
                elif result == "Leave":
                    if confirmation_popup(self.screen, "Quitter la partie ?"):
                        return "Menu" #si il quitte la parti on le renvoie au menu
            elif event.button==4:
                self.game.scroll("Monte")
            elif event.button==5:
                self.game.scroll("Descend")
                    
    def draw(self):
        self.game.draw(self.screen)
        if self.best_score:
            font = pygame.font.Font(None, 36)
            best_score_text = font.render("Meilleur score :" + str(self.best_score), True, (0,0,0))
            self.screen.blit(best_score_text, (10, 10))



                    

                

