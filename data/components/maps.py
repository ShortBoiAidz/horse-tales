# ==========================================
# PLEASE FIX. DOES NOT WORK.
# ==========================================
# ../game.py >> draw_game()
# has issues.
# Can't be fucked to debug any of it.
# ==========================================

from pytmx.util_pygame import load_pygame as lpg
import pygame as pg

class BarTile(pg.sprite.Sprite):
  def __init__(self, pos, surface, groups):
    super().__init__(groups)

    self.image = surface
    self.rect = self.image.get_rect(topleft = pos)

    for layer in barMapObject.bar.visibleLayers:
      if hasattr(layer, "data"):
        for x, y, surface in layer.tiles():
          pos = (x * 16, y * 16)
          BarTile(pos, surface, barSpriteGroup)

class BarMap():
  def __init__():
    global barSpriteGroup, bar

    bar = lpg("./assets/textures/mapsheets/bar.tmx")
    barSpriteGroup = pg.sprite.Group()

  def draw(screen):
    barSpriteGroup.draw(screen)

barMapObject = BarMap() # takes 0 positional arguments but 1 was given ????
barTileObject = BarTile() # can only assume this has problems too