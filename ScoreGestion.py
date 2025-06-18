import json 
import os 

score_file = "best_score.json"
score_template_file = "best_score.template.json"


default_score = {"Easy" : None, "Medium" : None, "Hard" : None}

def load_score():
    if not os.path.exists(score_file):
        if os.path.exists(score_template_file):
            shutil.copy(score_template_file, score_file)
        else:
            with open(score_file, 'w') as fichier:
                json.dump(default_score, fichier)
    try:
        with open(score_file, 'r') as fichier:
            return json.load(fichier)
    except json.JSONDecodeError:
        return default_score.copy()
        
def save_score(scores):
    with open(score_file, 'w') as fichier:
        json.dump(scores, fichier)