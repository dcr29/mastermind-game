import pygame
from scene import Scene
from Button import Button
from confirmation import confirmation_popup

class MenuScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        play_button_width = self.screen_width // 4
        play_button_height = self.screen_height // 7
        play_button_x = (self.screen_width // 2) - (play_button_width // 2)
        play_button_y = (self.screen_height // 2) - (4*play_button_height // 2)
        self.easy_button = Button(play_button_x, play_button_y, play_button_width, play_button_height, "Facile",(23, 131, 15),50,15)
        self.medium_button = Button(play_button_x, play_button_y+1.3*play_button_height, play_button_width, play_button_height, "Moyen",(255, 128, 0),50,15)
        self.hard_button = Button(play_button_x, play_button_y+2.6*play_button_height, play_button_width, play_button_height, "Difficile",(255, 0, 0),50,15)
        self.perso_button = Button(play_button_x, play_button_y+3.9*play_button_height, play_button_width, play_button_height, "Personalisable",(255, 0, 255),40,15)
        self.quit_button = Button(19*self.screen_width/20, 0, self.screen_width/20, self.screen_width/20, "quitter",(55, 0, 255),self.screen_width//70,50)
        self.help_button = Button(19*self.screen_width/20, self.screen_height - self.screen_width/20, self.screen_width/20, self.screen_width/20, "aide",(0, 255, 255),self.screen_width//60,50)
        self.back_ground = pygame.image.load("code/image/background_menu.png") #chargement de l'image de fond du Menu
        self.back_ground = pygame.transform.scale(self.back_ground, (self.screen_width, self.screen_height)) #on redimensionne l'image de fond du menu 


    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #si click gauche relaché
                if self.easy_button.is_clicked(event.pos):
                    return "Easy"  # Changer de scène vers le jeu en easy
                elif self.medium_button.is_clicked(event.pos):
                    return "Medium"  # Changer de scène vers le jeu en medium
                elif self.hard_button.is_clicked(event.pos):
                    return "Hard"  # Changer de scène vers le jeu en hard
                elif self.perso_button.is_clicked(event.pos):
                    return "Perso"  # Changer de scène vers le jeu en easy
                elif self.quit_button.is_clicked(event.pos):
                    if confirmation_popup(self.screen, "Quitter le jeu ?"): #ouvre une confirmation qui est True si le joueur veut quitter et False si il refuse
                        return "fin"
                elif self.help_button.is_clicked(event.pos):
                    return "Explaination" #Changer de scène vers la scene des expliactions
        
    def draw(self): 
        self.screen.blit(self.back_ground, (0, 0))#met l'image en fond d'écran
        #on dessine tous les boutons 
        self.easy_button.draw(self.screen)
        self.medium_button.draw(self.screen)
        self.hard_button.draw(self.screen)
        self.perso_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        self.help_button.draw(self.screen)
        #on affiche "Menu" en haut de l'écran
        font = pygame.font.Font("code/Font/Coolvetica.otf", 80)
        text_menu = font.render("Menu", True, (255, 255, 255))
        text_menu_width = text_menu.get_width()
        text_menu_x = (self.screen_width // 2) - (text_menu_width // 2)
        text_menu_y = self.screen_height // 20
        self.screen.blit(text_menu, (text_menu_x,text_menu_y))
