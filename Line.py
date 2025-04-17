import pygame
import math
from Hole import Hole
from Button import Button


class Line : 
    def __init__(self, screen_width, screen_height):
        self.Holes =[]
        Hole_radius = screen_height//12
        nb_hole = 4
        space_between_hole = Hole_radius / 4   
        sizeLineHole = nb_hole*2*Hole_radius + (nb_hole-1)*space_between_hole #taille des trous + tailles des espace
        x_start_line = (screen_width -sizeLineHole)/2
        self.rect_back = pygame.Rect(x_start_line, screen_height * 0.625,sizeLineHole,Hole_radius*2 )
        for i in range (4):
            self.Holes.append(Hole(x_start_line + Hole_radius, self.rect_back.top + Hole_radius, Hole_radius, (100,100,100)))
            x_start_line += Hole_radius*2 + space_between_hole

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 150, 150), self.rect_back, border_radius=15)  # Rectangle gris avec bords arrondis
    
        for hole in self.Holes :
            hole.draw(screen)

    def is_clicked(self,pos,color):
        pass
