import pygame

class DoneLine:
    def __init__(self, color, screen_width, screen_height, correct_count, wrong_place_count,try_number):
        self.color = color  # liste des couleurs proposées par le joueur
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rects = [] # liste de rectangles représentants les billes
        self.ball_radius = (screen_height // 12) / 2
        self.nb_hole = len(self.color)
        self.width = screen_width // (3 * len(self.color))
        self.height = screen_height // 12
        self.correct_count = correct_count    # nombre de billes bien placées
        self.wrong_place_count = wrong_place_count  # nombre de billes mal placées
        self.try_number = try_number
        self.space_between_ball = self.ball_radius // self.nb_hole
        self.done_line_size = 2 * self.ball_radius * self.nb_hole + (self.nb_hole - 1) * self.space_between_ball

    def move(self, start_x, start_y):  # positionne les billes à partir d'un point donné
        self.x = (self.screen_width - self.done_line_size) / 2
        self.y = start_y
        self.rects = []
        
        for i in range(self.nb_hole):
            rect = pygame.Rect(self.x + i * (self.space_between_ball + 2 * self.ball_radius), self.y, 2 * self.ball_radius, 2 * self.ball_radius)
            self.rects.append(rect)
            
    def draw(self, screen): # affiche la ligne de bille et le nombre de billes bien/mal placées
        for i, rect in enumerate(self.rects):
            center = rect.center
            pygame.draw.circle(screen, self.color[i], center, self.ball_radius)
            pygame.draw.circle(screen, (0, 0, 0), center, self.ball_radius, 2)  # contour des cercles (bille) noir
        
        font = pygame.font.Font(None, self.height)
        spacing = self.ball_radius  # espacement entre le dernier cercle (dernière bille) et les chiffres
        text_x = (self.screen_width + self.done_line_size) / 2 + spacing
        text_y = self.y + self.height // 4
        
        # Affichage du nombre de billes bien placées (en vert)
        text_correct_count = font.render(str(self.correct_count), True, (0, 255, 0))
        screen.blit(text_correct_count, (text_x, text_y))
        
        # Affichage du nombre de billes mal placées (en orange)
        text_wrong_place_count = font.render(str(self.wrong_place_count), True, (255, 165, 0))
        screen.blit(text_wrong_place_count, (text_x + spacing, text_y))

        # Affichage du nombre d'essais
        font_nb_try = pygame.font.Font(None, self.height//2)
        text_nb_Try = font_nb_try.render(str(self.try_number), True, (0,0, 0))
        screen.blit(text_nb_Try, (self.x - spacing, text_y + self.height//6))