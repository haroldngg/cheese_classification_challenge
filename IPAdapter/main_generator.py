import generator
import os





cheeses = {
    "Cabécou": {
        "nom_en_majuscule": "CABECOU",
        "description": "A small goat cheese, soft and creamy with a tangy, earthy flavor.",
        "negative_prompt": "non-goat cheese, hard texture, no earthy flavor, bland, dry"
    },
    "Pecorino": {
        "nom_en_majuscule": "PECORINO",
        "description": "A hard Italian cheese, salty and nutty, made from sheep's milk.",
        "negative_prompt": "non-Italian, non-sheep's milk, soft texture, bland, no salty taste"
    },
    "Vacherin": {
        "nom_en_majuscule": "VACHERIN",
        "description": "A soft cheese with a washed rind, creamy and rich with a strong aroma.",
        "negative_prompt": "hard texture, mild aroma, bland, non-creamy, dry"
    },
    "Chèvre": {
        "nom_en_majuscule": "CHÈVRE",
        "description": "A fresh goat cheese, tangy and creamy with a hint of citrus.",
        "negative_prompt": "non-goat cheese, hard texture, bland, no citrus hint, dry"
    },
    "Cheddar": {
        "nom_en_majuscule": "CHEDDAR",
        "description": "A hard cheese, sharp and tangy with a crumbly texture.",
        "negative_prompt": "soft texture, bland, non-crumbly, no sharp flavor, dry"
    },
    "Reblochon": {
        "nom_en_majuscule": "REBLOCHON",
        "description": "A soft cheese with a washed rind, creamy and mild with a fruity, nutty flavor.",
        "negative_prompt": "hard texture, dry, no fruity flavor, no nutty flavor, bland"
    },
    "Fromage frais": {
        "nom_en_majuscule": "FROMAGE FRAIS",
        "description": "A fresh cheese, mild and creamy with a smooth texture, perfect for spreading.",
        "negative_prompt": "hard texture, non-creamy, strong flavor, non-smooth, bland"
    },
    "Tomme de vache": {
        "nom_en_majuscule": "TOMME DE VACHE",
        "description": "A semi-hard cheese, earthy and nutty with a smooth, creamy texture.",
        "negative_prompt": "soft texture, no nutty flavor, bland, non-creamy, dry"
    },
    "Gruyère": {
        "nom_en_majuscule": "GRUYÈRE",
        "description": "A hard Swiss cheese, nutty and slightly sweet with a dense texture.",
        "negative_prompt": "soft texture, bland, no nutty flavor, non-Swiss, no sweet taste"
    },
    "Ossau- Iraty": {
        "nom_en_majuscule": "OSSAU-IRATY",
        "description": "A semi-hard cheese, nutty and creamy with a hint of olive, made from sheep's milk.",
        "negative_prompt": "non-sheep's milk, soft texture, no olive hint, bland, dry"
    },
    "Parmesan": {
        "nom_en_majuscule": "PARMESAN",
        "description": "A hard Italian cheese, salty and nutty with a granular texture, perfect for grating.",
        "negative_prompt": "soft texture, non-granular, bland, non-Italian, no salty taste"
    },
    "Beaufort": {
        "nom_en_majuscule": "BEAUFORT",
        "description": "A hard cheese, nutty and fruity with a firm texture, made from cow's milk.",
        "negative_prompt": "soft texture, non-cow's milk, no nutty flavor, bland, dry"
    },
    "Camembert": {
        "nom_en_majuscule": "CAMEMBERT",
        "description": "A soft cheese with a bloomy rind, smooth and creamy, with raw milk and mushroom aromas.",
        "negative_prompt": "hard texture, dry, no raw milk aroma, no mushroom aroma"
    },
    "Comté": {
        "nom_en_majuscule": "COMTÉ",
        "description": "A hard cheese, aged and nutty with a complex, buttery flavor.",
        "negative_prompt": "non-aged, soft texture, no nutty flavor, bland, dry"
    },
    "Saint-Félicien": {
        "nom_en_majuscule": "SAINT- FÉLICIEN",
        "description": "A soft cheese with a bloomy rind, creamy and mild with a buttery flavor.",
        "negative_prompt": "hard texture, bland, non-creamy, no buttery flavor, dry"
    },
    "Morbier": {
        "nom_en_majuscule": "MORBIER",
        "description": "A semi-soft cheese with a distinctive layer of ash, creamy with a mild, tangy flavor.",
        "negative_prompt": "no ash layer, hard texture, non-creamy, strong flavor, bland"
    },
    "Munster": {
        "nom_en_majuscule": "MUNSTER",
        "description": "A soft cheese with a washed rind, strong aroma and tangy, creamy flavor.",
        "negative_prompt": "hard texture, mild aroma, bland, non-creamy, no tangy flavor"
    },
    "Tête de moines": {
        "nom_en_majuscule": "TÊTE DE MOINES",
        "description": "A hard Swiss cheese, nutty and fruity, traditionally shaved into rosettes.",
        "negative_prompt": "soft texture, no nutty flavor, no fruity flavor, non-Swiss, bland"
    },
    "Raclette": {
        "nom_en_majuscule": "RACLETTE",
        "description": "A semi-hard cheese, perfect for melting, with a nutty and slightly salty taste.",
        "negative_prompt": "non-melting, bland, no nutty taste, no salty taste, soft texture"
    },
    "Feta": {
        "nom_en_majuscule": "FETA",
        "description": "A brined cheese, tangy and salty with a crumbly texture, made from sheep's milk.",
        "negative_prompt": "non-brined, no salty flavor, soft texture, non-crumbly, bland"
    },
    "Mothais": {
        "nom_en_majuscule": "MOTHAIS",
        "description": "A goat cheese with a bloomy rind, creamy and tangy with a delicate flavor.",
        "negative_prompt": "non-goat cheese, hard texture, no delicate flavor, bland, dry"
    },
    "Brie de Melun": {
        "nom_en_majuscule": "BRIE DE MELUN",
        "description": "A soft cheese with a bloomy rind, creamy and slightly tangy with mushroom notes.",
        "negative_prompt": "hard texture, dry, bland, no mushroom notes, non-creamy"
    },
    "Saint-Nectaire": {
        "nom_en_majuscule": "SAINT-NECTAIRE",
        "description": "A semi-soft cheese with a washed rind, creamy and earthy with a fruity finish.",
        "negative_prompt": "hard texture, dry, non-creamy, no fruity finish, bland"
    },
    "Stilton": {
        "nom_en_majuscule": "STILTON",
        "description": "A blue cheese, crumbly and creamy with a strong, tangy flavor.",
        "negative_prompt": "non-blue cheese, soft texture, no tangy flavor, bland, non-crumbly"
    },
    "Bûchette de chèvre": {
        "nom_en_majuscule": "BÛCHETTE DE CHÈVRE",
        "description": "A fresh goat cheese log, tangy and creamy with a hint of earthiness.",
        "negative_prompt": "non-goat cheese, hard texture, no earthy hint, bland, dry"
    },
    "Chabichou": {
        "nom_en_majuscule": "CHABICHOU",
        "description": "A goat cheese with a bloomy rind, smooth and tangy with a hint of hazelnut.",
        "negative_prompt": "non-goat cheese, hard texture, no hazelnut hint, bland, dry"
    },
    "Mont d'Or": {
        "nom_en_majuscule": "MONTDOR",
        "description": "A soft cheese with a washed rind, creamy and rich with a woody aroma.",
        "negative_prompt": "hard texture, non-creamy, no woody aroma, bland, dry"
    },
    "Mozzarella": {
        "nom_en_majuscule": "MOZZARELLA",
        "description": "A fresh Italian cheese, mild and milky with a stretchy texture.",
        "negative_prompt": "non-Italian, hard texture, strong flavor, non-stretchy, dry"
    },
    "Mimolette": {
        "nom_en_majuscule": "MIMOLETTE",
        "description": "A hard cheese, nutty and caramel-like with a bright orange color.",
        "negative_prompt": "soft texture, non-orange color, no nutty flavor, no caramel-like flavor, bland"
    },
    "Emmental": {
        "nom_en_majuscule": "EMMENTAL",
        "description": "A hard Swiss cheese, nutty and mild with characteristic holes.",
        "negative_prompt": "no holes, strong flavor, bland, soft texture, no nutty flavor"
    },
    "Maroilles": {
        "nom_en_majuscule": "MAROILLES",
        "description": "A soft cheese with a washed rind, strong aroma and tangy, creamy flavor.",
        "negative_prompt": "hard texture, mild aroma, bland, non-creamy, no tangy flavor"
    },
    "Neufchâtel": {
        "nom_en_majuscule": "NEUFCHATEL",
        "description": "A soft cheese with a bloomy rind, similar to Camembert but with a heart shape and milder flavor.",
        "negative_prompt": "hard texture, dry, no heart shape, strong flavor, non-creamy"
    },
    "Fourme d'Ambert": {
        "nom_en_majuscule": "FOURME DAMBERT",
        "description": "A blue-veined cheese, mild and creamy, with blue veins and a subtle nutty flavor.",
        "negative_prompt": "non-veined, no blue veins, hard texture, strong flavor, no nutty flavor"
    },
    "Époisses": {
        "nom_en_majuscule": "EPOISSES",
        "description": "A soft cheese with a washed rind, known for its strong smell and tangy, creamy flavor.",
        "negative_prompt": "mild aroma, bland, hard texture, non-creamy"
    },
    "Roquefort": {
        "nom_en_majuscule": "ROQUEFORT",
        "description": "A blue cheese, rich and creamy with a sharp, tangy flavor and strong aroma.",
        "negative_prompt": "non-blue cheese, mild flavor, non-creamy, no strong aroma, bland"
    },
    "Scarmoza": {
        "nom_en_majuscule": "SCARMOZA",
        "description": "A semi-hard Italian cheese, smoky and mild with a firm texture.",
        "negative_prompt": "non-Italian, no smoky flavor, soft texture, strong flavor, bland"
    },
        "Pouligny-Saint- Pierre": {
        "nom_en_majuscule": "POULIGNY SAINT- PIERRE",
        "description": "A goat cheese with a bloomy rind, smooth and tangy with a hint of hazelnut.",
        "negative_prompt": "non-goat cheese, hard texture, no hazelnut hint, bland, dry"
    }
}


for key in cheeses:
    value = cheeses[key]
    name = value['nom_en_majuscule']
    print(name)
    directory = '../input/val_simplified/' + name
    p_prompt = value['description']
    n_prompt = value['negative_prompt']

    generator.main(repo_image=name, positive_prompt=p_prompt, negative_prompt=n_prompt, name_repo_depo= name)
