import os

def count_files_in_directory(directory_path):
    try:
        # Liste les éléments dans le répertoire
        items = os.listdir(directory_path)
        
        # Compte le nombre de fichiers (non répertoires)
        file_count = sum(1 for item in items if os.path.isfile(os.path.join(directory_path, item)))
        
        return file_count
    except FileNotFoundError:
        return "Le chemin spécifié est introuvable."
    except Exception as e:
        return f"Une erreur s'est produite : {e}"

# Exemple d'utilisation
directory_path = "/Data/harold.ngoupeyou/cheese_classification_challenge/projet/dataset/train/advanced_prompt_advanced_models/00-v2/STILTON"
print(f"Nombre de fichiers dans le dossier : {count_files_in_directory(directory_path)}")
