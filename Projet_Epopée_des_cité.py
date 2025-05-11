from typing import List


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
