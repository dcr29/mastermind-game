import pygame
from scene import Scene
from Line import Line
from ColorPalette import ColorPalette
from GameGestion import GameGestion

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
                if self.color is not None:
                    valid = self.game.line.is_clicked(event.pos, self.color)
                    if valid:
                        print(valid)
                    if isinstance(valid, list):
                        self.game.verify_combination(valid)

                clicked = self.game.colorPalette.is_clicked(event.pos)
                if clicked:
                    self.color = clicked
                    


    def draw(self):
        self.game.draw(self.screen)
        
        