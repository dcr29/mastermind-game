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
        

class GameScene(Scene):
    def __init__(self, screen, level):
        super().__init__(screen)
        self.game = GameGestion(level, self.screen.get_width(), self.screen.get_height())
        self.color = None
        
    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                result = self.game.click(event.pos)
                if result == "WIN":
                    return "WIN"
            elif event.button==4:
                self.game.scroll(0)
            elif event.button==5:
                self.game.scroll(1)
                    
    def draw(self):
        self.game.draw(self.screen)
        
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
                    return "Easy"

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


