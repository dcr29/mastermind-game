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
                    return ("WIN", len(self.game.doneLineGestion.DoneLines))
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



                    

                



        
class WinScene(Scene):
    def __init__(self, screen, try_number):
        super().__init__(screen)
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        replay_button_width = self.screen_width // 4
        replay_button_height = self.screen_height // 7
        replay_button_x = (self.screen_width // 2) - (replay_button_width // 2)
        replay_button_y = (self.screen_height // 2) - (replay_button_height // 2)
        self.replay_button = Button(replay_button_x, replay_button_y, replay_button_width, replay_button_height, "Rejouer ?",(23, 131, 15),50,15)
        self.try_number = try_number
        quit_button_width = self.screen_width // 4
        quit_button_height = self.screen_height // 7
        quit_button_x = replay_button_x
        quit_button_y = 1.5 * replay_button_y
        self.quit_button = Button(quit_button_x, quit_button_y, quit_button_width, quit_button_height, "Quitter le jeu ?",(255, 0, 0),50,15)
    
    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.replay_button.is_clicked(event.pos):
                    return "Menu"
                elif self.quit_button.is_clicked(event.pos):
                    if confirmation_popup(self.screen, "Quitter le jeu ?"):
                        return "fin"

    def draw(self):
        self.screen.fill((7, 67, 102))
        font = pygame.font.Font(None, 80)
        
        win_text = font.render("Félicitations !", True, (255, 255, 255))
        text_rect = win_text.get_rect(center=(self.screen_width // 2, self.screen_height // 10))
        self.screen.blit(win_text, text_rect)
        
        win_text2 = font.render("Vous avez gagné en ", True, (255, 255, 255))
        text2_rect = win_text2.get_rect(center=(self.screen_width // 2, self.screen_height // 5))
        self.screen.blit(win_text2, text2_rect)
        
        text_nb_Try = font.render(str(self.try_number) + "  tentative(s)", True, (255,255, 255))
        text3_rect = text_nb_Try.get_rect(center=(self.screen_width // 2, self.screen_height // 3))
        self.screen.blit(text_nb_Try, text3_rect)
        
        self.replay_button.draw(self.screen)
        self.quit_button.draw(self.screen)

class ExplanationScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        screen_width = screen.get_width()
        self.menu_button = Button(19*screen_width/20, 0,screen_width/20, screen_width/20, "menu",(255, 0, 0),screen_width//40,10)

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1:
                if self.menu_button.is_clicked(event.pos):
                    if confirmation_popup(self.screen, "Retourner au menu ?"):
                        return "Menu"

    def draw(self):
        self.screen.fill((7, 67, 102))
        self.menu_button.draw(self.screen)
        #titre
        font_haut = pygame.font.Font("Font/Coolvetica.otf", 80)
        text_haut = font_haut.render("Bienvenue sur Mastermind", True, (0, 255, 255))
        text_haut_x = (self.screen.get_width() // 2) - (text_haut.get_width() // 2)
        text_y = self.screen.get_height() // 12
        self.screen.blit(text_haut, (text_haut_x,text_y))  # Afficher texte en haut de l'écran
        text_y += font_haut.get_height()*1.8

        #paragraphe
        font_paragraphe = pygame.font.Font("Font/Coolvetica.otf", 24)

        lines = ["Voici les règles du jeu Mastermind",
        "Le but du jeu est de trouver la combinaison de couleurs de billes choisie par l'ordinateur aléatoirement en un minimum d'essais.",
        "Trouver la bonne combinaison de billes revient à trouver la bonne position et la bonne couleur de chaque bille.",
        "Il existe plusieurs niveaux :",
        "       Facile              : 4 trous et 4 couleurs",
        "       Moyen            : 4 trous et 6 couleurs",
        "       Difficile           : 4 trous et 8 couleurs",
        "       Personnalisé   : A toi de choisir entre 2 à 8 trous et couleurs",
        " ",
        "Tu peux valider ta ligne lorsque tu as remplit tous les trous avec une couleur",
        "Après validation, tes anciennes lignes apparaissent en haut. À leur gauche s affiche ton nombre d éssais.",
        "À leur droite, en vert : le nombre de couleurs bien placées ; en orange : le nombre de bonnes couleurs mal placées.",
        " ",
        " ",
        " ",
        " "]

        for line in lines:
            line_text = font_paragraphe.render(line, True, (255, 255, 255))
            self.screen.blit(line_text, (self.screen.get_width() // 10 ,text_y))
            text_y += font_paragraphe.get_height()*1.3
        
        #affichage bonne partie en bas
        text_GG = font_haut.render("Bonne partie !!", True, (0, 255, 255))
        text_GG_x = (self.screen.get_width() // 2) - (text_GG.get_width() // 2)
        self.screen.blit(text_GG, (text_GG_x, self.screen.get_height() - text_GG.get_height()*1.5))  # Afficher texte en haut de l'écran



    
    
