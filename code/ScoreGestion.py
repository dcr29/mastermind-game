import json 
import shutil   # Pour faire des opérations sur les fichiers (copies etc...)
import os # Pour intéragir avec le système d'xploitation (recherche de fichiers .json)

# Fichier de score principal ('best_score.json') 
# et son modèle (tous les best_score à 'null') si le joueur n'a jamais joué au jeu ('best_score.template.json')
#score_file = "best_score.json"
#score_template_file = "best_score.template.json"

# Chemin du dossier où se trouvent vos .py
base_dir = os.path.dirname(os.path.abspath(__file__))

# Fichiers de score
score_file = os.path.join(base_dir, "best_score.json")
score_template_file = os.path.join(base_dir, "best_score.template.json")

default_score = {"Easy" : None, "Medium" : None, "Hard" : None} 

def load_score():
    # Si le fichier n'existe pas on le créer en utilisant le modèle 'best_score.template.json'
    if not os.path.exists(score_file):
        if os.path.exists(score_template_file):
            # On créer le fichier score_file en copiant le contenu du fichier score_template_file 
            # dans le fichier score_file
            shutil.copy(score_template_file, score_file) # src = score_template_file, dest = score_file
            
        # Sinon (si le modèle (score_template_file) n'existe pas) on créer le fichier contenant les scores par défaut
        else:
            with open(score_file, 'w') as fichier:
                json.dump(default_score, fichier)
    try:
        # Chargement du fichier score_file (il existe déjà)
        with open(score_file, 'r') as fichier:
            return json.load(fichier)
    except json.JSONDecodeError:
        # Si erreur dans le décodage du fichier json, on renvoie une copie du score par défaut
        return default_score.copy()
        
def save_score(scores):
    # Sauvgarde des scores dans le fichier json
    with open(score_file, 'w') as fichier:
        json.dump(scores, fichier)