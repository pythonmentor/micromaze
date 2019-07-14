"""Module définissant des objets en relation avec le héro du jeu."""


class Hero:
    """Classe représentant le héro se déplaçant sur le jeu."""

    def __init__(self):
        """Initialise un nouveau héro."""
        self.position = None
        self.maze = None

    def found_exit(self):
        """Prédicat qui retourne VRAI si le héro a trouvé la sortie."""
        return self.position == self.maze.exit

    def move(self, direction):
        """Déplace le héro dans la direction demandée."""
        new_position = self.position.get(direction)
        if new_position in self.maze:
            self.position = new_position

