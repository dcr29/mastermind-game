import pygame
from Button import Button
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
        play_button_y = (self.screen_height // 2) - (play_button_height // 2)
        self.play_button = Button(play_button_x, play_button_y, play_button_width, play_button_height, "Jouer",(23, 131, 15),50)
        
    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.play_button.is_clicked(event.pos):
                    return "Easy"  # Changer de scène vers le jeu en easy
        
    def draw(self): 
        self.screen.fill((7, 67, 102))  # Fond menu
        self.play_button.draw(self.screen)
        font = pygame.font.Font(None, 80)
        text_menu = font.render("Menu", True, (255, 255, 255))
        text_menu_width = text_menu.get_width()
        text_menu_height = text_menu.get_height()
        text_menu_x = (self.screen_width // 2) - (text_menu_width // 2)
        text_menu_y = self.screen_height // 12
        self.screen.blit(text_menu, (text_menu_x,text_menu_y))  # Afficher "Menu" en haut de l'écran
        
