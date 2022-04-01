"""
Graphic Module
"""

import pygame

DIM = W,H = 1024,600

class AppWindow():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(DIM)


if __name__ == "__main__":
    test = AppWindow()