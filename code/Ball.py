import pygame

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x  # Position en X
        self.y = y  # Position en Y
        self.radius = radius  # Rayon du cercle
        self.color = color  # Couleur de la bille

    def draw(self, screen):
        # Dessiner la bille sur l'écran centrer en x et y 
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        # Vérifie si le clic est dans la bille
        #si oui retourne la couleur de la bille sinon retourne False
        distance = ((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2) ** 0.5 #calcul de la distance entre la position du click et le centre
        if distance <= self.radius:
            return self.color
        return False
