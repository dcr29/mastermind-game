import pygame
from Ball import Ball

class ColorPalette : 
    def __init__(self, nb_ball, screen_width, screen_height,available_color):
        self.nb_ball=nb_ball
        self.balls=[]
        ball_radius = screen_height / 12
        x_ball = ( screen_width - nb_ball * 2 * ball_radius) / 2 + ball_radius #on centre la Colorpalette
                    #(largeur de l'écran - largeur de toute les billes)/2 et on se décale au centre de la bille
        for i in range(self.nb_ball):
            self.balls.append(Ball(x_ball, screen_height - ball_radius, ball_radius, available_color[i]))
            x_ball += 2 * ball_radius 
    
    def draw(self, screen):
        for ball in self.balls:
            ball.draw(screen) 

    def is_clicked(self, pos):
        for ball in self.balls:
            color = ball.is_clicked(pos) #la bille retourne sa couleur si elle est cliqué
            if color :
                return color
        return False