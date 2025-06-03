import pygame
import random
from Line import Line
from ColorPalette import ColorPalette
from DoneLineGestion import DoneLineGestion

class GameGestion():
    def __init__(self,  screen_width, screen_height, nb_colors, nb_hole):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.available_colors = [(0, 0, 255), (255, 192, 203), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 165, 0), (238, 130, 238), (0, 255,255)] 
        self.line = Line(screen_width, screen_height,nb_hole)
        
        self.colorSelect = None
        self.doneLineGestion = DoneLineGestion( self.screen_width//2,self.screen_height * 0.02) 


        self.colorPalette = ColorPalette(nb_colors, screen_width, screen_height, self.available_colors)
        #creation de la combinaison
        self.combination = []
        for i in range(nb_hole):
            self.combination.append(self.available_colors[random.randint(0,nb_colors-1)])
    

    
    def verify_combination(self, proposed_combination):
        correct_count = 0 
        wrong_place_count = 0
        used_index_secret = []
        used_index_proposed = []
        
        # Recherche des bonnes couleurs bien placées 
        for i in range(len(self.combination)):
            if self.combination[i] == proposed_combination[i]:
                correct_count += 1
                used_index_secret.append(i)
                used_index_proposed.append(i)
        
        # Recherche des bonnes couleurs mal placées
        for i in range(len(self.combination)):
            for j in range(len(proposed_combination)):
                if self.combination[i] == proposed_combination[j]:
                    if (i in used_index_secret) or (j in used_index_proposed):
                        pass
                    else :
                        wrong_place_count += 1
                        used_index_secret.append(i)
                        used_index_proposed.append(j)
        
        ball_width = self.screen_width // 16
        line_width = 4 * ball_width
        x = (self.screen_width - line_width) // 2
        y = self.screen_height // 20
        self.doneLineGestion.add_DoneLine(proposed_combination, self.screen_width, self.screen_height, correct_count, wrong_place_count)
        return correct_count == len(self.combination)
                
    def draw(self, screen):
        screen.fill((255, 255, 255))
        self.colorPalette.draw(screen)
        self.line.draw(screen)
        if self.doneLineGestion.DoneLines:
            self.doneLineGestion.draw(screen)

    def click(self,pos):
            if self.colorSelect is not None:
                comb_validated = self.line.is_clicked(pos, self.colorSelect)
                if isinstance(comb_validated, list): # si la combinaison validée est bien une liste
                    success = self.verify_combination(comb_validated)
                    self.colorSelect = None # une fois la ligne validée on reset la couleur choisie
                    if(success):
                        return "WIN"       
            color_clicked = self.colorPalette.is_clicked(pos)
            if color_clicked: # si le joueur a cliqué sur une couleur de la palette
                self.colorSelect = color_clicked
            
                
    def scroll(self,type):
        if (self.doneLineGestion.DoneLines) :
            size_Doneline= 0
            for Doneline in self.doneLineGestion.DoneLines:
                size_Doneline+= Doneline.height*1.15 #taille de toute les DoneLine                
            ymax = 0 
            ymin = -1*(size_Doneline - self.screen_height * 0.520)
            speed_scroll = self.screen_height/30
            if type==0 :
                if self.doneLineGestion.yAll >ymin: #arrette le scroll lorsque le dernier essais en bas 
                    self.doneLineGestion.yAll -=speed_scroll 
            elif type ==1:
                if self.doneLineGestion.yAll <ymax: #arrete le scroll lorsque que le premier essais est en haut de l'écran
                    self.doneLineGestion.yAll +=speed_scroll 
        
        