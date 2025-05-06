import pygame
import random
from Line import Line
from ColorPalette import ColorPalette
from DoneLine import DoneLine

class GameGestion():
    def __init__(self, level, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.available_colors = [(0, 0, 255), (255, 192, 203), (255, 0, 0), (0, 255, 0)]    # (255, 255, 0), (255, 165, 0), (238, 130, 238), (255, 255, 255)] autres couleurs pour autres niveaux
        self.line = Line(screen_width, screen_height)
        self.colorPalette = ColorPalette(4, screen_width, screen_height, self.available_colors)
        self.color = None
        self.last_done_line = None 
        
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
    
    def verify_combination(self, proposed_combination):
        correctCount = 0 
        wrongPlaceCount = 0
        used_index_secret = []
        used_index_proposed = []
        
        # Recherche des bonnes couleurs bien placées 
        for i in range(len(self.combination)):
            if self.combination[i] == proposed_combination[i]:
                correctCount += 1
                used_index_secret.append(i)
                used_index_proposed.append(i)
        
        # Recherche des bonnes couleurs mal placées
        for i in range(len(self.combination)):
            for j in range(len(proposed_combination)):
                if self.combination[i] == proposed_combination[j]:
                    if (i in used_index_secret) or (j in used_index_proposed):
                        pass
                    else :
                        wrongPlaceCount += 1
                        used_index_secret.append(i)
                        used_index_proposed.append(j)
        
        ball_width = self.screen_width // 16
        line_width = 4 * ball_width
        x = (self.screen_width - line_width) // 2
        y = self.screen_height // 20
        self.last_done_line = DoneLine(x, y, proposed_combination, self.screen_width, self.screen_height, correctCount, wrongPlaceCount)
        self.last_done_line.move(self.last_done_line.x, self.last_done_line.y)
        
        return correctCount == len(self.combination)
                
    def draw(self, screen):
        screen.fill((255, 255, 255))
        self.colorPalette.draw(screen)
        self.line.draw(screen)
        if self.last_done_line:
            self.last_done_line.draw(screen)
        
        
        
        