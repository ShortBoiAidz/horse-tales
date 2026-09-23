import pygame as pg
from data.components import player

playerObject = player.Player()

MAPSTATE = "caveEntrance"

class currentMap:
  def __init__(self):
    self.img = pg.image.load("assets/textures/mapsheets/cave_entrance.png")
    self.img = pg.transform.scale(self.img, (800, 600))

    self.map = caveEntranceMap()

    self.rect = self.img.get_rect()

  def update(self, screen):
    match MAPSTATE:
      case "caveEntrance":
        self.map.drawMap(screen)
        self.map.update()
      case "innerCave":
        self.map = innerCaveMap()
        self.map.drawMap(screen)
        self.map.update()

class caveEntranceMap:
  def __init__(self):
    self.entranceRect = pg.Rect(350, 230, 200, 100)
    self.img = pg.image.load("assets/textures/mapsheets/cave_entrance.png")
    self.img = pg.transform.scale(self.img, (800, 600))
    self.rect = self.img.get_rect()

  def drawMap(self, screen):
    screen.blit(self.img, self.rect.topleft)
    pg.draw.rect(screen, (0), self.entranceRect)

  def update(self):
    if self.entranceRect.colliderect(playerObject.rect):
      print("COLLIDE")
      MAPSTATE = "innerCave"

class innerCaveMap:
  def __init__(self):
    pass

  def drawMap(self, screen):
    pass

  def update(self):
    pass