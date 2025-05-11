# Épopée des Cités Perdues

### Thème du projet : "L’Épopée des Cités Perdues"

Le projet est un jeu textuel où le joueur incarne un explorateur chargé de redonner vie à des cités perdues. Il devra gérer des ressources, explorer des lieux, interagir avec des personnages (alliés ou ennemis) et relever des défis. Les données de base (personnages, lieux, ressources, etc.) sont fournies dans un fichier JSON, et le joueur interagit via la console.

Objectif du projet : Créer une version simple du jeu où le joueur explore une cité, gère des ressources et interagit avec des personnages via des choix textuels.


## Fichier JSON fourni : Un fichier data.json contient :

Une liste de lieux (par exemple, "Temple Oublié", "Forêt Maudite") avec des caractéristiques (nom, description, ressources disponibles, ennemis présents).
Une liste de personnages (nom, type [allié/ennemi], force, dialogue).
Une liste de ressources (nom, quantité initiale, utilité).
Exemple de data.json :

```json
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
```

## Mécaniques du jeu :

Le joueur commence avec un inventaire vide et un certain nombre de points de vie (par exemple, 100).
Le joueur peut :
Explorer un lieu (afficher sa description, récupérer des ressources, affronter un ennemi via un système de "combat" simple basé sur des comparaisons de force).
Interagir avec un personnage (dialoguer, payer un allié pour obtenir de l’aide, fuir un ennemi).
Gérer son inventaire (ajouter des ressources, vérifier les quantités).
Les choix du joueur sont faits via des entrées textuelles (par exemple, "1 pour explorer, 2 pour parler à un personnage, 3 pour quitter").
Les données du jeu (inventaire, points de vie, etc.) sont sauvegardées dans un fichier JSON à la fin de chaque session.

## Exemple de fonctionnalités à implémenter :

Lecture du JSON : Utiliser le module json pour charger les données.
Affichage des lieux : Une boucle pour afficher les lieux disponibles et leurs descriptions.
Combat simple : Une fonction qui compare la force du joueur (fixée ou augmentée par des ressources) à celle d’un ennemi, avec des conditions (if/else) pour déterminer l’issue.
Gestion de l’inventaire : Utiliser des dictionnaires pour stocker les ressources et des listes pour suivre les objets collectés.
Choix du joueur : Utiliser match-case pour gérer les entrées du joueur (par exemple, "explorer", "combattre", "quitter").
Sauvegarde : Écrire l’état du jeu (inventaire, points de vie) dans un fichier JSON.
Livrable attendu : Un programme structuré (selon PEP8) avec des fonctions bien documentées (docstrings), qui permet de jouer une session simple du jeu et de sauvegarder son état.
