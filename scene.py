import pygame
from Button import Button
from Line import Line
from ColorPalette import ColorPalette
from GameGestion import GameGestion
from confirmation import confirmation_popup
from DoneLineGestion import DoneLineGestion
from ScoreGestion import *

class Scene:
    def __init__(self, screen):
        self.screen = screen

    def handle_events(self, event):
        pass

    def draw(self):
        pass  

