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
avaibleColor = [(0, 0, 255), (255, 192, 203), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 165, 0), (238, 130, 238), (255, 255, 255)]
colorPalette = ColorPalette(4,screen.get_width(),screen.get_height(),avaibleColor)
color=None
doneLine=None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        elif event.type == pygame.MOUSEBUTTONUP: # si click
            if event.button == 1: # si c'est un click gauche
                if color != None :
                    valid = line.is_clicked(event.pos , color)
                    if valid : 
                        print(valid)
                clicked = colorPalette.is_clicked(event.pos)
                if clicked :
                    color = clicked
                
                    
    colorPalette.draw(screen)
    line.draw(screen)
    #doneLine.draw(screen)

    pygame.display.flip()

pygame.quit()