# 🤖 Simulateur de robot avec système de logs

## Description
Ce projet simule un robot se déplaçant sur une grille 2D et enregistre 
toutes ses actions dans un fichier texte `robots_logs.txt` avec date précise.

Le robot gère automatiquement les obstacles, les bordures de grille et 
la consommation de batterie. Le système de logs est conçu pour être 
réutilisable sur des projets plus avancés.

J'ai créé ce projet pour apprendre à écrire dans des fichiers externes 
depuis Python et pour comprendre comment les systèmes embarqués 
trackent les actions en temps réel

## Fonctionnement
- On initialise un objet `Robot`
- On lui donne des instructions de déplacement (gauche, droite, haut, bas)
- Le robot détecte automatiquement les obstacles et les bordures
- La batterie diminue à chaque déplacement
- Chaque action est enregistrée dans `robots_logs.txt` avec l'heure exacte

**Exemple de logs générés :**
```
[2026-02-21 14:32:01] INFO - Robot avance à droite → [1, 0]
[2026-02-21 14:32:03] WARNING - Obstacle détecté, impossible d'avancer à droite
[2026-02-21 14:32:05] WARNING - Batterie à 50%
[2026-02-21 14:32:07] ERROR - Batterie vide, robot arrêté !
```

## Technologies & concepts

- **Python** — langage principal
- **datetime** — horodatage précis de chaque action
- **time** — cooldown entre les actions du robot
- **POO** — architecture en classes séparées (Robot, Logger)
- **Gestion de fichiers** — écriture et suppression de logs en temps réel

## Personnaliser le projet
Les obstacles et la taille de la grille se modifient dans `robot.py` :
```python
self.obstacles = [[3, 0], [6, 4], [10, 5]]  # positions des obstacles
self.largeur = 20   # largeur de la grille
self.hauteur = 15   # hauteur de la grille
```

Les actions du robot se définissent dans `main.py` :
```python
robot1.droite()   # déplacement à droite
robot1.gauche()   # déplacement à gauche
robot1.haut()     # déplacement vers le haut
robot1.bas()      # déplacement vers le bas
robot1.logger.vider()  # supprime tous les logs
```

## Installation
Consultez `requirements.txt` pour les dépendances nécessaires.

## Ce qui est prévu
- Envoi des logs par mail en cas d'erreur critique
- Export des logs en différents formats (CSV, JSON)
- Interface visuelle avec Pygame