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

    def draw(self,screen):
        x=self.xAll
        y=self.yAll
        for DoneLine in self.DoneLines:
            DoneLine.move(x,y)
            DoneLine.draw(screen)
            y+=DoneLine.height*1.15
