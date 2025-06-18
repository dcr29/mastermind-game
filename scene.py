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

class MenuScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        play_button_width = self.screen_width // 4
        play_button_height = self.screen_height // 7
        play_button_x = (self.screen_width // 2) - (play_button_width // 2)
        play_button_y = (self.screen_height // 2) - (4*play_button_height // 2)
        self.easy_button = Button(play_button_x, play_button_y, play_button_width, play_button_height, "Facile",(23, 131, 15),50)
        self.medium_button = Button(play_button_x, play_button_y+1.2*play_button_height, play_button_width, play_button_height, "Moyen",(23, 131, 15),50)
        self.hard_button = Button(play_button_x, play_button_y+2.4*play_button_height, play_button_width, play_button_height, "Difficile",(23, 131, 15),50)
        self.perso_button = Button(play_button_x, play_button_y+3.6*play_button_height, play_button_width, play_button_height, "Personalisable",(23, 131, 15),30)
        self.quit_button = Button(19*self.screen_width/20, 0, self.screen_width/20, self.screen_width/20, "quitter",(55, 0, 255),self.screen_width//50)
        self.help_button = Button(19*self.screen_width/20, self.screen_height - self.screen_width/20, self.screen_width/20, self.screen_width/20, "help",(55, 0, 255),self.screen_width//40)

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.easy_button.is_clicked(event.pos):
                    return "Easy"  # Changer de scène vers le jeu en easy
                elif self.medium_button.is_clicked(event.pos):
                    return "Medium"  # Changer de scène vers le jeu en medium
                elif self.hard_button.is_clicked(event.pos):
                    return "Hard"  # Changer de scène vers le jeu en hard
                elif self.perso_button.is_clicked(event.pos):
                    return "Perso"  # Changer de scène vers le jeu en easy
                elif self.quit_button.is_clicked(event.pos):
                    if confirmation_popup(self.screen, "Quitter le jeu ?"):
                        return "fin"
                elif self.help_button.is_clicked(event.pos):
                    return "Explaination"
        
    def draw(self): 
        self.screen.fill((7, 67, 102))  # Fond menu
        self.easy_button.draw(self.screen)
        self.medium_button.draw(self.screen)
        self.hard_button.draw(self.screen)
        self.perso_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        self.help_button.draw(self.screen)
        font = pygame.font.Font(None, 80)
        text_menu = font.render("Menu", True, (255, 255, 255))
        text_menu_width = text_menu.get_width()
        text_menu_x = (self.screen_width // 2) - (text_menu_width // 2)
        text_menu_y = self.screen_height // 12
        self.screen.blit(text_menu, (text_menu_x,text_menu_y))  # Afficher "Menu" en haut de l'écran
        

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



class SettingScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.choice_nb=[]
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        button_width = screen_width // 8
        button_height = screen_height // 7
        button_x = (screen_width // 2) - (7*button_width // 2)
        button_y = 3*(screen_height // 5)
        for i in range(7):
            self.choice_nb.append(Button((button_x)+ (button_width)*(i)+i*1.3, button_y, button_width, button_height, str(i+2),(23, 131, 15),50))
        self.nb_hole=0
        self.nb_hole_validate = False 
        self.nb_color=0
        self.valid_button= Button((screen_width // 2) - (button_width // 2),button_y+button_height*1.2, button_width, button_height, "Valid", (0,255,0),20)
        self.valid_button.put_image('valid.png')
        self.menu_button = Button(19*screen_width/20, 0,screen_width/20, screen_width/20, "menu",(255, 0, 0),screen_width//40)

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1:
                for i in range(7):
                    if self.choice_nb[i].is_clicked(event.pos):
                        
                        if(self.nb_hole_validate==False):
                            self.nb_hole=i+2
                        else:
                            self.nb_color=i+2
                if(self.valid_button.is_clicked(event.pos)):
                    if(self.nb_hole_validate==False):
                        self.nb_hole_validate = True
                    else :
                         return self.nb_color*10 + self.nb_hole 
                elif self.menu_button.is_clicked(event.pos):
                    if confirmation_popup(self.screen, "Retourner au menu ?"):
                        return "Menu"
                    

                


                    
    def draw(self):
        self.screen.fill((7, 67, 102))  # Fond menu
        font = pygame.font.Font(None, 80)
        text_customisation = font.render("customisation", True, (255, 255, 255))
        text_customisation_width = text_customisation.get_width()
        text_customisation_x = (self.screen.get_width() // 2) - (text_customisation_width // 2)
        text_customisation_y = self.screen.get_height() // 12
        self.screen.blit(text_customisation, (text_customisation_x,text_customisation_y))  # Afficher "customisation" en haut de l'écran
        self.menu_button.draw(self.screen)
        font2 = pygame.font.Font(None, 30)
        if(self.nb_hole==0):
            text_choix = font2.render("Veuillez choisir le nombre de trou", True, (255, 255, 255))
            self.screen.blit(text_choix, ((self.screen.get_width() // 2) - (text_choix.get_width() // 2),2*self.screen.get_height()/5))
        elif(self.nb_hole!=0 and self.nb_hole_validate == False):
            text_choix = font2.render("Veuillez choisir le nombre de trou", True, (255, 255, 255))
            self.screen.blit(text_choix, ((self.screen.get_width() // 2) - (text_choix.get_width() // 2),2*self.screen.get_height()/5))
            self.valid_button.draw(self.screen)
        elif(self.nb_color==0 and self.nb_hole_validate == True):
            text_choix = font2.render("Veuillez choisir le nombre de couleur", True, (255, 255, 255))
            self.screen.blit(text_choix, ((self.screen.get_width() // 2) - (text_choix.get_width() // 2),2*self.screen.get_height()/5))
        else:
            text_choix = font2.render("Veuillez choisir le nombre de couleur", True, (255, 255, 255))
            self.screen.blit(text_choix, ((self.screen.get_width() // 2) - (text_choix.get_width() // 2),2*self.screen.get_height()/5))
            self.valid_button.draw(self.screen)

        #affichage des boutons :
        for i in range(7):
            if self.nb_hole_validate == False :
                if i == self.nb_hole-2 :
                    self.choice_nb[i].color = (9,52,6)
                else :
                    self.choice_nb[i].color = (23, 131, 15)
            else :
                if i == self.nb_color-2 :
                    self.choice_nb[i].color = (9,52,6)
                else :
                    self.choice_nb[i].color = (23, 131, 15)
            self.choice_nb[i].draw(self.screen)    

        
class WinScene(Scene):
    def __init__(self, screen, try_number):
        super().__init__(screen)
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        replay_button_width = self.screen_width // 4
        replay_button_height = self.screen_height // 7
        replay_button_x = (self.screen_width // 2) - (replay_button_width // 2)
        replay_button_y = (self.screen_height // 2) - (replay_button_height // 2)
        self.replay_button = Button(replay_button_x, replay_button_y, replay_button_width, replay_button_height, "Rejouer ?",(23, 131, 15),50)
        self.try_number = try_number
        quit_button_width = self.screen_width // 4
        quit_button_height = self.screen_height // 7
        quit_button_x = replay_button_x
        quit_button_y = 1.5 * replay_button_y
        self.quit_button = Button(quit_button_x, quit_button_y, quit_button_width, quit_button_height, "Quitter le jeu ?",(255, 0, 0),50)
    
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
        self.menu_button = Button(19*screen_width/20, 0,screen_width/20, screen_width/20, "menu",(255, 0, 0),screen_width//40)

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
        font_haut = pygame.font.Font(None, 80)
        text_haut = font_haut.render("Bienvenue sur Mastermind", True, (0, 255, 255))
        text_haut_x = (self.screen.get_width() // 2) - (text_haut.get_width() // 2)
        text_y = self.screen.get_height() // 12
        self.screen.blit(text_haut, (text_haut_x,text_y))  # Afficher texte en haut de l'écran
        text_y += font_haut.get_height()*2.5

        #paragraphe
        font_paragraphe = pygame.font.Font(None, 24)

        lines = ["Voici les regles du jeu Mastermind",
        "Le but du jeu est de trouver la combinaison de couleurs de billes choisie par l'ordinateur aleatoirement en un minimum d'essais.",
        "Trouver la bonne combinaison de billes revient à trouver la bonne position et la bonne couleur de chaque bille.",
        "Il existe plusieurs niveaux :",
        "       Facile         : 4 trous et 4 couleurs",
        "       Moyen          : 4 trous et 6 couleurs",
        "       Difficile      : 4 trous et 8 couleurs",
        "       Personnalisé   :  A toi de choisir entre 2 et 8 trou et couleurs",
        " ",
        "Tu peux valider ta ligne lorsque que tu as remplis tout les trous avec une couleur",
        "Apres validation tes anciennes lignes apparaissent en haut avec elle à gauche c'est ton nombre d'éssais qui s'affiche ",
        "à leur droite en vert le nombre de couleur bien placé et en orange le nombre de bonne couleur mais mal placé",
        " ",
        " ",
        " ",
        " "]

        for line in lines:
            line_text = font_paragraphe.render(line, True, (255, 255, 255))
            self.screen.blit(line_text, (self.screen.get_width() // 10 ,text_y))
            text_y += font_paragraphe.get_height()*1.5
        
        #affichage bonne partie en bas
        text_GG = font_haut.render("Bonne partie !!", True, (0, 255, 255))
        text_GG_x = (self.screen.get_width() // 2) - (text_GG.get_width() // 2)
        self.screen.blit(text_GG, (text_GG_x, self.screen.get_height() - text_GG.get_height()*1.5))  # Afficher texte en haut de l'écran



    
    
