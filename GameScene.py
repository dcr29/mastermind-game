import pygame
from scene import Scene
from Line import Line
from ColorPalette import ColorPalette

class GameScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.line = Line(screen.get_width(), screen.get_height())
        self.avaibleColor = [(0, 0, 255), (255, 192, 203), (255, 0, 0),
                             (0, 255, 0), (255, 255, 0), (255, 165, 0),
                             (238, 130, 238), (255, 255, 255)]
        self.colorPalette = ColorPalette(4, screen.get_width(), screen.get_height(), self.avaibleColor)
        self.color = None

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.color is not None:
                    valid = self.line.is_clicked(event.pos, self.color)
                    if valid:
                        print(valid)
                clicked = self.colorPalette.is_clicked(event.pos)
                if clicked:
                    self.color = clicked

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.colorPalette.draw(self.screen)
        self.line.draw(self.screen)
