import textdistance

### AMELIORATIONS : 
# si cheddar mozarella, mozarella doit gagenr (cheddar donne .1 à tous les fromages)
# pareille pour tomme et vache

def find_best_match(word, word_set):
    word = word.upper()
    distances = {w: textdistance.levenshtein.normalized_distance(w, word) for w in word_set}
    closest_word = min(distances, key=distances.get)
    return closest_word, textdistance.levenshtein.normalized_distance(closest_word, word)



dictionary = {
    "BRIE": ["BRIE DE MELUN"],
    "MELUN": ["BRIE DE MELUN"],
    "CAMEMBERT": ["CAMEMBERT"],
    "EPOISSES": ["EPOISSES"],
    "FOURME": ["FOURME D'AMBERT"],
    "D'AMBERT": ["FOURME D'AMBERT"],
    "RACLETTE": ["RACLETTE"],
    "MORBIER": ["MORBIER"],
    "SAINT-NECTAIRE": ["SAINT-NECTAIRE"],
    "ST-NECTAIRE": ["SAINT-NECTAIRE"],
    "NECTAIRE": ["SAINT-NECTAIRE"],
    "POULIGNY": ["POULIGNY SAINT-PIERRE"],
    "SAINT-PIERRE": ["POULIGNY SAINT-PIERRE"],
    "ST-PIERRE": ["POULIGNY SAINT-PIERRE"],
    "PIERRE": ["POULIGNY SAINT-PIERRE"],
    "ROQUEFORT": ["ROQUEFORT"],
    "COMTE": ["COMTE"],
    "CHEVRE": ["CHEVRE"],
    "PECORINO": ["PECORINO"],
    "NEUFCHATEL": ["NEUFCHATEL"],
    "CHEDDAR": ["CHEDDAR"],
    "BUCHETTE": ["BUCHETTE DE CHEVRE"],
    "CHEVRE.": ["BUCHETTE DE CHEVRE"],
    "PARMESAN": ["PARMESAN"],
    "SAINT-FELICIEN": ["SAINT-FELICIEN"],
    "ST-FELICIEN": ["SAINT-FELICIEN"],
    "FELICIEN": ["SAINT-FELICIEN"],
    "MONT": ["MONT D'OR"],
    "D'OR": ["MONT D'OR"],
    "DOR":["MONT D'OR"],
    "STILTON": ["STILTON"],
    "SCARMOZA": ["SCARMOZA"],
    "CABECOU": ["CABECOU"],
    "BEAUFORT": ["BEAUFORT"],
    "MUNSTER": ["MUNSTER"],
    "CHABICHOU": ["CHABICHOU"],
    "REBLOCHON": ["REBLOCHON"],
    "EMMENTAL": ["EMMENTAL"],
    "FETA": ["FETA"],
    "OSSAU": ["OSSAU-IRATY"],
    "IRATY": ["OSSAU-IRATY"],
    "OSSAU-IRATY": ["OSSAU-IRATY"],
    "MIMOLETTE": ["MIMOLETTE"],
    "MAROILLES": ["MAROILLES"],
    "GRUYERE": ["GRUYERE"],
    "MOTHAIS": ["MOTHAIS"],
    "VACHERIN": ["VACHERIN"],
    "MOZZARELLA": ["MOZZARELLA"],
    "TETE": ["TETE DE MOINES"],
    "MOINES": ["TETE DE MOINES"],
    "FRAIS": ["FROMAGE FRAIS"],

    "TOMME": ["TOMME DE VACHE"],

    "SAINT": ["SAINT-NECTAIRE", "POULIGNY SAINT-PIERRE", "SAINT-FELICIEN"],
    "BREBIS": ["ROQUEFORT", "PECORINO", "OSSAU-IRATY", "FETA"],
    "CHEVRE": ["CAMEMBERT", "CHABICHOU", "CHEVRE", "BUCHETTE DE CHEVRE", "FETA", "CABECOU", "MOTHAIS"],
    "GOAT": ["CAMEMBERT", "CHABICHOU", "CHEVRE", "BUCHETTE DE CHEVRE", "FETA", "CABECOU", "MOTHAIS"],
    "VACHE": ['BRIE DE MELUN', 'EPOISSES', "FOURME D'AMBERT", 'RACLETTE', 'MORBIER', 'SAINT-NECTAIRE', 'POULIGNY SAINT-PIERRE', 'COMTE', 'NEUFCHATEL', 'CHEDDAR', 'PARMESAN', 'SAINT-FELICIEN', "MONT D'OR", 'STILTON', 'SCARMOZA', 'BEAUFORT', 'MUNSTER', 'TOMME DE VACHE', 'REBLOCHON', 'EMMENTAL', 'MIMOLETTE', 'MAROILLES', 'GRUYERE', 'VACHERIN', 'MOZZARELLA', 'TETE DE MOINES', 'FROMAGE FRAIS'],


    "ITALIE": ["PECORINO", "PARMESAN", "MOZZARELLA", "SCARMOZA"],
    "GRECE": ["FETA"],
    "SUISSE": ["RACLETTE", "EMMENTAL", "GRUYERE"],
    "ANGLETERRE": ["STILTON", "CHEDDAR"],
    "ENGLAND": ["STILTON", "CHEDDAR"],
    "FRANCAIS": ["RACLETTE", 'BRIE DE MELUN', 'CAMEMBERT', 'EPOISSES', "FOURME D'AMBERT", 'MORBIER', 'SAINT-NECTAIRE', 'POULIGNY SAINT-PIERRE', 'ROQUEFORT', 'COMTE', 'CHEVRE', 'NEUFCHATEL', 'BUCHETTE DE CHEVRE', 'SAINT-FELICIEN', "MONT D'OR", 'CABECOU', 'BEAUFORT', 'MUNSTER', 'CHABICHOU', 'TOMME DE VACHE', 'REBLOCHON', 'OSSAU-IRATY', 'MIMOLETTE', 'MAROILLES', 'MOTHAIS', 'VACHERIN', 'TETE DE MOINES', 'FROMAGE FRAIS'],
    "BLEU": ["ROQUEFORT", "STILTON"],

    # confusions classique avec des noms de fromages
    "RECETTE": [], 
    "CHEESE": [], 
    "LAITERIE": [], 
    "FOURCE": [], 
    "PIECE": [], 
    "BOURSE": [], 
    "D'argent": [],
    "FROMAGE": [],
    "FINES": [],
    "VITAMINE": [],
    "FERME": [], 
    "ARTISAN": [],
    "MOINS": [],
    "BEFORE": [],
    "EPAISSES": [],
    "COMRTIME": [], #label de certaines images de droits réservés
}

