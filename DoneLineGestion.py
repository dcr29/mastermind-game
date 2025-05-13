import pygame
from DoneLine import DoneLine

class DoneLineGestion():
    def __init__(self,x,y):
        self.xAll=x 
        self.yAll=y   #x et y en haut à gauche de toute les DoneLine
        self.DoneLines=[]

    def add_DoneLine(self,color,screen_width, screen_height,nbGood, nbWrongPlace):
        newValidLine = DoneLine(color,screen_width, screen_height,nbGood, nbWrongPlace)
        self.DoneLines.append(newValidLine)
        size_Doneline= 0
        for Doneline in self.DoneLines:
            size_Doneline+= Doneline.height*1.15
        if size_Doneline >= screen_height*0.520 : #si toute les doneline sont plus grande que leur espace d'affichage
            self.yAll = -1*(size_Doneline - screen_height*0.520) #on recentre avec les dernière à chaque nouvelle doneline

    def draw(self,screen):
        x=self.xAll
        y=self.yAll
        for DoneLine in self.DoneLines:
            if y > -DoneLine.height and y < screen.get_height()*0.520: #on dessine les DoneLine que au dessus de la palette et dans l'écran
                DoneLine.move(x,y)
                DoneLine.draw(screen)
            y+=DoneLine.height*1.15
