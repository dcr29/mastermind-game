import pygame

class DoneLine:
    def __init__(self, color, screen_width, screen_height, correctCount, wrongPlaceCount,try_number):
        self.color = color  # liste des couleurs proposées par le joueur
        self.rects = [] # liste de rectangles représentants les billes
        self.width = screen_width // 16 
        self.height = screen_height // 12
        self.correctCount = correctCount    # nombre de billes bien placées
        self.wrongPlaceCount = wrongPlaceCount  # nombre de billes mal placées
        self.try_number=try_number

    def move(self, start_x, start_y):  # positionne les rectangles (billes) à partir d'un point donné
        self.x = start_x
        self.y = start_y
        self.rects = [] #reset de la liste de rect
        for i in range(4):
            rect = pygame.Rect(self.x + i * self.width, self.y, self.width, self.height)
            self.rects.append(rect)
            
    def draw(self, screen): # affiche la ligne de bille et le nombre de billes bien/mal placées

        for i, rect in enumerate(self.rects):
            pygame.draw.rect(screen, self.color[i], rect)
        
        font = pygame.font.Font(None, self.height)
        spacing = self.width // 2   # espacement entre le dernier carré (dernière bille) et les chiffres
        text_x = self.x + (self.width * 4) + spacing // 2
        text_y = self.y + self.height // 6 
        
        # Affichage du nombre de billes bien placées (en vert)
        text_correctCount = font.render(str(self.correctCount), True, (0, 255, 0))
        screen.blit(text_correctCount, (text_x, text_y))
        
        # Affichage du nombre de billes mal placées (en orange)
        text_wrongPlaceCount = font.render(str(self.wrongPlaceCount), True, (255, 165, 0))
        screen.blit(text_wrongPlaceCount, (text_x + spacing, text_y))

        # Affichage du nombre d'essais'
        text_nb_Try = font.render(str(self.try_number), True, (0,0, 0))
        screen.blit(text_nb_Try, (self.x - spacing, text_y))