fromages = sorted("""BRIE DE MELUN
CAMEMBERT
EPOISSES
FOURME D'AMBERT
RACLETTE
MORBIER
SAINT-NECTAIRE
POULIGNY SAINT-PIERRE
ROQUEFORT
COMTE
CHEVRE
PECORINO
NEUFCHATEL
CHEDDAR
BUCHETTE DE CHEVRE
PARMESAN
SAINT-FELICIEN
MONT D'OR
STILTON
SCARMOZA
CABECOU
BEAUFORT
MUNSTER
CHABICHOU
TOMME DE VACHE
REBLOCHON
EMMENTAL
FETA
OSSAU-IRATY
MIMOLETTE
MAROILLES
GRUYERE
MOTHAIS
VACHERIN
MOZZARELLA
TETE DE MOINES
FROMAGE FRAIS""".split("\n"))

def combine_conf(confiance, distance):
    return distance

def identification(detection):
    dico = {
        "BRIE DE MELUN": 0,
        "CAMEMBERT": 0,
        "EPOISSES": 0,
        "FOURME D'AMBERT": 0,
        "RACLETTE": 0,
        "MORBIER": 0,
        "SAINT-NECTAIRE": 0,
        "POULIGNY SAINT-PIERRE": 0,
        "ROQUEFORT": 0,
        "COMTE": 0,
        "CHEVRE": 0,
        "PECORINO": 0,
        "NEUFCHATEL": 0,
        "CHEDDAR": 0,
        "BUCHETTE DE CHEVRE": 0,
        "PARMESAN": 0,
        "SAINT-FELICIEN": 0,
        "MONT D'OR": 0,
        "STILTON": 0,
        "SCARMOZA": 0,
        "CABECOU": 0,
        "BEAUFORT": 0,
        "MUNSTER": 0,
        "CHABICHOU": 0,
        "TOMME DE VACHE": 0,
        "REBLOCHON": 0,
        "EMMENTAL": 0,
        "FETA": 0,
        "OSSAU-IRATY": 0,
        "MIMOLETTE": 0,
        "MAROILLES": 0,
        "GRUYERE": 0,
        "MOTHAIS": 0,
        "VACHERIN": 0,
        "MOZZARELLA": 0,
        "TETE DE MOINES": 0,
        "FROMAGE FRAIS": 0
    }


    l_potentiels = []
    for zone, mot, confiance in detection:

        for mot_simple in mot.split(' '):
            mot_detecte, distance = find_best_match(mot_simple, dictionary)
            final_conf = combine_conf(confiance, distance)
            
            if final_conf<0.01 or (final_conf<0.4 and len(mot_detecte)>4): # les mots de moins de 4 lettres doivent avoir 100% de bonnes lettres, trop d'erreur sinon (exemple, "mont" et mint, mon, ont, etc...)
                mots_vrai = dictionary[mot_detecte]
                l_potentiels.append((mots_vrai, mot, mot_detecte, final_conf))

    for (lmot_vrai, mot, mot_detecte, final_conf) in l_potentiels:
        for mot_vrai in lmot_vrai:
            dico[mot_vrai] = dico[mot_vrai]+1

    max_value = max(dico.values())

# Extraire les éléments associés à la valeur maximale
    max_elements = [k for k, v in dico.items() if v == max_value]

    liste_ind = [1.0 if nom in max_elements else 0.0 for nom in fromages]

    return liste_ind

