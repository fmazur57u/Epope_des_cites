from typing import List, Dict, Union
import json


class Joueur:
    """Classes qui réprésente le joueur avec un inventaire, des points de vie et des points de force.
    Cette classe permet au joueur combattre les ennemies,

    Attributs:
        inventaire (List[str]): La liste d'objet disponible dans l'inventaire. Le joueur peut utiliser les ressources dans sont inventaire.
        points de vie  (int): Les points de vie du joueur. Si c'est égale à 0, le joueur à perdus le jeu.
        points de force (int): Les points de force qui permette d'évaluer si le joueur est plus ou moins fortt qu'un ennemis.

    Exemples:
        >>> joueur = Joueur([], 100, 5)

    """

    def __init__(self, inventaire: List[str], points_de_vie: int, force: int):
        self.inventaire = inventaire
        self.points_de_vie = points_de_vie
        self.force = force


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
        >>> data = load_json(data.json)
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


data = load_json("data.json")
print(data)
