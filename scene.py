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




    
    
