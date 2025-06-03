import pygame
from DoneLine import DoneLine
 
class DoneLineGestion():
    def __init__(self,y):
        self.yAll=y 
        self.DoneLines=[]

    def add_DoneLine(self,color,screen_width, screen_height,nbGood, nbWrongPlace):
        try_number=len(self.DoneLines)+1
        newValidLine = DoneLine(color,screen_width, screen_height,nbGood, nbWrongPlace,try_number)
        self.DoneLines.append(newValidLine)
        size_Doneline= 0
        for Doneline in self.DoneLines:
            size_Doneline+= Doneline.ball_radius*2.15
        if size_Doneline >= screen_height*0.520 : #si toute les doneline sont plus grande que leur espace d'affichage
            self.yAll = -1*(size_Doneline - screen_height*0.520) #on recentre avec les dernière à chaque nouvelle doneline

    def draw(self,screen):
        y=self.yAll
        for DoneLine in self.DoneLines:
            if y > -DoneLine.ball_radius*2 and y < screen.get_height()*0.520: #on dessine les DoneLine que au dessus de la palette et dans l'écran
                DoneLine.move(y) #centrage automatique
                DoneLine.draw(screen)
            y+=DoneLine.ball_radius*2.15
