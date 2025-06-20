import pygame

class Button:
    
    def __init__(self, x, y, width, height, text, color, font_size, b_radius):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.image = None
        self.color = color
        self.font_size = font_size
        self.border_radius = b_radius
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=self.border_radius)
        if self.image:  # Si une image est définie, on adapte ses dimensions à celles du bouton
            resized_image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height)) 
            img_rect = resized_image.get_rect(center=self.rect.center)
            screen.blit(resized_image, img_rect)
        else :
            font = pygame.font.Font("Font/Coolvetica.otf", self.font_size)
            text_surface = font.render(self.text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=self.rect.center)  
            screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def put_image(self,image_directory):
        self.image = pygame.image.load(image_directory)