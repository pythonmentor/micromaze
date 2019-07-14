"""Module définissant l'interface utilisateur principale de l'application."""

import curses


class GameDisplay:
    """Classe représentant l'UI principale de l'application."""

    def __init__(self, game):
        """Initialise le modèle."""
        self.game = game
        self.hero_position = None

    def _draw_background(self, screen):
        """Affiche le plateau de jeu initial."""
        # Initialisation de la bibliothèque curses de la bibliothèque standard
        screen.clear()
        curses.curs_set(False) # cache le curseur

        # Mesure de la hauteur et de la largeur du terminal
        height, width = screen.getmaxyx()

        # Initialisation des couleurs
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

        # Affichage du plateau de jeu: on couvre le fond de noir
        for position in self.game.maze.walls:
            screen.addstr(*position, ' ', curses.color_pair(3))
        # On affiche les passages
        for position in self.game.maze.passages:
            screen.addstr(*position, ' ', curses.color_pair(1))
        self.hero_position = self.game.hero.position

    def update(self, screen):
        """Met à jour l'affichage du plateau de jeu."""
        # Effacer le héro de sa position actuelle
        if not self.hero_position:
            self._draw_background(screen)
        if self.game.hero.found_exit():
            screen.addstr(
                self.game.maze.height+1, 0,'Bravo, vous avez trouvé la sortie!'
            )
        screen.addstr(*self.hero_position, ' ', curses.color_pair(1))
        screen.addstr(*self.game.maze.start, 'S', curses.color_pair(2))
        screen.addstr(*self.game.maze.exit, 'X', curses.color_pair(2))
        screen.addstr(*self.game.hero.position, 'M', curses.color_pair(1))
        self.hero_position = self.game.hero.position


    

    
