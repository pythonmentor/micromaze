"""Module définissant la facade du modèle représentant le jeu."""

from config.settings import BASE_DIR
from .maze import Maze
from .hero import Hero


class Game:

    def __init__(self):
        """Initialise le modèle de l'application."""
        self.hero = Hero()
        self.maze = Maze(BASE_DIR/'levels'/'level-01.txt')
        self.maze.add(self.hero)

    def move(self, direction):
        """Déplace le personnage principal de l'application."""
        self.hero.move(direction)