"""Ce module définit le contrôleur principal de l'application."""

import curses

from .models import game
from .controllers import keyboard
from .views import display


class Application:
    """Classe contrôlant la boucle de jeu principale."""

    def __init__(self):
        """Initilise l'application."""
        self.running = False
        self.game = game.Game()
        self.keyboard = keyboard.KeyboardController(self.game)
        self.display = display.GameDisplay(self.game)

    def start(self):
        """Démarre l'interface de l'application."""
        self.running = True
        # Exécute l'application dans une fenêtre curses.
        curses.wrapper(self._run)

    def _run(self, screen):
        """Boucle de jeu principale"""
        # Démarrage de la boucle principale
        self.display.update(screen)
        
        while self.running:
            self.running = self.keyboard.process(screen)
            self.display.update(screen)
            screen.refresh()

            