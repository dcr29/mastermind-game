import pygame
from scene import Scene
from Button import Button
from confirmation import confirmation_popup


class SettingScene(Scene):
    #scene pour paramétrer les parties où l'on personnalise 
    #on peut retourner au menu avec un bouton 
    # on choisis le nombre de trou et couleur à l'aide de 6 bouton centré et d'un bouton pour valider
    def __init__(self, screen):
        super().__init__(screen)
        self.choice_nb=[]
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        button_side = screen_width // 10
        button_x = (screen_width // 2) - (7*button_side*1.1 // 2) #centrage des boutons
        button_y = 3*(screen_height // 6)
        for i in range(7): #on va créer 6 boutons pour choisir les valeurs du nombre de trous et couleurs
            self.choice_nb.append(Button((button_x)+ (button_side*1.1)*(i), button_y, button_side, button_side, str(i+2),(255, 255, 255),50,9)) 
        self.nb_hole=0
        self.nb_hole_validate = False 
        self.nb_color=0
        self.valid_button= Button((screen_width // 2) - (button_side // 2),button_y+button_side*1.2, button_side, button_side, "Valid", (0,255,0),20,15)
        self.valid_button.put_image('image/valid.png')
        self.menu_button = Button(19*screen_width/20, 0,screen_width/20, screen_width/20, "menu",(0,128, 255),screen_width//60,50)
        self.back_ground = pygame.image.load("image/background_degrade.png") #chargement de l'image de fond de la scene d'explication, on met le meme 
        self.back_ground = pygame.transform.scale(self.back_ground, (screen_width, self.screen.get_height())) #on redimensionne l'image de fond 
        


    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1:
                for i in range(7):
                    if self.choice_nb[i].is_clicked(event.pos):
                        if(self.nb_hole_validate==False):
                            self.nb_hole=i+2 #si le nombre de trou n'a pas été choisit on met la valeur du bouton cliqué
                        else:
                            self.nb_color=i+2 #si le nombre de trou a été choisi le joueur choisit alors le nombre de couleur
                if(self.valid_button.is_clicked(event.pos) and  ((self.nb_hole!=0 and self.nb_hole_validate==False) or (self.nb_color!=0 and self.nb_hole_validate))):
                #on peut valider que si on a choisit un nombre
                    if(self.nb_hole_validate==False):
                        self.nb_hole_validate = True #le joueur a validé son nombre de trou
                    else :
                         return self.nb_color*10 + self.nb_hole #il a tout validé on retourne son nombre de couleurs dans les dizaine et le nombre de trous dans les untiés
                elif self.menu_button.is_clicked(event.pos)  :
                    if confirmation_popup(self.screen, "Retourner au menu ?"): #on demande confirmation si il veut retourné au menu
                        return "Menu"

                        
    def draw(self):
        self.screen.blit(self.back_ground, (0, 0))#met l'image en fond d'écran
        font_title = pygame.font.Font("Font/Coolvetica.otf", self.screen.get_height()//10) # police du titre
        text_customisation = font_title.render("Personnalisation", True, (255,255, 255))
        text_customisation_width = text_customisation.get_width()
        text_customisation_x = (self.screen.get_width() // 2) - (text_customisation_width // 2)
        text_customisation_y = self.screen.get_height() // 14
        self.screen.blit(text_customisation, (text_customisation_x,text_customisation_y))  # Afficher "customisation" en haut de l'écran
        self.menu_button.draw(self.screen) #dessine le bouton pour retourner au menu
        #text du choix
        font_text = pygame.font.Font("Font/Coolvetica.otf", self.screen.get_height()//15)
        text_choix_y = 2*self.screen.get_height()/6
        if(self.nb_hole==0):
            #on propose de choisir le nombre de trous mais pas de valider
            text_choix = font_text.render("Veuillez choisir le nombre de trous", True, (255, 255, 255))
            text_choix_x = (self.screen.get_width() // 2) - (text_choix.get_width() // 2) #centrage du texte
            self.screen.blit(text_choix, (text_choix_x,text_choix_y))
        elif(self.nb_hole!=0 and self.nb_hole_validate == False):
            #on propose de choisir le nombre de trous et de valider
            text_choix = font_text.render("Veuillez choisir le nombre de trous", True, (255, 255, 255))
            text_choix_x = (self.screen.get_width() // 2) - (text_choix.get_width() // 2)#centrage du texte
            self.screen.blit(text_choix, (text_choix_x,text_choix_y))
            self.valid_button.draw(self.screen)
        elif(self.nb_color==0 and self.nb_hole_validate == True):
            #on propose de choisir le nombre de couleurs mais pas de valider
            text_choix = font_text.render("Veuillez choisir le nombre de couleurs", True, (255, 255, 255))
            text_choix_x = (self.screen.get_width() // 2) - (text_choix.get_width() // 2)#centrage du texte
            self.screen.blit(text_choix, (text_choix_x,text_choix_y))
        else:
            #on propose de choisir le nombre de couleurs etde valider
            text_choix = font_text.render("Veuillez choisir le nombre de couleurs", True, (255, 255, 255))
            text_choix_x = (self.screen.get_width() // 2) - (text_choix.get_width() // 2) #centrage du texte
            self.screen.blit(text_choix, (text_choix_x,text_choix_y))
            self.valid_button.draw(self.screen)

        #affichage des boutons :
        for i in range(7):
            if self.nb_hole_validate == False :
                if i == self.nb_hole-2 :
                    self.choice_nb[i].color = (0,102,204) #on fonce la couleur du bouton coché
                else :
                    self.choice_nb[i].color = (51, 153, 255) #couleur du bouton par défaut
            else :
                if i == self.nb_color-2 :
                    self.choice_nb[i].color = (0,102,204) #on fonce la couleur du bouton coché
                else :
                    self.choice_nb[i].color = (51, 153, 255)#couleur du bouton par défaut
            self.choice_nb[i].draw(self.screen)   #on dessine les boutons 
