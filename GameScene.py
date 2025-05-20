import pygame
from scene import Scene
from Line import Line
from ColorPalette import ColorPalette
from GameGestion import GameGestion

class GameScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.game = GameGestion("Easy", self.screen.get_width(), self.screen.get_height())
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
        