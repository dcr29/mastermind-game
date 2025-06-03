import pygame
from Button import Button

def confirmation_popup(screen, message):
    font = pygame.font.Font(None, 36)
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    # Zone de l'affichage de la confirmation
    popup_width = screen_width // 2
    popup_height = screen_height // 3
    popup_x = (screen_width - popup_width) // 2
    popup_y = (screen_height - popup_height) // 2
    popup_rect = pygame.Rect(popup_x, popup_y, popup_width, popup_height)

    # Boutons
    yes_button = Button(popup_x+popup_width/5, popup_y+4*popup_height/6, popup_width/5, popup_height/6, "Oui", (0, 200, 0), 30)
    no_button = Button(popup_x+3*popup_width/5, popup_y+4*popup_height/6, popup_width/5, popup_height/6, "Non", (200, 0, 0), 30)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Ne quitte pas immédiatement
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if yes_button.is_clicked(event.pos):
                    return True
                elif no_button.is_clicked(event.pos):
                    return False
        # Cadre popup
        pygame.draw.rect(screen, (240, 240, 240), popup_rect)
        pygame.draw.rect(screen, (0, 0, 0), popup_rect, 3)
        # Message
        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(center=(popup_rect.centerx, popup_rect.y + 40))
        screen.blit(text, text_rect)
        # Dessin des boutons
        yes_button.draw(screen)
        no_button.draw(screen)

        pygame.display.flip()
