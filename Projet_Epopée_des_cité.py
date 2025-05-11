from typing import List, Dict, Union
import json


class Personnage:
    """Classes mére qui réprésente tous type de personnage avec un nom, un type, des points de force et un dialogue.
    Cette classe permet au personnage d'attaquer un ennemie et de soit réussir à tuer l'ennemie, soit le personnage se fait tuer.

    Attributs:
        nom (str): Le nom du personnage.
        type (str): Le type de personnage.
        force (int): Les points de force du personnage.
        dialogue (str): Le dialogue du personnage.

    Exemples:
        >>> liste_personnages = [
            {"nom": "Arwen", "type": "allié", "force": 5, "dialogue": "Je peux t'aider à explorer, mais il me faut 10 unités d'or."},
            {"nom": "Serpent Géant", "type": "ennemi", "force": 8, "dialogue": "Sssss... Tu ne passeras pas !"}
        ]
        >>> allie = Personnage("Arwen", "Allié", 5, "Je peux t'aider à explorer, mais il me faut 10 unités d'or.")
        >>> ennemie = Personnage("Serpent Géant", "ennemie", 8, "Sssss... Tu ne passeras pas !")
        >>> liste_personnages = allie.attaquer(ennemie, liste_personnages)
        "L'ennemie vous à tuer."
        >>> print(liste_personnages)
        [
            {"nom": "Serpent Géant", "type": "ennemi", "force": 8, "dialogue": "Sssss... Tu ne passeras pas !"}
        ]
        >>> allie = Personnage("Arwen", 10, "Je peux t'aider à explorer, mais il me faut 10 unités d'or.")
        >>> liste_personnages = allie.attaquer(ennemie, liste_personnages)
        "Vous avez réussie à tuer l'ennemie."
        >>> print(liste_personnages)
        [
            {"nom": "Arwen", "type": "allié", "force": 5, "dialogue": "Je peux t'aider à explorer, mais il me faut 10 unités d'or."}
        ]

    """

    def __init__(self, nom: str, type: str, force: int, dialogue: str):
        """Initialise un nouveau personnage.

        Args:
            nom (str): Le nom du personnage.
            type (str): Le type du personnage.
            force (int): La force du personnage.
            dialoguie (str): Le dialogue du personnage.
        """
        self.nom = nom
        self.type = type
        self.force = force
        self.dialogue = dialogue

    def attaquer(
        self, ennemie: object, personnages_jeu: List[Dict[str, Union[str, int]]]
    ) -> List[Dict[str, Union[str, int]]]:
        """Fonction qui décrit la capacité d'attaquer d'un personnage.
        Si le personnage à une force inférieur a celle de l'ennemie,
        il meurt et sera supprimer du jeu.

        Args:
            ennemie (object): Un personnage ennemie.
            personnages_jeu (List[Dict[str, Union[str, int]]]): Tous les personnages du jeu encore disponible.

        Returns:
            List[Dict[str, Union[str, int]]]: La liste des personnages restants.

        Exemples:
            >>> liste_personnages = [
                {"nom": "Arwen", "type": "allié", "force": 5, "dialogue": "Je peux t'aider à explorer, mais il me faut 10 unités d'or."},
                {"nom": "Serpent Géant", "type": "ennemi", "force": 8, "dialogue": "Sssss... Tu ne passeras pas !"}
            ]
            >>> allie = Personnage("Arwen", "Allié", 5, "Je peux t'aider à explorer, mais il me faut 10 unités d'or.")
            >>> ennemie = Personnage("Serpent Géant", "ennemie", 8, "Sssss... Tu ne passeras pas !")
            >>> liste_personnages = allie.attaquer(ennemie, liste_personnages)
            "L'ennemie vous à tuer."
            >>> print(liste_personnages)
            [
                {"nom": "Serpent Géant", "type": "ennemi", "force": 8, "dialogue": "Sssss... Tu ne passeras pas !"}
            ]
            >>> allie = Personnage("Arwen", 10, "Je peux t'aider à explorer, mais il me faut 10 unités d'or.")
            >>> liste_personnages = allie.attaquer(ennemie, liste_personnages)
            "Vous avez réussie à tuer l'ennemie."
            >>> print(liste_personnages)
            [
                {"nom": "Arwen", "type": "allié", "force": 5, "dialogue": "Je peux t'aider à explorer, mais il me faut 10 unités d'or."}
            ]
        """
        if ennemie.force > self.force:
            print("L'ennemie vous à tuer.")
            return delete_personnage(self, personnages_jeu)
        else:
            print("Vous avez réussie à tuer l'ennemie.")
            return delete_personnage(ennemie, personnages_jeu)


