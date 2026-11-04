
import pygame as pg
from libraries.PygameTkinterGUITools import *


#& ----------------------------------

class createLabel():
  def __init__(self, scene, text, font_size, row):
    """Creates a label using Pygame Tkinter Gui Tools but makes it a little easier to read and write. Kind of just an extra layer of maintainability.

    Args:
        scene (str): The scene to which the label belongs. E.g. "menu" or "game"
        text (str): The text to display on the label
        font_size (int): The size of the font for the label
        row (int): The row position of the label
    """
    self.text = text
    self.font_size = font_size
    self.row = row
    self.scene = scene


  def draw(self):
    Label(self.scene, text=self.text, font_size=self.font_size).grid(row=self.row, column=0, pady=(0, 20))