# Mastermind-Project
## Projet programmation 2A 

### Nathan Kubiez-Develay / Dimitri Courtois Rozelot

**Règles du jeu :**

Le but du jeu est de trouver **la combinaison de couleurs de billes** choisie par l'ordinateur en **un minimum d'essais**.

Trouver la bonne combinaison de billes revient à trouver **la bonne position** et **la bonne couleur** de chaque bille.

Il existe plusieurs **modes de jeu** :

- "facile" : 4 trous pouvant accueillir les billes, 4 billes de couleurs différentes 
	
- "moyen" : 4 trous, 6 billes différentes

- "difficile" : 4 trous, 8 billes différentes

- "personalisable" : l'utilisateur peut choisir le nombre de trous entre 2 et 8 et le nombre de couleurs entre 2 et 8

Le joueur possède **un nombre d'essais infini** et son meilleur score par mode de jeu ("facile", "moyen", "difficile") est affiché en haut à gauche de la fenêtre de jeu.

Après chaque chaque essai, le nombre de billes de la **bonne couleur** et à la **bonne position** est indiqué par un **chiffre en vert**.

Le nombre de billes à la **bonne position** mais **pas de la bonne couleur** est indiqué par un **chiffre en orange**.

**Lancement du jeu :** 

  **Sur Windows**
  
Pour lancer notre jeu Mastermind il suffit de télécharger ou cloner le dépot Github, et d'avoir python3 et pygame d'installés sur votre PC.
Si tout est installé, pour lancer le jeu réalisez un double-clic sur le fichier `Mastermind_Windows.bat`.

( Comment vérifier si tout est installé et l'installer sinon: 
Ouvrez l'invite de commande et tapez `python3 --version` s'il apparaît *python3.Y.X c'est que python est installé mais si il apparaît *'python' n’est pas reconnu en tant que  commande interne ou externe.*, vous devez installer python en téléchargant la version de python depuis le lien https://www.python.org/downloads/ puis en exécutant le .exe, durant  l'installation pensez à cocher *Add Python 3.x to PATH* . Python3 est maintenant installé.  
Maintenant tapez `python -m pygame --version` dans l'invite de commande, s'il apparaît par exemple *2.3.0* c'est que pygame est installé vous pouvez donc lancer le jeu mais s'il apparaît une erreur comme *No module named pygame*, il faut installer pygame en tapant la commande `pip install pygame`. Pygame et python sont maintenant installés, le jeu peut être lancé ).

  **Sur Mac et Linux**

Pour lancer notre jeu Mastermind il suffit de télécharger ou cloner le dépot github, et d'avoir python3 et pygame d'installés sur votre PC.
Si tout est installé, il faut ajouter les droits d'exécution sur le fichier en tapant la commande `chmod +x Mastermind_mac_linux.sh`.
Enfin, vous pouvez exécuter le fichier Mastermind_mac_linux.sh avec la commande `./Mastermind_mac_linux.sh` une fois placé dans le dossier téléchargé.

( Comment vérifier si tout est installé et l'installer sinon:
Ouvrez le terminal et tapez `python3 --version` s'il apparaît *python3.Y.X c'est que python est installé mais s'il apparaît une erreur de type *command not found* c'est que python n'est pas installé il faut alors l'installer.  
Pour vérifier que pygame est installé, tapez la commande `python3 --version` s'il apparaît par exemple *2.3.0* c'est que pygame est installé, vous pouvez donc lancer le jeu mais s'il apparaît une erreur comme *No module named pygame*, il faut installer pygame en tapant la commande `pip install pygame`. Pygame et python sont maintenant installés, le jeu peut être lancé)






