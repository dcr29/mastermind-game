import pygame
from Button import Button
from Line import Line
from ColorPalette import ColorPalette
from GameGestion import GameGestion

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
        self.easy_button = Button(play_button_x, play_button_y, play_button_width, play_button_height, "Easy",(23, 131, 15),50)
        self.medium_button = Button(play_button_x, play_button_y+1.2*play_button_height, play_button_width, play_button_height, "Medium",(23, 131, 15),50)
        self.hard_button = Button(play_button_x, play_button_y+2.4*play_button_height, play_button_width, play_button_height, "Hard",(23, 131, 15),50)
        self.perso_button = Button(play_button_x, play_button_y+3.6*play_button_height, play_button_width, play_button_height, "Perso",(23, 131, 15),50)
        
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
        
    def draw(self): 
        self.screen.fill((7, 67, 102))  # Fond menu
        self.easy_button.draw(self.screen)
        self.medium_button.draw(self.screen)
        self.hard_button.draw(self.screen)
        self.perso_button.draw(self.screen)
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
                self.game.click(event.pos)
            elif event.button==4:
                self.game.scroll(0)
            elif event.button==5:
                self.game.scroll(1)
                    
    def draw(self):
        self.game.draw(self.screen)


class SettingScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.choice_nb=[]
        button_width = self.screen.get_width() // 8
        button_height = self.screen.get_height() // 7
        button_x = (self.screen.get_width() // 2) - (6*button_width // 2)
        button_y = 3*(self.screen.get_height() // 5)
        for i in range(6):
            self.choice_nb.append(Button((button_x)+ (button_width)*(i)+i*1.3, button_y, button_width, button_height, str(i+2),(23, 131, 15),50))
        self.nb_hole=0
        self.nb_hole_validate = False 
        self.nb_color=0
        self.valid_button= Button((self.screen.get_width() // 2) - (button_width // 2),button_y+button_height*1.2, button_width, button_height, "Valid", (0,255,0),20)
        self.valid_button.put_image('valid.png')



    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for i in range(6):
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
                    

                


                    
    def draw(self):
        self.screen.fill((7, 67, 102))  # Fond menu
        font = pygame.font.Font(None, 80)
        text_customisation = font.render("customisation", True, (255, 255, 255))
        text_customisation_width = text_customisation.get_width()
        text_customisation_height = text_customisation.get_height()
        text_customisation_x = (self.screen.get_width() // 2) - (text_customisation_width // 2)
        text_customisation_y = self.screen.get_height() // 12
        self.screen.blit(text_customisation, (text_customisation_x,text_customisation_y))  # Afficher "customisation" en haut de l'écran
        font2 = pygame.font.Font(None, 30)
        font3 = pygame.font.Font(None, 30)
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
        for i in range(6):
            self.choice_nb[i].draw(self.screen)
