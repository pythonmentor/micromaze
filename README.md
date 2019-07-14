# Micro-jeu de labyrinthe

Ce projet est un jeu à vocation éducative démontrant comment utiliser python
et la programmation orientée objet pour implémenter un jeu simple en suivant
une séparation des couches basique avec le pattern architectural MVC.

La version terminal du jeu utilise curses, faisant partie de la bibliothèque 
standard de python, afin d'offrir un mode d'interaction proche de la version 
graphique.

La version graphique utilise la bibliothèque pygame (à venir).

## Installation des dépendances

Les dépendances de ce projet s'installent avec pipenv que vous devez au 
préalable installer sur votre ordinateur (`pip install pipenv`). Ensuite:

```
$ pipenv install
```

## Démarrage du programme

Pour lancer l'application, il suffit d'utiliser la commande suivante sans
activation préalable d'un environnement virtuel:

```
$ pipenv run python main.py
```
