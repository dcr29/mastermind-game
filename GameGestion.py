import pygame
import random
from Line import Line
from ColorPalette import ColorPalette

class GameGestion():
    def __init__(self, level, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.available_colors = [(0, 0, 255), (255, 192, 203), (255, 0, 0), (0, 255, 0)] #(255, 255, 0), (255, 165, 0), (238, 130, 238), (255, 255, 255)] autres couleurs pour autres nivraux
        self.line = Line(screen_width, screen_height)
        self.colorPalette = ColorPalette(4, screen_width, screen_height, self.available_colors)
        self.color = None
        
        # Définition du nombre de couleurs disponibles selon le niveau
        if level == "Easy":
            self.nb_colors = 4
        elif level == "Medium":
            self.nb_colors = 6
        else:
            self.nb_colors = 4
        
        self.combination = []
        for i in range(self.nb_colors):
            selected_colors = random.choice(self.available_colors)
            self.combination.append(selected_colors)

    def get_combination(self): # fonction de test
        return self.combination
    
    def draw(self, screen):
        screen.fill((255, 255, 255))
        self.colorPalette.draw(screen)
        self.line.draw(screen)
        
        
        