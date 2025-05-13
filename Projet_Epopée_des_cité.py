from typing import List, Dict, Union
import json


class Joueur:

    def __init__(self, vie: int, force: int, inventaires: Dict[str, int]):
        self.vie = vie
        self.force = force
        self.inventaires = inventaires

    def afficher_lieux(self, lieux: List[Dict[str, Union[str, List[str]]]]) -> None:
        liste_des_lieux = [
            f"nom: {lieu["nom"]}, description: {lieu["description"]}, ressources :{lieu["ressources"]}, ennemis: {lieu["ennemis"]}"
            for lieu in lieux
        ]
        print(liste_des_lieux)

    def verification_inventaire(self) -> None:
        print(self.inventaires)

    def ajout_objet_inventaire(self, ressource: str) -> None:
        self.inventaires[ressource["nom"]] += ressource["quantite"]
        print(f"Vous avez récupérer {ressource["quantite"]} de {ressource["nom"]}")

    def payer_allie(self, allie: Dict[str, Union[str, int]]) -> None:
        print(allie["dialogue"])
        prix = allie["dialogue"].split()[-3]
        if prix > self.inventaires["or"]:
            print(f"Vous n'avez pas assez d'or pour payer {allie["nom"]}.")
        else:
            self.inventaires["or"] -= prix
            self.force += allie["force"]

    def attaquer(self, ennemi: Dict[str, Union[str, int]]) -> None:
        if self.force < ennemi["force"]:
            self.vie -= ennemi["force"]
            print(f"L'ennemi vous fait {ennemi["force"]} de point de dégats.")
        else:
            print(f"Vous avez tuer un {ennemi["nom"]}.")


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
