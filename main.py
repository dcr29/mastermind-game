import pygame
from ColorPalette import ColorPalette
from Button import Button
from Line import Line
from DoneLine import DoneLine

pygame.init()
    
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mastermind")

screen.fill((255, 255, 255))

# déclaration des objets :
line = Line(screen.get_width(),screen.get_height())
button = Button(750, 0, 50, 50, "END", (255, 0, 0), 20)
avaibleColor = [(0, 0, 255), (255, 192, 203), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 165, 0), (238, 130, 238), (255, 255, 255)]
colorPalette = ColorPalette(4,screen.get_width(),screen.get_height(),avaibleColor)
color=()

test_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]
done_line = DoneLine(100, 100, test_colors, 800, 600, correctCount = 2, wrongPlaceCount = 1)
done_line.move(50, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        elif event.type == pygame.MOUSEBUTTONUP: # si click
            if event.button == 1: # si c'est un click gauche
                clicked = colorPalette.is_clicked(event.pos)
                if clicked :
                    color = clicked
                if button.is_clicked(event.pos):
                    running = False #si le bouton est cliqué on arrete le jeu
                    
    colorPalette.draw(screen)
    button.draw(screen)
    line.draw(screen)
    done_line.draw(screen)

    pygame.display.flip()

pygame.quit()