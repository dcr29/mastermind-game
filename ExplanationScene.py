import pygame
from scene import Scene
from Button import Button
from confirmation import confirmation_popup



class ExplanationScene(Scene):
    #scene où les regles et le fonctionnement du jeux est expliquer
    # retour au menu possible grace à un bouton en haut à droite 
    def __init__(self, screen):
        super().__init__(screen)
        screen_width = screen.get_width()
        self.menu_button = Button(19*screen_width/20, 0,screen_width/20, screen_width/20, "menu",(0,128, 255),screen_width//60,50)
        self.back_ground = pygame.image.load("image/background_degrade.png") #chargement de l'image de fond de la scene d'explication
        self.back_ground = pygame.transform.scale(self.back_ground, (screen_width, self.screen.get_height())) #on redimensionne l'image de fond 
        

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            return "fin"
        elif event.type == pygame.MOUSEBUTTONUP:
          if event.button == 1:
                if self.menu_button.is_clicked(event.pos): #est-ce que le joueur a demandé à retourner au menu 
                    if confirmation_popup(self.screen, "Retourner au menu ?"):# on lui demande confirmation
                        return "Menu" #on veut chnager la scene pour la scene menu

    def draw(self):
        self.screen.blit(self.back_ground, (0, 0))#met l'image en fond d'écran
        self.menu_button.draw(self.screen) #dessine le boutton de retour
        #titre
        font_title = pygame.font.Font("Font/Coolvetica.otf", self.screen.get_height()//10) #charge la police et taille du titre
        text_title = font_title.render("Bienvenue sur Mastermind", True, (0, 255, 255)) 
        text_haut_x = (self.screen.get_width() // 2) - (text_title.get_width() // 2) #centrage du texte
        text_y = self.screen.get_height() // 12
        self.screen.blit(text_title, (text_haut_x,text_y))  # Afficher texte en haut de l'écran
        text_y += font_title.get_height()*1.6

        #paragraphe
        font_paragraphe = pygame.font.Font("Font/Coolvetica.otf", self.screen.get_height()//35)

        lines = ["Voici les règles du jeu Mastermind",
        "Le but du jeu est de trouver la combinaison de couleurs de billes choisie par l'ordinateur aléatoirement en un minimum d'essais.",
        "Trouver la bonne combinaison de billes revient à trouver la bonne position et la bonne couleur de chaque bille.",
        "Il existe plusieurs niveaux :",
        "       Facile              : 4 trous et 4 couleurs",
        "       Moyen            : 4 trous et 6 couleurs",
        "       Difficile           : 4 trous et 8 couleurs",
        "       Personnalisé   : A toi de choisir entre 2 à 8 trous et couleurs",
        " ",
        "Tu peux valider ta ligne lorsque tu as remplit tous les trous avec une couleur",
        "Après validation, tes anciennes lignes apparaissent en haut. À leur gauche s affiche ton nombre d éssais.",
        "À leur droite, en vert : le nombre de couleurs bien placées ; en orange : le nombre de bonnes couleurs mal placées.",
        " ",
        " ",
        " ",
        " "]

        for line in lines:
            line_text = font_paragraphe.render(line, True, (255, 255, 255)) #on transforme chaque ligne en texte à afficher
            self.screen.blit(line_text, (self.screen.get_width() // 10 ,text_y)) #on l'affiche
            text_y += font_paragraphe.get_height()*1.3 #on incrémente y
        
        #affichage bonne partie en bas
        text_GG = font_title.render("Bonne partie !!", True, (0, 255, 255)) #texte bonne partie
        text_GG_x = (self.screen.get_width() // 2) - (text_GG.get_width() // 2) #centrage du texte
        self.screen.blit(text_GG, (text_GG_x, self.screen.get_height() - text_GG.get_height()*1.5))  # Afficher texte en haut de l'écran
