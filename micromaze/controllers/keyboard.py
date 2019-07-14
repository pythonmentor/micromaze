from curses import KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT


# Directions en fonction des touches du clavier
directions = {
    KEY_UP: "up",
    KEY_DOWN: "down",
    KEY_LEFT: "left",
    KEY_RIGHT: "right"
}

class KeyboardController:
    """Classe définissant les contrôles au clavier"""

    def __init__(self, game):
        """Initialisation du contrôleur."""
        self.game = game

    def process(self, screen):
        """Traites les entrées utilisateur."""
        # On capture le moment où l'utilisateur presse une flèche du clavier
        key = screen.getch()  
        if key == ord('q') or self.game.hero.found_exit():
            return False
        elif key in directions:
            self.game.move(directions[key])

        return True
            
