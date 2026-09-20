import pygame as pg
from data.components import player

playerObject = player.Player()

class currentMap:
  def __init__(self):
    self.img = pg.image.load("assets/textures/mapsheets/cave_entrance.png")
    self.img = pg.transform.scale(self.img, (800, 600))
    self.rect = self.img.get_rect()

  def drawMap(self, screen):
    self.img = pg.transform.scale(self.img, (800, 600))
    screen.blit(self.img, self.rect.topleft)