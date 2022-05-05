"""
Core module
"""

import graphic_module
import word_module

from .game_engine import GameEngine

class AppCore():

    def __init__(self):
        self.game_engine = GameEngine()
        self.graphic_engine = graphic_module.AppWindow(self.game_engine)

    def launch_app(self):
        self.graphic_engine.start()
