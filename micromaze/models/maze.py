"""Module définissant des objets en relation avec le concept de labyrinthe."""

from config.settings import PASSAGE, WALL, START, EXIT

from .position import Position


class Maze:
    """Classe représentant le plateau de jeu."""

    def __init__(self, mazefile):
        """Initialise un nouveau plateau de jeu."""
        self.hero = None
        self.passages = set()
        self.walls = set()
        self.start = None
        self.exit = None
        self.height = None
        self.width = None  
        self._load_from_file(mazefile)

    def _load_from_file(self, mazefile):
        """Charge le plateau de jeu à partir d'un fichier texte."""
        with mazefile.open() as maze:
            # On analyse le labyrithe ligne par ligne et colonne par colonne
            for y, line in enumerate(maze):
                for x, col in enumerate(line):
                    if col in (PASSAGE, START, EXIT):
                        self.passages.add(Position(x, y))
                    if col == START:
                        self.start = Position(x, y)
                    elif col == EXIT:
                        self.exit = Position(x, y)
                    else:
                        self.walls.add(Position(x, y))
            self.height, self.height = y+1, x+1

    def add(self, hero):
        """Place le héro sur le plateau de jeu."""
        hero.position = self.start
        hero.maze = self
        self.hero = hero

    def __contains__(self, position):
        """Retourne True si position est un passage du labyrinthe."""
        return position in self.passages


