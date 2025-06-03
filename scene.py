import pygame
from Button import Button
from Line import Line
from ColorPalette import ColorPalette
from GameGestion import GameGestion
from confirmation import confirmation_popup

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
        self.quit_button = Button(19*self.screen_width/20, 0, self.screen_width/20, self.screen_width/20, "quitter",(255, 0, 0),self.screen_width//40)

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
        
    def draw(self): 
        self.screen.fill((7, 67, 102))  # Fond menu
        self.easy_button.draw(self.screen)
        self.medium_button.draw(self.screen)
        self.hard_button.draw(self.screen)
        self.perso_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        font = pygame.font.Font(None, 80)
        text_menu = font.render("Menu", True, (255, 255, 255))
        text_menu_width = text_menu.get_width()
        text_menu_height = text_menu.get_height()
        text_menu_x = (self.screen_width // 2) - (text_menu_width // 2)
        text_menu_y = self.screen_height // 12
        self.screen.blit(text_menu, (text_menu_x,text_menu_y))  # Afficher "Menu" en haut de l'écran
        

class GameScene(Scene):
    def __init__(self, screen, nb_colors, nb_hole):
        super().__init__(screen)
        self.game = GameGestion( self.screen.get_width(), self.screen.get_height(), nb_colors, nb_hole)
        self.color = None
        
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
    def __init__(self, screen):
        super().__init__(screen)
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        replay_button_width = self.screen_width // 4
        replay_button_height = self.screen_height // 7
        replay_button_x = (self.screen_width // 2) - (replay_button_width // 2)
        replay_button_y = (self.screen_height // 2) - (replay_button_height // 2)
        self.replay_button = Button(replay_button_x, replay_button_y, replay_button_width, replay_button_height, "Rejouer ?",(255, 102, 102),50)
    
    
    
    
    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button:
                if self.replay_button.is_clicked(event.pos):
                    return "Menu"

    def draw(self):
        self.screen.fill((153, 204, 255))
        font = pygame.font.Font(None, 80)
        
        win_text = font.render("Congratulations !", True, (255, 255, 255))
        text_rect = win_text.get_rect(center=(self.screen_width // 2, self.screen_height // 6))
        self.screen.blit(win_text, text_rect)
        
        win_text2 = font.render("You have won !", True, (255, 255, 255))
        text2_rect = win_text2.get_rect(center=(self.screen_width // 2, self.screen_height // 3))
        self.screen.blit(win_text2, text2_rect)
        
        self.replay_button.draw(self.screen)

