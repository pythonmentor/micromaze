"""Module définissant des objets en relation avec le concept de position dans
un labyrinthe.
"""


class Position(tuple):
    """Classe représentant une position dans un labyrinthe à deux dimensions"""

    def __new__(cls, x, y):
        """Crée une nouvelle position."""
        return super().__new__(cls, (x, y))
    
    @property
    def x(self):
        """Position horizontale dans le labyrinthe."""
        return self[0]

    @property
    def y(self):
        """Position verticale dans le labyrithe."""
        return self[1]

    @property
    def up(self):
        """Position adjacente située au dessus."""
        return self.__class__(self.x - 1, self.y)

    @property
    def down(self):
        """Position adjacente située au dessous."""
        return self.__class__(self.x + 1, self.y)

    @property
    def left(self):
        """Position adjacente située à gauche."""
        return self.__class__(self.x, self.y - 1)

    @property
    def right(self):
        """Position adjacente située à droite"""
        return self.__class__(self.x, self.y + 1)

    def get(self, direction):
        """Retourne la position adjancente située dans la direction spécifiée
        sous forme de chaine de charactère.
        """
        if direction not in ("up", "down", "left", "right"):
            return self
        return getattr(self, str(direction))

    
