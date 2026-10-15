import pygame as pg
from pytmx.util_pygame import load_pygame as lpg
from PygameTkinterGUITools import *

from data.states import mapstates

class BarMap(pg.sprite.Sprite):
  def __init__(self, pos, surface, groups):
    super().__init__(groups)

    self.image = surface
    self.rect = self.image.get_rect(topleft = pos)

  def draw(self, screen, mapSprites):
    mapSprites.draw(screen)

class DrawMaps():
  def draw(self, bar, mapSprites):
    for layer in bar.visible_layers:
      if hasattr(layer, "data"):
        for x, y, surface in layer.tiles():
          pos = (x * 16, y * 16)
          BarMap(pos, surface, mapSprites)