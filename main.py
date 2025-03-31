import pygame
from Ball import Ball
from Button import Button

pygame.init()
    
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mastermind")

screen.fill((255, 255, 255))
button = Button(500, 500, 50, 50, "Jouer", (255, 0, 0), 20)
ball1 = Ball(400,300,50,(255,0,255))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:    # si clic
            if event.button == 1:   # si c'est un clic gauche
                ball1.is_clicked(event.pos)
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_clicked(event.pos):
                print("Clic détécté sur le bouton")

    button.draw(screen)        
    ball1.draw(screen)
    
    pygame.display.flip()

pygame.quit()