def load_json(
    filename: str,
) -> Dict[str, List[Dict[str, Union[str, List[str], int]]]]:
    """Fonction qui permet de charger des données à partir d'un fichier json.

    Args:
        filename (str): Le nom du fichier à partir duquel il faut charger les données.

    Returns:
        Dict[str, List[Dict[str, Union[str, List[str], int]]]]: Un dictionnaire qui contient
        trois liste de dictionnaire, le premier pour les lieux, le deuxiéme pour les
        personnages et le troisiéme pour les ressources.

    Raises:
        FileNotFoundError: Quand le fichier n'a pas été trouver.
        JSONDecodeError: Si il y a une erreur dans le json du fichier charger.

    Exemples:
        >>> data = load_json("data.json")
        >>> print(data)
        {
            "lieux": [
                {"nom": "Temple Oublié", "description": "Un temple envahi par la végétation", "ressources": ["or", "pierres"], "ennemis": ["serpent géant"]},
                {"nom": "Forêt Maudite", "description": "Une forêt sombre et mystérieuse", "ressources": ["bois", "herbes"], "ennemis": ["loup spectral"]}
            ],
            "personnages": [
                {"nom": "Arwen", "type": "allié", "force": 5, "dialogue": "Je peux t'aider à explorer, mais il me faut 10 unités d'or."},
                {"nom": "Serpent Géant", "type": "ennemi", "force": 8, "dialogue": "Sssss... Tu ne passeras pas !"}
            ],
            "ressources": [
                {"nom": "or", "quantite": 20, "utilite": "Acheter de l'aide"},
                {"nom": "bois", "quantite": 10, "utilite": "Construire des abris"}
            ]
        }
        >>> data = load_json("d")
        Traceback (most recent call last):
            ...
        FileNotFoundError: f"Le fichier {filename} n'a pas été trouver."
        Si il y a une erreur dans le fichier json.
        >>> data = load_json("data.json")
        Traceback (most recent call last):
            ...
        JSONDecodeError: f"Erreur de décodage : {e}"
    """
    try:
        with open(file=filename, mode="r", encoding="utf-8") as fichier:
            data = json.load(fichier)
    except FileNotFoundError as e:
        print(f"Le fichier {filename} n'a pas été trouver.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage : {e}")
        return {}
    return data


def delete_personnage(
    personnage: object, personnages_jeu: List[Dict[str, Union[str, int]]]
) -> List[Dict[str, Union[str, int]]]:
    """Fonction qui permet de supprimer un personnage.

    Args:
        personnage (object): Un personnage instancier avec la classe Personnage.
        personnages_jeu (List[Dict[str, Union[str, int]]]): Liste de dictionnaire
        qui représente la liste des personnages encore disponible dans la partie.

    Returns:
        List[Dict[str, Union[str, int]]]: La liste des personnages restants.

    Exemples:
        >>> liste_personnages = [
                {"nom": "Arwen", "type": "allié", "force": 5, "dialogue": "Je peux t'aider à explorer, mais il me faut 10 unités d'or."},
                {"nom": "Serpent Géant", "type": "ennemi", "force": 8, "dialogue": "Sssss... Tu ne passeras pas !"}
            ]
        >>> allie = Personnage("Arwen", "Allié", 5, "Je peux t'aider à explorer, mais il me faut 10 unités d'or.")
        >>> liste_personnage = delete_personnage(allie, liste_personnages)
        >>> print(liste_personnage)
        [
                {"nom": "Serpent Géant", "type": "ennemi", "force": 8, "dialogue": "Sssss... Tu ne passeras pas !"}
        ]
    """
    for p in personnages_jeu:
        if p["nom"] == personnage.nom:
            personnages_jeu.remove(p)
            return personnages_jeu


"""test"""

data = load_json("data.json")
print(data)
liste_personnages = data["personnages"]
print(liste_personnages)
allie = liste_personnages[0]
ennemie = liste_personnages[1]
allie = Personnage(allie["nom"], allie["type"], allie["force"], allie["dialogue"])
ennemie = Personnage(
    ennemie["nom"], ennemie["type"], ennemie["force"], ennemie["dialogue"]
)

liste_personnages = allie.attaquer(ennemie, liste_personnages)
print(liste_personnages)
allie.force = 20
data = load_json("data.json")
liste_personnages = data["personnages"]
liste_personnages = allie.attaquer(ennemie, liste_personnages)
print(liste_personnages)
