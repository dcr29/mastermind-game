import pygame
from scene import Scene
from Button import Button
from confirmation import confirmation_popup


class WinScene(Scene):
    def __init__(self, screen, try_number):
        super().__init__(screen)
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()
        #création des boutons
        button_width = self.screen_width // 4
        button_height = self.screen_height // 7
        button_x = (self.screen_width // 2) - (button_width // 2) #centrage horizontal
        button_y = 3* self.screen_height // 5
        self.replay_button = Button(button_x, button_y, button_width, button_height, "Rejouer ?",(51, 153, 255),50,15)
        self.quit_button = Button(button_x, button_y + button_height*1.5, button_width, button_height, "Quitter le jeu ?",(255, 0, 0),50,15)

        self.try_number = try_number #nombre d'essais mis par le joueur pour gagné
        self.back_ground = pygame.image.load("image/background_win.png") #chargement de l'image de fond de la scene d'explication
        self.back_ground = pygame.transform.scale(self.back_ground, (self.screen_width, self.screen_height)) #on redimensionne l'image de fond 
        


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
        self.screen.blit(self.back_ground, (0, 0))#met l'image en fond d'écran
        font = pygame.font.Font("Font/Coolvetica.otf", self.screen_height//12)
        
        win_text = font.render("Félicitations !", True, (255, 255, 255))
        text_rect = win_text.get_rect(center=(self.screen_width // 2, self.screen_height // 12)) #centrage du texte à 1/12 de la hauteur
        self.screen.blit(win_text, text_rect)
        
        win_text2 = font.render("Vous avez gagné en ", True, (255, 255, 255))
        text2_rect = win_text2.get_rect(center=(self.screen_width // 2, self.screen_height // 5)) #centrage du texte à 1/5 de la hauteur
        self.screen.blit(win_text2, text2_rect)
        
        text_nb_Try = font.render(str(self.try_number) + "  tentative(s)", True, (255,255, 255))
        text3_rect = text_nb_Try.get_rect(center=(self.screen_width // 2, self.screen_height // 3)) #centrage du texte à 1/3 de la hauteur
        self.screen.blit(text_nb_Try, text3_rect)
        
        self.replay_button.draw(self.screen)
        self.quit_button.draw(self.screen)
