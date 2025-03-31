import pygame
from Ball import Ball

pygame.init()
    
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mastermind")
screen.fill((255, 255, 255))

running = True
ball1 = Ball(400,300,50,(255,0,255))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    ball1.draw(screen)
    pygame.display.flip()

pygame.quit()