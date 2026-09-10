import pygame
from scene import Scene
from Button import Button
from confirmation import confirmation_popup


class WinScene(Scene):
    #scene de victoire qui affiche la combinaison gagnante ainsi que le nombre de tentatives de l'utilisateur
    #propose avec deux bouton de relancer une partie ou fermer le jeux
    def __init__(self, screen, try_number,combination):
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
        self.combination = combination
        self.try_number = try_number #nombre d'essais mis par le joueur pour gagné
        self.back_ground = pygame.image.load("code/image/background_win.png") #chargement de l'image de fond de la scene d'explication
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
        font = pygame.font.Font(None, self.screen_height//12)
        
        win_text = font.render("Félicitations !", True, (255, 255, 255))
        text_rect = win_text.get_rect(center=(self.screen_width // 2, self.screen_height // 12)) #centrage de "Félicitations !" à 1/12 de la hauteur
        self.screen.blit(win_text, text_rect)
        
        win_text2 = font.render("Vous avez gagné en ", True, (255, 255, 255))
        text2_rect = win_text2.get_rect(center=(self.screen_width // 2, self.screen_height // 5)) #centrage du texte à 1/5 de la hauteur
        self.screen.blit(win_text2, text2_rect)
        
        text_nb_Try = font.render(str(self.try_number) + "  tentative(s)", True, (255,255, 255))
        text3_rect = text_nb_Try.get_rect(center=(self.screen_width // 2, self.screen_height // 3)) #centrage du nombre de tentatives à 1/3 de la hauteur
        self.screen.blit(text_nb_Try, text3_rect)
        
        #affichage de la bonne combinaison
        nb_hole = len(self.combination)
        ball_radius = self.screen_height //20 
        space_between_ball = ball_radius//15
        size_line = 2 *ball_radius*nb_hole + (nb_hole - 1) * space_between_ball
        x_center_ball = self.screen_width //2 - size_line//2  + ball_radius #on centre et on se décale pour commencer à la bille de gauche
        y_center_ball = self.screen_height //2 
        for color in self.combination : #on affiche une bille pour chaque couleur de la combianaison
            pygame.draw.circle(self.screen, (0, 0, 0), (x_center_ball, y_center_ball) , ball_radius) #contour en noir 
            pygame.draw.circle(self.screen, color, (x_center_ball, y_center_ball), ball_radius*0.95) # bonne couleur
            x_center_ball += 2*ball_radius + space_between_ball

        self.replay_button.draw(self.screen)
        self.quit_button.draw(self.screen)
