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
        x = (screen_width -sizeLineHole)/2
        self.rect_back = pygame.Rect(x, screen_height * 0.625,sizeLineHole,Hole_radius*2 )
        for i in range (4):
            self.Holes.append(Hole(x + Hole_radius, self.rect_back.top + Hole_radius, Hole_radius, (100,100,100)))
            x += Hole_radius*2 + space_between_hole

        x_bouton = x + Hole_radius
        y_bouton = screen_height * 0.625 + Hole_radius/2 
        #self.valid_button= Bouton(screen_width - marge + espace_entre_trou / 2, screen_height * 0.65, bouton_width, bouton_height, "Valid", (0,255,0))
        self.valid_button= Button(x_bouton, y_bouton, Hole_radius, Hole_radius, "Valid", (0,255,0),20)
        self.valid_button.put_image('valid.png')

    def draw(self, screen):
        pygame.draw.rect(screen, (150, 150, 150), self.rect_back, border_radius=15)  # Rectangle gris avec bords arrondis
    
        for hole in self.Holes :
            hole.draw(screen)
        self.valid_button.draw(screen)

    def is_clicked(self, pos, color):
        for hole in self.Holes :
            hole.is_clicked(pos,color)
        if self.valid_button.is_clicked(pos):
            for hole in self.Holes :
                if hole.color == (100,100,100):#si une case pas remplie on n'accepte pas la validation
                    return False
            valid_comb = []
            for hole in self.Holes :
                    valid_comb.append(hole.color)
                    hole.color = (100,100,100) #reset de la couleur des trous
            return valid_comb
