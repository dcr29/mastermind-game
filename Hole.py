import pygame
import math

class Hole:
    def __init__(self, x, y, radius, color):
        self.x = x  # Position en X
        self.y = y  # Position en Y
        self.radius = radius
        self.color = color  # Couleur du trou
        

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.rayon)
        pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), self.rayon, 2)  # Contour noir

    def move(self, x, y):
        # Déplacer le trou
        self.x = x
        self.y = y

    def is_clicked(self, pos, color):
        x_clic, y_clic = pos
        distance = math.sqrt((x_clic - self.x) ** 2 + (y_clic - self.y) ** 2) #calcul de la distance entre le centre et le clique
        if distance < self.radius:
            self.color = color
