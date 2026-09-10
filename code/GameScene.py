import pygame
from scene import Scene
from GameGestion import GameGestion
from confirmation import confirmation_popup

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
                    return "WIN"
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
            font_best_score = pygame.font.Font(None, self.screen.get_height()//10)
            trophy_picture = pygame.image.load('code/image/trophee_best_score.png')
            
            # Redimensionnement de l'image 'trophee_best_score.png' 
            real_width, real_height = trophy_picture.get_size()
            new_size = (real_width // 4, real_height // 4)
            new_size_trophy_picture = pygame.transform.scale(trophy_picture, new_size) # Redimensionne l'image à une nouvelle taille
            new_size_trophy_picture_width = new_size_trophy_picture.get_width()
            new_size_trophy_picture_height = new_size_trophy_picture.get_height()
            
            # Coordonnées de l'image 'trophee_best_score.png'
            x_trophy_picture = 0
            y_trophy_picture = 0
            
            # Coordonnées du nombre indiquant le meilleur score
            best_score_text_x = 1.2 * new_size_trophy_picture_width
            best_score_text_y = 0
            
            best_score_text = font_best_score.render(str(self.best_score), True, (249,199,13))
            
            self.screen.blit(best_score_text, (best_score_text_x, best_score_text_y))
            self.screen.blit(new_size_trophy_picture, (x_trophy_picture, y_trophy_picture))

